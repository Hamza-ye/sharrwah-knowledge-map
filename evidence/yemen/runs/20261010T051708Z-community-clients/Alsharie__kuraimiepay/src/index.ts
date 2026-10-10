import axios, {AxiosError, AxiosInstance} from 'axios';
import {Buffer} from 'node:buffer';
import * as https from "node:https"; // Use 'node:buffer' for explicit Node.js Buffer

// --- Type Definitions ---

interface KuraimiEPayClientOptions {
    username: string;
    password: string;
    environment?: 'UAT' | 'PROD';
    baseUrl?: string; // Optional: Override the base URL

    /**
     * DANGER: Set to `true` to disable SSL/TLS certificate verification.
     * ONLY use this for trusted UAT/development environments where the server
     * might have a self-signed certificate. NEVER use in production.
     * Defaults to `false`.
     */
    dangerouslyDisableSSLCertVerification?: boolean; // New option
}

interface BaseApiPayload {
    SCustID: string;
    REFNO: string;
}

export interface SendPaymentPayload extends BaseApiPayload {
    AMOUNT: number;
    CRCY?: string; // YER is default
    MRCHNTNAME: string;
    PINPASS: string; // 4-digit PIN, will be base64 encoded
}

export interface ReversePaymentPayload extends BaseApiPayload {
}

interface ResultSet {
    PH_REF_NO?: string; // Present in successful payment/reversal
}

export interface ApiResponse<T = ResultSet | null> {
    Code: number; // 1 for success, others for failure
    Message: string; // English message
    MessageDesc: string; // Arabic message
    Date: string; // ISO-like date string
    ResultSet: T;
}

export interface ApiErrorResponseData extends Omit<ApiResponse<null>, 'Code'> {
    Code?: number; // Sometimes error responses might not have a standard Code
}

export interface ApiError extends Error {
    statusCode?: number;
    data?: ApiErrorResponseData;
    originalError?: AxiosError | Error;
}


// --- Constants ---

const UAT_BASE_URL = 'https://web.krmbank.net.ye:44746';
// PROD_BASE_URL should be provided by Kuraimi Bank
// const PROD_BASE_URL = 'YOUR_PRODUCTION_BASE_URL';

const API_PATHS = {
    sendPayment: '/alk-payments-exp/v1/PHEPaymentAPI/EPayment/SendPayment',
    reversePayment: '/alk-payments-exp/v1/PHEPaymentAPI/EPayment/ReversePayment',
};

// --- Client Class ---

class KuraimiEPayClient {
    private axiosInstance: AxiosInstance;
    private username: string;
    private password: string;
    private environment: 'UAT' | 'PROD';

    constructor({
                    username,
                    password,
                    environment = 'UAT',
                    baseUrl,
                    dangerouslyDisableSSLCertVerification = false, // Default to false (secure)
                }: KuraimiEPayClientOptions) {
        if (!username || !password) {
            throw new Error('Username and Password are required.');
        }

        this.username = username;
        this.password = password;
        this.environment = environment;

        let effectiveBaseUrl = baseUrl;
        if (!effectiveBaseUrl) {
            if (this.environment === 'UAT') {
                effectiveBaseUrl = UAT_BASE_URL;
            } else if (this.environment === 'PROD') {
                // Replace with actual PROD_BASE_URL when available
                throw new Error('Production base URL is not defined. Please provide it via options.baseUrl or update the SDK.');
                // effectiveBaseUrl = PROD_BASE_URL;
            } else {
                // This case should be caught by the type system for `environment`
                throw new Error(`Invalid environment: ${this.environment}. Choose 'UAT' or 'PROD'.`);
            }
        }

        const authHeader = `Basic ${Buffer.from(`${this.username}:${this.password}`).toString('base64')}`;

        let httpsAgentOptions: https.AgentOptions = {};
        if (dangerouslyDisableSSLCertVerification === true) {
            console.warn(
                '[KuraimiEPayClient] WARNING: SSL/TLS certificate verification is DISABLED. ' +
                'This should ONLY be used for trusted UAT/development environments.'
            );
            httpsAgentOptions.rejectUnauthorized = false;
        }

        this.axiosInstance = axios.create({
            baseURL: effectiveBaseUrl,
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'Authorization': authHeader,
            },
            httpsAgent: new https.Agent(httpsAgentOptions), // Apply the httpsAgent
        });
    }

    private _encodePin(pinpass: string): string {
        // Basic validation, API might enforce more strictly

        return Buffer.from(pinpass).toString('base64');
    }

    private async _handleApiError(error: unknown): Promise<never> {
        const apiError: ApiError = new Error();

        if (axios.isAxiosError(error)) {
            apiError.message = `API Error: ${error.response?.status || 'Network Error'} ${error.response?.statusText || ''}`.trim();
            apiError.statusCode = error.response?.status;
            apiError.data = error.response?.data as ApiErrorResponseData; // Assert type for convenience
            apiError.originalError = error;
        } else if (error instanceof Error) {
            apiError.message = `Client Error: ${error.message}`;
            apiError.originalError = error;
        } else {
            apiError.message = 'An unknown error occurred';
        }
        throw apiError;
    }

    public async sendPayment(paymentData: SendPaymentPayload): Promise<ApiResponse> {
        const {SCustID, REFNO, AMOUNT, CRCY = 'YER', MRCHNTNAME, PINPASS} = paymentData;

        if (!SCustID || !REFNO || AMOUNT === undefined || !MRCHNTNAME || !PINPASS) {
            throw new Error('Missing required fields for sendPayment.');
        }

        const payload = {
            SCustID,
            REFNO,
            AMOUNT,
            CRCY,
            MRCHNTNAME,
            PINPASS: this._encodePin(PINPASS),
        };

        try {
            const response = await this.axiosInstance.post<ApiResponse>(API_PATHS.sendPayment, payload);
            return response.data;
        } catch (error) {
            return this._handleApiError(error);
        }
    }

    public async reversePayment(reversalData: ReversePaymentPayload): Promise<ApiResponse> {
        const {SCustID, REFNO} = reversalData;

        if (!SCustID || !REFNO) {
            throw new Error('Missing required fields for reversePayment: SCustID, REFNO.');
        }

        const payload = {
            SCustID,
            REFNO,
        };

        try {
            const response = await this.axiosInstance.post<ApiResponse>(API_PATHS.reversePayment, payload);
            return response.data;
        } catch (error) {
            return this._handleApiError(error);
        }
    }
}

export default KuraimiEPayClient;
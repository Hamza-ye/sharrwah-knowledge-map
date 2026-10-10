"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const axios_1 = __importDefault(require("axios"));
const node_buffer_1 = require("node:buffer"); // Use 'node:buffer' for explicit Node.js Buffer
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
    constructor({ username, password, environment = 'UAT', baseUrl }) {
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
            }
            else if (this.environment === 'PROD') {
                // Replace with actual PROD_BASE_URL when available
                throw new Error('Production base URL is not defined. Please provide it via options.baseUrl or update the SDK.');
                // effectiveBaseUrl = PROD_BASE_URL;
            }
            else {
                // This case should be caught by the type system for `environment`
                throw new Error(`Invalid environment: ${this.environment}. Choose 'UAT' or 'PROD'.`);
            }
        }
        const authHeader = `Basic ${node_buffer_1.Buffer.from(`${this.username}:${this.password}`).toString('base64')}`;
        this.axiosInstance = axios_1.default.create({
            baseURL: effectiveBaseUrl,
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'Authorization': authHeader,
            },
        });
    }
    _encodePin(pinpass) {
        // Basic validation, API might enforce more strictly
        if (typeof pinpass !== 'string') {
            console.warn('PINPASS should be a string.');
        }
        return node_buffer_1.Buffer.from(pinpass).toString('base64');
    }
    async _handleApiError(error) {
        const apiError = new Error();
        if (axios_1.default.isAxiosError(error)) {
            apiError.message = `API Error: ${error.response?.status || 'Network Error'} ${error.response?.statusText || ''}`.trim();
            apiError.statusCode = error.response?.status;
            apiError.data = error.response?.data; // Assert type for convenience
            apiError.originalError = error;
        }
        else if (error instanceof Error) {
            apiError.message = `Client Error: ${error.message}`;
            apiError.originalError = error;
        }
        else {
            apiError.message = 'An unknown error occurred';
        }
        throw apiError;
    }
    async sendPayment(paymentData) {
        const { SCustID, REFNO, AMOUNT, CRCY = 'YER', MRCHNTNAME, PINPASS } = paymentData;
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
            const response = await this.axiosInstance.post(API_PATHS.sendPayment, payload);
            return response.data;
        }
        catch (error) {
            return this._handleApiError(error);
        }
    }
    async reversePayment(reversalData) {
        const { SCustID, REFNO } = reversalData;
        if (!SCustID || !REFNO) {
            throw new Error('Missing required fields for reversePayment: SCustID, REFNO.');
        }
        const payload = {
            SCustID,
            REFNO,
        };
        try {
            const response = await this.axiosInstance.post(API_PATHS.reversePayment, payload);
            return response.data;
        }
        catch (error) {
            return this._handleApiError(error);
        }
    }
}
exports.default = KuraimiEPayClient;

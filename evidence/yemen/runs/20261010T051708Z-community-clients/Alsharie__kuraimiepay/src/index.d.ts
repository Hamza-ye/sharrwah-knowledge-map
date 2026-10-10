import { AxiosError } from 'axios';
interface KuraimiEPayClientOptions {
    username: string;
    password: string;
    environment?: 'UAT' | 'PROD';
    baseUrl?: string;
}
interface BaseApiPayload {
    SCustID: string;
    REFNO: string;
}
export interface SendPaymentPayload extends BaseApiPayload {
    AMOUNT: number;
    CRCY?: string;
    MRCHNTNAME: string;
    PINPASS: string;
}
export interface ReversePaymentPayload extends BaseApiPayload {
}
interface ResultSet {
    PH_REF_NO?: string;
}
export interface ApiResponse<T = ResultSet | null> {
    CODE: number;
    MESSAGE: string;
    MESSAGEDESC: string;
    DATE: string;
    ResultSet: T;
}
export interface ApiErrorResponseData extends Omit<ApiResponse<null>, 'CODE'> {
    CODE?: number;
}
export interface ApiError extends Error {
    statusCode?: number;
    data?: ApiErrorResponseData;
    originalError?: AxiosError | Error;
}
declare class KuraimiEPayClient {
    private axiosInstance;
    private username;
    private password;
    private environment;
    constructor({ username, password, environment, baseUrl }: KuraimiEPayClientOptions);
    private _encodePin;
    private _handleApiError;
    sendPayment(paymentData: SendPaymentPayload): Promise<ApiResponse>;
    reversePayment(reversalData: ReversePaymentPayload): Promise<ApiResponse>;
}
export default KuraimiEPayClient;

import KuraimiEPayClient, {ApiError, ApiResponse, ReversePaymentPayload} from '../index'; // Adjust if installed

// IMPORTANT: Replace with your actual credentials and details
const apiClient = new KuraimiEPayClient({
    username: 'YOUR_SUPPLIER_USERNAME', // Provided by Kuraimi Bank
    password: 'YOUR_SUPPLIER_PASSWORD', // Provided by Kuraimi Bank
    environment: 'UAT', // Or 'PROD' when available and configured
});

async function reverseTransaction() {
    const reversalDetails: ReversePaymentPayload = {
        SCustID: 'SC12345',  // Customer ID used in the original transaction
        REFNO: 'TS_TXN1678886660000', // REFNO of the transaction to be reversed
    };

    console.log('Sending reversal request for:', reversalDetails);

    try {
        const response: ApiResponse = await apiClient.reversePayment(reversalDetails);
        console.log('Reversal Response:');
        console.dir(response, {depth: null});

        if (response.CODE === 1) {
            console.log('Reversal Successful! Bank Reference (if applicable):', response.ResultSet?.PH_REF_NO);
        } else {
            console.error('Reversal Failed. Code:', response.CODE, 'Message:', response.MESSAGE, 'Description:', response.MESSAGEDESC);
        }
    } catch (error) {
        const apiError = error as ApiError; // Type assertion
        console.error('Error reversing transaction:');
        if (apiError.data) {
            console.error('API Error Data:', apiError.data);
        } else {
            console.error(apiError.message || apiError);
        }
        if (apiError.statusCode) {
            console.error('Status Code:', apiError.statusCode);
        }
    }
}

reverseTransaction();
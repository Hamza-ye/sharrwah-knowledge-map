import KuraimiEPayClient, {ApiError, ApiResponse, SendPaymentPayload} from '../index'; // Adjust if installed

// IMPORTANT: Replace with your actual credentials and details
const apiClient = new KuraimiEPayClient({
    username: 'YOUR_SUPPLIER_USERNAME', // Provided by Kuraimi Bank
    password: 'YOUR_SUPPLIER_PASSWORD', // Provided by Kuraimi Bank
    environment: 'UAT', // Or 'PROD' when available and configured
});

async function makePayment() {
    const paymentDetails: SendPaymentPayload = {
        SCustID: 'SC12345',      // Customer ID from your system
        REFNO: `TS_TXN${Date.now()}`, // Unique reference number for this transaction
        AMOUNT: 1000.00,         // Transaction amount
        // CRCY: 'YER',          // Currency (YER is default, optional)
        MRCHNTNAME: 'My Test Merchant TS', // Your merchant name
        PINPASS: '1234',         // Customer's 4-digit PIN
    };

    console.log('Sending payment with details:', paymentDetails);

    try {
        const response: ApiResponse = await apiClient.sendPayment(paymentDetails);
        console.log('Payment Response:');
        console.dir(response, {depth: null});

        if (response.CODE === 1 && response.ResultSet?.PH_REF_NO) {
            console.log('Payment Successful! Bank Reference:', response.ResultSet.PH_REF_NO);
        } else {
            console.error('Payment Failed. Code:', response.CODE, 'Message:', response.MESSAGE, 'Description:', response.MESSAGEDESC);
        }
    } catch (error) {
        const apiError = error as ApiError; // Type assertion
        console.error('Error making payment:');
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

makePayment();
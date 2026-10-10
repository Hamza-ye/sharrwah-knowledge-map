package com.example.autopayapp.receivers

import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent
import android.provider.Telephony
import android.util.Log
import com.example.autopayapp.api.ApiClient
import com.example.autopayapp.utils.MessageParser

class SmsReceiver : BroadcastReceiver() {

    private val TAG = "SmsReceiver"

    override fun onReceive(context: Context, intent: Intent) {
        if (intent.action == Telephony.Sms.Intents.SMS_RECEIVED_ACTION) {
            val messages = Telephony.Sms.Intents.getMessagesFromIntent(intent)
            
            for (sms in messages) {
                val sender = sms.displayOriginatingAddress ?: ""
                val body = sms.displayMessageBody ?: ""

                // Check if the sender is a supported digital wallet service
                if (isWalletSender(sender)) {
                    Log.d(TAG, "Captured Wallet SMS from: $sender, Body: $body")

                    val parsedTx = MessageParser.parse(body, sender)
                    // Forward the captured information to the server
                    ApiClient.processPayment(context, "sms-$sender", parsedTx ?: com.example.autopayapp.utils.ParsedTransaction("Unknown", "0", "", sender, body))
                }
            }
        }
    }

    private fun isWalletSender(sender: String): Boolean {
        val supportedSenders = listOf(
            "KuraimiIMB",
            "KuraimiBank",
            "Jawaly",
            "Jaib",
            "SamaYemen"
        )
        return supportedSenders.any { sender.contains(it, ignoreCase = true) } || sender.contains("wallet", ignoreCase = true)
    }
}

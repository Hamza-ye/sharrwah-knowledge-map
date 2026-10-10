package com.example.autopayapp.services

import android.service.notification.NotificationListenerService
import android.service.notification.StatusBarNotification
import android.util.Log
import com.example.autopayapp.api.ApiClient
import com.example.autopayapp.utils.MessageParser

class NotificationListener : NotificationListenerService() {

    private val TAG = "NotificationListener"

    override fun onNotificationPosted(sbn: StatusBarNotification) {
        val packageName = sbn.packageName
        
        if (isWalletApp(packageName)) {
            val extras = sbn.notification.extras
            val title = extras.getString("android.title") ?: ""
            val text = extras.getCharSequence("android.text")?.toString() ?: ""

            val fullText = "$title: $text"
            Log.d(TAG, "Captured Wallet Notification from: $packageName, Text: $fullText")

            val parsedTx = MessageParser.parse(fullText, packageName)
            if (parsedTx != null) {
                // Forward the captured information to the server
                ApiClient.processPayment(this, "notification-$packageName", parsedTx)
            } else {
                Log.w(TAG, "Notification ignored: Did not match any known payment formats. ($fullText)")
            }
        }
    }

    private fun isWalletApp(packageName: String): Boolean {
        val supportedWallets = listOf(
            "com.kuraimi.bank",
            "com.samayemen.wallet",
            "com.jawaly.app",
            "com.jaib.wallet"
        )
        return supportedWallets.contains(packageName) || packageName.contains("wallet", ignoreCase = true)
    }

    override fun onNotificationRemoved(sbn: StatusBarNotification) {
        // Notification dismissed
    }
}

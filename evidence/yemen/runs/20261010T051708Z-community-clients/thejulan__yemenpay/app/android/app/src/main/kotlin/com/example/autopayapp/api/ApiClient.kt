package com.example.autopayapp.api

import android.content.Context
import android.util.Log
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import org.json.JSONObject
import java.io.OutputStreamWriter
import java.net.HttpURLConnection
import java.net.URL
import android.app.NotificationManager
import android.app.NotificationChannel
import android.os.Build
import androidx.core.app.NotificationCompat
import android.os.Handler
import android.os.Looper
import com.example.autopayapp.MainActivity
import com.example.autopayapp.utils.ParsedTransaction
import java.text.SimpleDateFormat
import java.util.Date
import java.util.Locale
import java.util.concurrent.ConcurrentHashMap

object ApiClient {
    private const val TAG = "ApiClient"
    // Using 10.0.2.2 for Android Emulator to host localhost
    private const val SERVER_URL = "http://10.0.2.2:5000/api/payments/verify"
    
    // Deduplication cache mapping the rawMessage to its last processed timestamp
    private val processedMessagesCache = ConcurrentHashMap<String, Long>()

    fun processPayment(context: Context, source: String, parsedTx: ParsedTransaction?) {
        val rawMsg = parsedTx?.rawMessage ?: return
        val now = System.currentTimeMillis()
        
        // Deduplicate: if seen within the last 60 seconds, ignore it
        val lastSeen = processedMessagesCache[rawMsg]
        if (lastSeen != null && (now - lastSeen) < 60000) {
            Log.d(TAG, "Duplicate message ignored to prevent hanging/duplicates.")
            return
        }
        
        processedMessagesCache[rawMsg] = now
        
        // Cleanup cache occasionally to prevent memory leaks
        if (processedMessagesCache.size > 100) {
            val threshold = now - 60000
            processedMessagesCache.entries.removeIf { it.value < threshold }
        }

        val prefs = context.getSharedPreferences("FlutterSharedPreferences", Context.MODE_PRIVATE)
        val merchantId = prefs.getString("flutter.merchant_id", "") ?: ""
        val secretKey = prefs.getString("flutter.secret_key", "") ?: ""

        val dateStr = SimpleDateFormat("yyyy-MM-dd HH:mm", Locale.ENGLISH).format(Date())

        val eventPayload = JSONObject().apply {
            put("sender", parsedTx.senderName)
            put("amount", parsedTx.amount)
            put("currency", parsedTx.currency)
            put("wallet", parsedTx.wallet.ifEmpty { source })
            put("date", dateStr)
            put("status", "checking")
            put("message", rawMsg)
        }

        if (merchantId.isEmpty() || secretKey.isEmpty()) {
            Log.e(TAG, "Merchant ID or Secret Key is missing. Cannot process payment.")
            eventPayload.put("status", "failed")
            broadcastToFlutter(eventPayload.toString())
            return
        }

        CoroutineScope(Dispatchers.IO).launch {
            try {
                val url = URL(SERVER_URL)
                val connection = url.openConnection() as HttpURLConnection
                connection.requestMethod = "POST"
                connection.setRequestProperty("Content-Type", "application/json; charset=UTF-8")
                connection.setRequestProperty("Accept", "application/json")
                connection.doOutput = true

                val payload = JSONObject().apply {
                    put("merchantId", merchantId)
                    put("secretKey", secretKey)
                    put("source", source)
                    put("message", parsedTx?.rawMessage ?: "")
                    put("timestamp", System.currentTimeMillis())
                    
                    val parsedObj = JSONObject().apply {
                        put("sender", parsedTx?.senderName ?: "Unknown")
                        put("amount", parsedTx?.amount ?: "0")
                        put("currency", parsedTx?.currency ?: "")
                        put("wallet", parsedTx?.wallet ?: source)
                    }
                    put("parsedTx", parsedObj)
                }

                val writer = OutputStreamWriter(connection.outputStream)
                writer.write(payload.toString())
                writer.flush()
                writer.close()

                val responseCode = connection.responseCode
                Log.d(TAG, "Server response code: $responseCode")

                if (responseCode == HttpURLConnection.HTTP_OK) {
                    val responseStr = connection.inputStream.bufferedReader().use { it.readText() }
                    val responseJson = JSONObject(responseStr)
                    
                    val txId = responseJson.optString("tx_id", "")
                    val txStatus = responseJson.optString("status", "checking")
                    
                    eventPayload.put("tx_id", txId)
                    eventPayload.put("status", txStatus)
                    broadcastToFlutter(eventPayload.toString())
                } else {
                    eventPayload.put("status", "failed")
                    broadcastToFlutter(eventPayload.toString())
                }

            } catch (e: Exception) {
                Log.e(TAG, "Error sending payment to server: ${e.message}")
                eventPayload.put("status", "failed")
                broadcastToFlutter(eventPayload.toString())
            }
        }
    }

    private fun broadcastToFlutter(jsonString: String) {
        Handler(Looper.getMainLooper()).post {
            MainActivity.eventSink?.success(jsonString)
        }
    }

    private fun showSuccessNotification(context: Context, body: String) {
        val manager = context.getSystemService(Context.NOTIFICATION_SERVICE) as NotificationManager
        val channelId = "AutoPaySuccessChannel"
        
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            val channel = NotificationChannel(channelId, "Payment Success", NotificationManager.IMPORTANCE_HIGH)
            manager.createNotificationChannel(channel)
        }

        val iconResId = context.resources.getIdentifier("ic_launcher", "mipmap", context.packageName)
        val notification = NotificationCompat.Builder(context, channelId)
            .setContentTitle("AutoPay Success")
            .setContentText(body)
            .setSmallIcon(if (iconResId != 0) iconResId else android.R.drawable.ic_dialog_info)
            .setAutoCancel(true)
            .build()

        manager.notify(System.currentTimeMillis().toInt(), notification)
    }
}

package com.example.autopayapp

import android.content.Context
import android.content.pm.PackageManager
import androidx.core.app.ActivityCompat
import androidx.core.content.ContextCompat
import android.content.Intent
import android.os.Build
import android.provider.Settings
import androidx.annotation.NonNull
import androidx.core.app.NotificationManagerCompat
import androidx.core.app.NotificationCompat
import android.app.NotificationChannel
import android.app.NotificationManager
import io.flutter.embedding.android.FlutterActivity
import io.flutter.embedding.engine.FlutterEngine
import io.flutter.plugin.common.EventChannel
import io.flutter.plugin.common.MethodChannel
import com.example.autopayapp.services.AutoPayBackgroundService
import java.net.HttpURLConnection
import java.net.URL
import java.io.InputStreamReader
import java.io.BufferedReader
import java.io.OutputStreamWriter
import android.net.Uri
import android.os.Handler
import android.os.Looper

class MainActivity: FlutterActivity() {
    private val METHOD_CHANNEL = "com.samayemen.autopay/service"
    private val EVENT_CHANNEL = "com.samayemen.autopay/transactions"

    companion object {
        var eventSink: EventChannel.EventSink? = null
    }

    override fun configureFlutterEngine(@NonNull flutterEngine: FlutterEngine) {
        super.configureFlutterEngine(flutterEngine)

        // Setup EventChannel for live transactions
        EventChannel(flutterEngine.dartExecutor.binaryMessenger, EVENT_CHANNEL).setStreamHandler(
            object : EventChannel.StreamHandler {
                override fun onListen(arguments: Any?, events: EventChannel.EventSink?) {
                    eventSink = events
                }

                override fun onCancel(arguments: Any?) {
                    eventSink = null
                }
            }
        )

        MethodChannel(flutterEngine.dartExecutor.binaryMessenger, METHOD_CHANNEL).setMethodCallHandler { call, result ->
            when (call.method) {
                "startService" -> {
                    startBackgroundService()
                    result.success("Service Started")
                }
                "stopService" -> {
                    stopBackgroundService()
                    result.success("Service Stopped")
                }
                "isServiceRunning" -> {
                    result.success(AutoPayBackgroundService.isRunning)
                }
                "isNotificationPermissionGranted" -> {
                    val packageNames = NotificationManagerCompat.getEnabledListenerPackages(this)
                    result.success(packageNames.contains(packageName))
                }
                "openNotificationSettings" -> {
                    val intent = Intent(Settings.ACTION_NOTIFICATION_LISTENER_SETTINGS)
                    startActivity(intent)
                    result.success(true)
                }
                "setPreference" -> {
                    val key = call.argument<String>("key")
                    val value = call.argument<String>("value")
                    if (key != null && value != null) {
                        val prefs = getSharedPreferences("app_prefs", Context.MODE_PRIVATE)
                        prefs.edit().putString(key, value).apply()
                        result.success(true)
                    } else {
                        result.error("INVALID_ARGS", "Key or value is null", null)
                    }
                }
                "getPreference" -> {
                    val key = call.argument<String>("key")
                    if (key != null) {
                        val prefs = getSharedPreferences("app_prefs", Context.MODE_PRIVATE)
                        result.success(prefs.getString(key, null))
                    } else {
                        result.error("INVALID_ARGS", "Key is null", null)
                    }
                }
                "clearPreferences" -> {
                    val prefs = getSharedPreferences("app_prefs", Context.MODE_PRIVATE)
                    prefs.edit().clear().apply()
                    result.success(true)
                }
                "checkSmsPermission" -> {
                    val granted = ContextCompat.checkSelfPermission(this@MainActivity, android.Manifest.permission.RECEIVE_SMS) == PackageManager.PERMISSION_GRANTED
                    result.success(granted)
                }
                "requestSmsPermission" -> {
                    ActivityCompat.requestPermissions(this@MainActivity, arrayOf(android.Manifest.permission.RECEIVE_SMS, android.Manifest.permission.READ_SMS), 101)
                    result.success(true)
                }
                "showNotification" -> {
                    val title = call.argument<String>("title") ?: "YemenPay"
                    val body = call.argument<String>("body") ?: ""
                    val channelId = "autopay_channel"
                    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
                        val channel = NotificationChannel(channelId, "AutoPay Notifications", NotificationManager.IMPORTANCE_HIGH)
                        val manager = getSystemService(NotificationManager::class.java)
                        manager?.createNotificationChannel(channel)
                    }
                    val notification = NotificationCompat.Builder(this@MainActivity, channelId)
                        .setContentTitle(title)
                        .setContentText(body)
                        .setSmallIcon(android.R.drawable.ic_dialog_info)
                        .build()
                    val manager = NotificationManagerCompat.from(this@MainActivity)
                    if (ActivityCompat.checkSelfPermission(this@MainActivity, android.Manifest.permission.POST_NOTIFICATIONS) == PackageManager.PERMISSION_GRANTED || Build.VERSION.SDK_INT < Build.VERSION_CODES.TIRAMISU) {
                        manager.notify(System.currentTimeMillis().toInt(), notification)
                    }
                    result.success(true)
                }
                "httpGet" -> {
                    val urlString = call.argument<String>("url")
                    if (urlString != null) {
                        Thread {
                            try {
                                val url = URL(urlString)
                                val connection = url.openConnection() as HttpURLConnection
                                connection.requestMethod = "GET"
                                connection.connectTimeout = 5000
                                connection.readTimeout = 5000
                                
                                val responseCode = connection.responseCode
                                if (responseCode == HttpURLConnection.HTTP_OK) {
                                    val reader = BufferedReader(InputStreamReader(connection.inputStream))
                                    val response = java.lang.StringBuilder()
                                    var line: String?
                                    while (reader.readLine().also { line = it } != null) {
                                        response.append(line)
                                    }
                                    reader.close()
                                    Handler(Looper.getMainLooper()).post {
                                        result.success(response.toString())
                                    }
                                } else {
                                    Handler(Looper.getMainLooper()).post {
                                        result.error("HTTP_ERROR", "Response code: $responseCode", null)
                                    }
                                }
                            } catch (e: Exception) {
                                Handler(Looper.getMainLooper()).post {
                                    result.error("HTTP_EXCEPTION", e.message, null)
                                }
                            }
                        }.start()
                    } else {
                        result.error("INVALID_ARGS", "URL is null", null)
                    }
                }
                "httpPost" -> {
                    val urlString = call.argument<String>("url")
                    val bodyString = call.argument<String>("body")
                    if (urlString != null && bodyString != null) {
                        Thread {
                            try {
                                val url = URL(urlString)
                                val connection = url.openConnection() as HttpURLConnection
                                connection.requestMethod = "POST"
                                connection.setRequestProperty("Content-Type", "application/json")
                                connection.doOutput = true
                                connection.connectTimeout = 5000
                                connection.readTimeout = 5000
                                
                                val writer = OutputStreamWriter(connection.outputStream)
                                writer.write(bodyString)
                                writer.flush()
                                writer.close()
                                
                                val responseCode = connection.responseCode
                                if (responseCode == HttpURLConnection.HTTP_OK) {
                                    val reader = BufferedReader(InputStreamReader(connection.inputStream))
                                    val response = java.lang.StringBuilder()
                                    var line: String?
                                    while (reader.readLine().also { line = it } != null) {
                                        response.append(line)
                                    }
                                    reader.close()
                                    Handler(Looper.getMainLooper()).post {
                                        result.success(response.toString())
                                    }
                                } else {
                                    Handler(Looper.getMainLooper()).post {
                                        result.error("HTTP_ERROR", "Response code: $responseCode", null)
                                    }
                                }
                            } catch (e: Exception) {
                                Handler(Looper.getMainLooper()).post {
                                    result.error("HTTP_EXCEPTION", e.message, null)
                                }
                            }
                        }.start()
                    } else {
                        result.error("INVALID_ARGS", "URL or body is null", null)
                    }
                }
                "getAppVersion" -> {
                    try {
                        val pInfo = packageManager.getPackageInfo(packageName, 0)
                        val version = pInfo.versionName
                        result.success(version)
                    } catch (e: PackageManager.NameNotFoundException) {
                        result.error("PACKAGE_ERROR", "Version not found", null)
                    }
                }
                "isPackageInstalled" -> {
                    val packageNameToCheck = call.argument<String>("packageName")
                    if (packageNameToCheck != null) {
                        try {
                            packageManager.getPackageInfo(packageNameToCheck, 0)
                            result.success(true)
                        } catch (e: PackageManager.NameNotFoundException) {
                            result.success(false)
                        }
                    } else {
                        result.error("INVALID_ARGS", "Package name is null", null)
                    }
                }
                "launchUrl" -> {
                    val urlString = call.argument<String>("url")
                    if (urlString != null) {
                        try {
                            val intent = Intent(Intent.ACTION_VIEW, Uri.parse(urlString))
                            intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
                            startActivity(intent)
                            result.success(true)
                        } catch (e: Exception) {
                            result.error("LAUNCH_ERROR", e.message, null)
                        }
                    } else {
                        result.error("INVALID_ARGS", "URL is null", null)
                    }
                }
                else -> {
                    result.notImplemented()
                }
            }
        }
    }

    private fun startBackgroundService() {
        val serviceIntent = Intent(this, AutoPayBackgroundService::class.java)
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            startForegroundService(serviceIntent)
        } else {
            startService(serviceIntent)
        }
    }

    private fun stopBackgroundService() {
        val serviceIntent = Intent(this, AutoPayBackgroundService::class.java)
        stopService(serviceIntent)
    }
}

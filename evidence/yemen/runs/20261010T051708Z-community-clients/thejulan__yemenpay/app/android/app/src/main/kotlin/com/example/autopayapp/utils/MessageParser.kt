package com.example.autopayapp.utils

import java.util.regex.Pattern

data class ParsedTransaction(
    val senderName: String,
    val amount: String,
    val currency: String,
    val wallet: String,
    val rawMessage: String
)

object MessageParser {
    // 1. KuraimiIMB Regex
    // Example: أودع/محمد الشيبباني لحسابك مبلغ 100 رصيدك 100.55 USD
    private val kuraimiPattern = Pattern.compile("أودع/(.+?)\\s*لحسابك مبلغ\\s*([\\d\\.]+).*?([A-Za-z]+)")

    // 2. Jaib Regex
    // Example: اضيف 5000ر.ي تحويل مشترك رص:5222.56ر.ي من فهمي الهتاري-771750560
    private val jaibPattern = Pattern.compile("اضيف\\s*([\\d\\.]+)\\s*(.+?)\\s*تحويل.*?من\\s*(.+?)-(\\d+)")

    fun parse(message: String, sourceWallet: String): ParsedTransaction? {
        val kuraimiMatcher = kuraimiPattern.matcher(message)
        if (kuraimiMatcher.find()) {
            return ParsedTransaction(
                senderName = kuraimiMatcher.group(1)?.trim() ?: "Unknown",
                amount = kuraimiMatcher.group(2)?.trim() ?: "0",
                currency = kuraimiMatcher.group(3)?.trim() ?: "USD",
                wallet = "kuraimi",
                rawMessage = message
            )
        }

        val jaibMatcher = jaibPattern.matcher(message)
        if (jaibMatcher.find()) {
            var rawCurrency = jaibMatcher.group(2)?.trim() ?: "ر.ي"
            if (rawCurrency == "ر.ي" || rawCurrency.contains("ر.ي")) { rawCurrency = "YER" }
            return ParsedTransaction(
                amount = jaibMatcher.group(1)?.trim() ?: "0",
                currency = rawCurrency,
                senderName = jaibMatcher.group(3)?.trim() ?: "Unknown",
                wallet = "jaib",
                rawMessage = message
            )
        }

        // Fallback for unparsed messages
        return null
    }
}

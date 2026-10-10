import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

class AppTheme {
  // Brand Colors from AutoPay Web SDK
  static const Color brand50 = Color(0xFFf0f9ff);
  static const Color brand100 = Color(0xFFe0f2fe);
  static const Color brand500 = Color(0xFF0ea5e9); // Primary Sky Blue
  static const Color brand600 = Color(0xFF0284c7);
  static const Color brand700 = Color(0xFF0369a1);
  static const Color brand900 = Color(0xFF0c4a6e); // Dark Slate

  static const Color background = Color(0xFFf8fafc);
  static const Color surface = Colors.white;
  static const Color textPrimary = Color(0xFF1e293b); // Slate 800
  static const Color textSecondary = Color(0xFF64748b); // Slate 500

  static ThemeData get lightTheme {
    return ThemeData(
      primaryColor: brand500,
      scaffoldBackgroundColor: background,
      colorScheme: const ColorScheme.light(
        primary: brand500,
        secondary: brand600,
        surface: surface,
      ),
      textTheme: GoogleFonts.notoKufiArabicTextTheme().apply(
        bodyColor: textPrimary,
        displayColor: textPrimary,
      ),
      elevatedButtonTheme: ElevatedButtonThemeData(
        style: ElevatedButton.styleFrom(
          backgroundColor: brand500,
          foregroundColor: Colors.white,
          textStyle: GoogleFonts.notoKufiArabic(fontWeight: FontWeight.bold),
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(12),
          ),
          padding: const EdgeInsets.symmetric(vertical: 16, horizontal: 24),
        ),
      ),
      appBarTheme: const AppBarTheme(
        backgroundColor: surface,
        foregroundColor: textPrimary,
        elevation: 0,
        centerTitle: true,
      ),
      inputDecorationTheme: InputDecorationTheme(
        filled: true,
        fillColor: surface,
        border: OutlineInputBorder(
          borderRadius: BorderRadius.circular(12),
          borderSide: const BorderSide(color: Color(0xFFcbd5e1)), // Slate 300
        ),
        enabledBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(12),
          borderSide: const BorderSide(color: Color(0xFFcbd5e1)),
        ),
        focusedBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(12),
          borderSide: const BorderSide(color: brand500, width: 2),
        ),
      ),
    );
  }
}

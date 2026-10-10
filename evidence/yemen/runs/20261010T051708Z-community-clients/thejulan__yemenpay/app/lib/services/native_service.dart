import 'package:flutter/services.dart';

class NativeService {
  static const MethodChannel _channel = MethodChannel('com.samayemen.autopay/service');

  // Preferences
  static Future<bool> setPreference(String key, String value) async {
    try {
      final result = await _channel.invokeMethod<bool>('setPreference', {'key': key, 'value': value});
      return result ?? false;
    } catch (e) {
      return false;
    }
  }

  static Future<String?> getPreference(String key) async {
    try {
      return await _channel.invokeMethod<String>('getPreference', {'key': key});
    } catch (e) {
      return null;
    }
  }

  static Future<bool> clearPreferences() async {
    try {
      final result = await _channel.invokeMethod<bool>('clearPreferences');
      return result ?? false;
    } catch (e) {
      return false;
    }
  }

  // Permissions
  static Future<bool> checkSmsPermission() async {
    try {
      final result = await _channel.invokeMethod<bool>('checkSmsPermission');
      return result ?? false;
    } catch (e) {
      return false;
    }
  }

  static Future<bool> requestSmsPermission() async {
    try {
      final result = await _channel.invokeMethod<bool>('requestSmsPermission');
      return result ?? false;
    } catch (e) {
      return false;
    }
  }

  // Notification
  static Future<void> showNotification({required String title, required String body}) async {
    try {
      await _channel.invokeMethod('showNotification', {'title': title, 'body': body});
    } catch (e) {
      // Ignore
    }
  }
}

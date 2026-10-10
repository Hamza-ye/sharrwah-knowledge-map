import 'package:flutter/services.dart';

class MethodChannelService {
  static const MethodChannel _channel = MethodChannel('com.samayemen.autopay/service');
  static const EventChannel _eventChannel = EventChannel('com.samayemen.autopay/transactions');

  static Future<String> startService() async {
    try {
      final String result = await _channel.invokeMethod('startService');
      return result;
    } on PlatformException catch (e) {
      return 'Failed to start service: ${e.message}';
    }
  }

  static Future<String> stopService() async {
    try {
      final String result = await _channel.invokeMethod('stopService');
      return result;
    } on PlatformException catch (e) {
      return 'Failed to stop service: ${e.message}';
    }
  }

  static Future<bool> isServiceRunning() async {
    try {
      final bool result = await _channel.invokeMethod('isServiceRunning');
      return result;
    } on PlatformException catch (_) {
      return false;
    }
  }

  static Future<bool> isNotificationPermissionGranted() async {
    try {
      final bool result = await _channel.invokeMethod('isNotificationPermissionGranted');
      return result;
    } on PlatformException catch (_) {
      return false;
    }
  }

  static Future<void> openNotificationSettings() async {
    try {
      await _channel.invokeMethod('openNotificationSettings');
    } on PlatformException catch (_) {
      // Ignored
    }
  }

  static Future<String?> httpGet(String url) async {
    try {
      final String? result = await _channel.invokeMethod('httpGet', {'url': url});
      return result;
    } on PlatformException catch (_) {
      return null;
    }
  }

  static Future<String?> httpPost(String url, String body) async {
    try {
      final String? result = await _channel.invokeMethod('httpPost', {'url': url, 'body': body});
      return result;
    } on PlatformException catch (_) {
      return null;
    }
  }

  static Future<String> getAppVersion() async {
    try {
      final String result = await _channel.invokeMethod('getAppVersion');
      return result;
    } on PlatformException catch (_) {
      return '1.0.0';
    }
  }

  static Future<bool> isPackageInstalled(String packageName) async {
    try {
      final bool result = await _channel.invokeMethod('isPackageInstalled', {'packageName': packageName});
      return result;
    } on PlatformException catch (_) {
      return false;
    }
  }

  static Future<bool> launchUrl(String url) async {
    try {
      final bool result = await _channel.invokeMethod('launchUrl', {'url': url});
      return result;
    } on PlatformException catch (_) {
      return false;
    }
  }

  static Stream<dynamic> get transactionsStream {
    return _eventChannel.receiveBroadcastStream();
  }
}

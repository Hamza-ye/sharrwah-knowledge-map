import 'package:flutter/material.dart';
import 'dart:convert';
import 'package:phosphor_flutter/phosphor_flutter.dart';
import '../services/native_service.dart';
import '../services/method_channel_service.dart';
import 'permissions_screen.dart';
import 'main_screen.dart';
import 'update_screen.dart';

class LoginScreen extends StatefulWidget {
  const LoginScreen({Key? key}) : super(key: key);

  @override
  State<LoginScreen> createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  final TextEditingController _merchantIdController = TextEditingController();
  final TextEditingController _secretKeyController = TextEditingController();
  final GlobalKey<FormState> _formKey = GlobalKey<FormState>();
  bool _isLoading = false;

  Future<void> _saveAndContinue() async {
    if (_formKey.currentState?.validate() ?? false) {
      setState(() => _isLoading = true);
      
      final merchantId = _merchantIdController.text.trim();
      final secretKey = _secretKeyController.text.trim();

      try {
        final responseBody = await MethodChannelService.httpPost(
          'http://10.0.2.2:5000/api/merchant/login',
          jsonEncode({
            'merchantId': merchantId,
            'secretKey': secretKey,
            'deviceInfo': 'Android Device (Flutter)',
          }),
        );

        if (responseBody != null) {
          final data = jsonDecode(responseBody);
          if (data['status'] == 'success') {
            await NativeService.setPreference('merchant_id', merchantId);
            await NativeService.setPreference('secret_key', secretKey);

            final hasSms = await NativeService.checkSmsPermission();
            final hasNotif = await MethodChannelService.isNotificationPermissionGranted();

            // Check API for version update
            bool needsUpdate = false;
            try {
              final versionResponseBody = await MethodChannelService.httpGet('http://10.0.2.2:5000/api/version/apk');
              if (versionResponseBody != null) {
                final vData = jsonDecode(versionResponseBody);
                if (vData['status'] == 'success') {
                  final serverVersion = vData['version'] as String;
                  final changelog = vData['changelog'] as String;
                  
                  final localVersion = await MethodChannelService.getAppVersion();
                  
                  if (serverVersion != localVersion) {
                    needsUpdate = true;
                    if (mounted) {
                      Navigator.pushReplacement(
                        context,
                        MaterialPageRoute(builder: (_) => UpdateScreen(version: serverVersion, changelog: changelog)),
                      );
                    }
                  }
                }
              }
            } catch (_) {
              // Ignore
            }

            if (!needsUpdate && mounted) {
              if (hasSms || hasNotif) {
                Navigator.pushReplacement(
                  context,
                  MaterialPageRoute(builder: (_) => const MainScreen()),
                );
              } else {
                Navigator.pushReplacement(
                  context,
                  MaterialPageRoute(builder: (_) => const PermissionsScreen()),
                );
              }
            }
          } else {
            _showError(data['error'] ?? 'Login failed');
          }
        } else {
          _showError('Invalid credentials or server error.');
        }
      } catch (e) {
        _showError('Network error. Check connection to server.');
      } finally {
        if (mounted) setState(() => _isLoading = false);
      }
    }
  }

  void _showError(String message) {
    if (!mounted) return;
    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
        title: Row(
          children: [
            const Directionality(textDirection: TextDirection.ltr, child: Icon(PhosphorIconsRegular.warningCircle, color: Colors.red)),
            const SizedBox(width: 8),
            const Text('خطأ في تسجيل الدخول', style: TextStyle(color: Colors.red, fontSize: 18, fontWeight: FontWeight.bold)),
          ],
        ),
        content: Text(message, style: const TextStyle(fontSize: 16)),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context),
            child: const Text('حسناً', style: TextStyle(fontWeight: FontWeight.bold)),
          ),
        ],
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        decoration: BoxDecoration(
          gradient: LinearGradient(
            begin: Alignment.topLeft,
            end: Alignment.bottomRight,
            colors: [
              Theme.of(context).primaryColor.withOpacity(0.05),
              Colors.white,
            ],
          ),
        ),
        child: SafeArea(
          child: Center(
            child: SingleChildScrollView(
              padding: const EdgeInsets.symmetric(horizontal: 32.0, vertical: 24.0),
              child: Form(
                key: _formKey,
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  crossAxisAlignment: CrossAxisAlignment.stretch,
                  children: [
                    Container(
                      padding: const EdgeInsets.all(24),
                      decoration: BoxDecoration(
                        color: Colors.white,
                        shape: BoxShape.circle,
                        boxShadow: [
                          BoxShadow(
                            color: Theme.of(context).primaryColor.withOpacity(0.15),
                            blurRadius: 30,
                            offset: const Offset(0, 10),
                          ),
                        ],
                      ),
                      child: Directionality(textDirection: TextDirection.ltr, child: Icon(
                        PhosphorIcons.storefront(PhosphorIconsStyle.fill),
                        size: 70,
                        color: Theme.of(context).primaryColor,
                      )),
                    ),
                    const SizedBox(height: 40),
                    Text(
                      'تسجيل الدخول',
                      style: Theme.of(context).textTheme.headlineMedium?.copyWith(
                            fontWeight: FontWeight.w900,
                            color: Theme.of(context).primaryColor,
                            letterSpacing: -0.5,
                          ),
                      textAlign: TextAlign.center,
                    ),
                    const SizedBox(height: 12),
                    Text(
                      'أدخل بيانات التاجر لربط بوابة الدفع الآلي بخوادم متجرك.',
                      style: Theme.of(context).textTheme.bodyLarge?.copyWith(
                            color: Colors.grey.shade600,
                            height: 1.5,
                          ),
                      textAlign: TextAlign.center,
                    ),
                    const SizedBox(height: 48),
                    Container(
                      decoration: BoxDecoration(
                        color: Colors.white,
                        borderRadius: BorderRadius.circular(20),
                        boxShadow: [
                          BoxShadow(
                            color: Colors.black.withOpacity(0.03),
                            blurRadius: 20,
                            offset: const Offset(0, 4),
                          ),
                        ],
                      ),
                      padding: const EdgeInsets.all(24),
                      child: Column(
                        children: [
                          TextFormField(
                            controller: _merchantIdController,
                            decoration: InputDecoration(
                              labelText: 'معرف التاجر (Merchant ID)',
                              prefixIcon: const Directionality(textDirection: TextDirection.ltr, child: Icon(PhosphorIconsRegular.identificationCard)),
                              filled: true,
                              fillColor: Colors.grey.shade50,
                              border: OutlineInputBorder(
                                borderRadius: BorderRadius.circular(16),
                                borderSide: BorderSide.none,
                              ),
                            ),
                            validator: (value) =>
                                value == null || value.isEmpty ? 'هذا الحقل مطلوب' : null,
                          ),
                          const SizedBox(height: 20),
                          TextFormField(
                            controller: _secretKeyController,
                            obscureText: true,
                            decoration: InputDecoration(
                              labelText: 'المفتاح السري (Secret Key)',
                              prefixIcon: const Directionality(textDirection: TextDirection.ltr, child: Icon(PhosphorIconsRegular.key)),
                              filled: true,
                              fillColor: Colors.grey.shade50,
                              border: OutlineInputBorder(
                                borderRadius: BorderRadius.circular(16),
                                borderSide: BorderSide.none,
                              ),
                            ),
                            validator: (value) =>
                                value == null || value.isEmpty ? 'هذا الحقل مطلوب' : null,
                          ),
                        ],
                      ),
                    ),
                    const SizedBox(height: 48),
                    ElevatedButton(
                      onPressed: _saveAndContinue,
                      style: ElevatedButton.styleFrom(
                        padding: const EdgeInsets.symmetric(vertical: 20),
                        shape: RoundedRectangleBorder(
                          borderRadius: BorderRadius.circular(16),
                        ),
                        elevation: 5,
                        shadowColor: Theme.of(context).primaryColor.withOpacity(0.4),
                      ),
                      child: _isLoading
                          ? const CircularProgressIndicator(color: Colors.white)
                          : const Text(
                              'متابعة وإعداد الصلاحيات',
                              style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
                            ),
                    ),
                  ],
                ),
              ),
            ),
          ),
        ),
      ),
    );
  }
}

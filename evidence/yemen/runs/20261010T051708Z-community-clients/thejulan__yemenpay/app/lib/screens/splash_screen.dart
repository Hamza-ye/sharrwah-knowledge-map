import 'package:flutter/material.dart';
import 'package:phosphor_flutter/phosphor_flutter.dart';
import '../services/native_service.dart';
import '../services/method_channel_service.dart';
import 'dart:convert';
import 'login_screen.dart';
import 'onboarding_screen.dart';
import 'main_screen.dart';
import 'update_screen.dart';

class SplashScreen extends StatefulWidget {
  const SplashScreen({Key? key}) : super(key: key);

  @override
  State<SplashScreen> createState() => _SplashScreenState();
}

class _SplashScreenState extends State<SplashScreen> {
  @override
  void initState() {
    super.initState();
    _routeToNextScreen();
  }

  Future<void> _routeToNextScreen() async {
    await Future.delayed(const Duration(seconds: 2));
    
    final hasSeenOnboardingStr = await NativeService.getPreference('has_seen_onboarding');
    final hasSeenOnboarding = hasSeenOnboardingStr == 'true';
    final merchantId = await NativeService.getPreference('merchant_id');

    // Check API for version update
    try {
      final responseBody = await MethodChannelService.httpGet('http://10.0.2.2:5000/api/version/apk');
      if (responseBody != null) {
        final data = jsonDecode(responseBody);
        if (data['status'] == 'success') {
          final serverVersion = data['version'] as String;
          final changelog = data['changelog'] as String;
          
          final localVersion = await MethodChannelService.getAppVersion();
          
          if (serverVersion != localVersion) {
             if (mounted) {
               Navigator.pushReplacement(
                 context,
                 MaterialPageRoute(builder: (_) => UpdateScreen(version: serverVersion, changelog: changelog)),
               );
             }
             return;
          }
        }
      }
    } catch (_) {
      // Ignore version check if server is unreachable
    }

    if (!mounted) return;

    if (!hasSeenOnboarding) {
      Navigator.pushReplacement(
        context,
        MaterialPageRoute(builder: (_) => const OnboardingScreen()),
      );
    } else if (merchantId != null && merchantId.isNotEmpty) {
      Navigator.pushReplacement(
        context,
        MaterialPageRoute(builder: (_) => const MainScreen()),
      );
    } else {
      Navigator.pushReplacement(
        context,
        MaterialPageRoute(builder: (_) => const LoginScreen()),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Theme.of(context).primaryColor,
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Directionality(textDirection: TextDirection.ltr, child: Icon(
              PhosphorIcons.wallet(PhosphorIconsStyle.fill),
              size: 100,
              color: Colors.white,
            )),
            const SizedBox(height: 16),
            const Text(
              'YemenPay AutoPay',
              style: TextStyle(
                color: Colors.white,
                fontSize: 28,
                fontWeight: FontWeight.bold,
              ),
            ),
            const SizedBox(height: 8),
            Text(
              'بوابة الدفع الآلي للمحافظ الإلكترونية',
              style: TextStyle(
                color: Colors.white.withOpacity(0.8),
                fontSize: 16,
              ),
            ),
          ],
        ),
      ),
    );
  }
}

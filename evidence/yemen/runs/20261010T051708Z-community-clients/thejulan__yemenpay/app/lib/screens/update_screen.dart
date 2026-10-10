import 'package:flutter/material.dart';
import 'package:phosphor_flutter/phosphor_flutter.dart';
import '../services/method_channel_service.dart';

class UpdateScreen extends StatelessWidget {
  final String version;
  final String changelog;

  const UpdateScreen({
    Key? key,
    required this.version,
    required this.changelog,
  }) : super(key: key);

  Future<void> _launchUrl(String urlString) async {
    await MethodChannelService.launchUrl(urlString);
  }

  @override
  Widget build(BuildContext context) {
    return PopScope(
      canPop: false, // Prevent back navigation
      child: Scaffold(
        backgroundColor: Colors.white,
        body: SafeArea(
          child: Padding(
            padding:
                const EdgeInsets.symmetric(horizontal: 32.0, vertical: 24.0),
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: [
                Container(
                  padding: const EdgeInsets.all(24),
                  decoration: BoxDecoration(
                    color: Colors.blue.shade50,
                    shape: BoxShape.circle,
                  ),
                  child: const Directionality(
                      textDirection: TextDirection.ltr,
                      child: Icon(
                        PhosphorIconsRegular.downloadSimple,
                        size: 80,
                        color: Colors.blue,
                      )),
                ),
                const SizedBox(height: 32),
                const Text(
                  'تحديث جديد متاح!',
                  style: TextStyle(
                    fontSize: 24,
                    fontWeight: FontWeight.bold,
                    color: Colors.black87,
                  ),
                  textAlign: TextAlign.center,
                ),
                const SizedBox(height: 8),
                Text(
                  'الإصدار $version متوفر الآن',
                  style: TextStyle(
                    fontSize: 16,
                    color: Colors.grey.shade600,
                  ),
                  textAlign: TextAlign.center,
                ),
                const SizedBox(height: 32),
                Container(
                  padding: const EdgeInsets.all(16),
                  decoration: BoxDecoration(
                    color: Colors.grey.shade50,
                    border: Border.all(color: Colors.grey.shade200),
                    borderRadius: BorderRadius.circular(16),
                  ),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      const Text(
                        'ما الجديد:',
                        style: TextStyle(
                          fontSize: 16,
                          fontWeight: FontWeight.bold,
                          color: Colors.black87,
                        ),
                      ),
                      const SizedBox(height: 12),
                      Text(
                        changelog,
                        style: TextStyle(
                          fontSize: 14,
                          color: Colors.grey.shade700,
                          height: 1.5,
                        ),
                      ),
                    ],
                  ),
                ),
                const Spacer(),
                ElevatedButton.icon(
                  onPressed: () =>
                      _launchUrl('https://example.com/download'), // Placeholder
                  icon: const Directionality(
                      textDirection: TextDirection.ltr,
                      child: Icon(PhosphorIconsRegular.downloadSimple)),
                  label: const Text(
                    'تحديث الآن',
                    style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
                  ),
                  style: ElevatedButton.styleFrom(
                    padding: const EdgeInsets.symmetric(vertical: 16),
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(16),
                    ),
                  ),
                ),
                const SizedBox(height: 16),
                OutlinedButton.icon(
                  onPressed: () => _launchUrl('https://github.com/'),
                  icon: const Directionality(
                    textDirection: TextDirection.ltr,
                    child: Icon(PhosphorIconsRegular.githubLogo,
                        color: Colors.white), // Added white color
                  ),
                  label: const Text(
                    'عرض الكود المصدري',
                    style: TextStyle(
                      fontSize: 16,
                      fontWeight: FontWeight.bold,
                      color: Colors.white, // Added white color
                    ),
                  ),
                  style: OutlinedButton.styleFrom(
                    backgroundColor:
                        Colors.black, // Sets the background to black
                    padding: const EdgeInsets.symmetric(
                        vertical: 16,
                        horizontal:
                            24), // Added horizontal padding for better spacing
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(16),
                    ),
                    side: const BorderSide(
                        color: Colors
                            .black), // Ensures border matches the background
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}

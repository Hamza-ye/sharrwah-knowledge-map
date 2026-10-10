import 'package:flutter/material.dart';
import '../services/native_service.dart';
import 'package:phosphor_flutter/phosphor_flutter.dart';
import '../services/method_channel_service.dart';
import 'main_screen.dart';
import 'dart:async';

class PermissionsScreen extends StatefulWidget {
  const PermissionsScreen({Key? key}) : super(key: key);

  @override
  State<PermissionsScreen> createState() => _PermissionsScreenState();
}

class _PermissionsScreenState extends State<PermissionsScreen> with WidgetsBindingObserver {
  bool _smsGranted = false;
  bool _notificationGranted = false;

  @override
  void initState() {
    super.initState();
    WidgetsBinding.instance.addObserver(this);
    _checkPermissions();
  }

  @override
  void dispose() {
    WidgetsBinding.instance.removeObserver(this);
    super.dispose();
  }

  @override
  void didChangeAppLifecycleState(AppLifecycleState state) {
    if (state == AppLifecycleState.resumed) {
      _checkPermissions();
    }
  }

  Future<void> _checkPermissions() async {
    final smsGranted = await NativeService.checkSmsPermission();
    final notifStatus = await MethodChannelService.isNotificationPermissionGranted();

    setState(() {
      _smsGranted = smsGranted;
      _notificationGranted = notifStatus;
    });
  }

  Future<void> _requestSmsPermission() async {
    final granted = await NativeService.requestSmsPermission();
    setState(() {
      _smsGranted = granted;
    });
  }

  Future<void> _requestNotificationPermission() async {
    await MethodChannelService.openNotificationSettings();
  }

  void _finish() {
    if (_smsGranted || _notificationGranted) {
      Navigator.pushReplacement(
        context,
        MaterialPageRoute(builder: (_) => const MainScreen()),
      );
    } else {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(
          content: Text('الرجاء منح صلاحية واحدة على الأقل للاستمرار'),
          backgroundColor: Colors.red,
        ),
      );
    }
  }

  Widget _buildPermissionCard({
    required String title,
    required String description,
    required IconData icon,
    required bool isGranted,
    required VoidCallback onTap,
  }) {
    return Container(
      margin: const EdgeInsets.only(bottom: 16),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(16),
        border: Border.all(
          color: isGranted ? Colors.green.shade200 : Colors.grey.shade200,
          width: isGranted ? 2 : 1,
        ),
        boxShadow: [
          BoxShadow(
            color: Colors.black.withOpacity(0.02),
            blurRadius: 8,
            offset: const Offset(0, 4),
          ),
        ],
      ),
      child: Material(
        color: Colors.transparent,
        child: InkWell(
          onTap: isGranted ? null : onTap,
          borderRadius: BorderRadius.circular(16),
          child: Padding(
            padding: const EdgeInsets.all(20),
            child: Row(
              children: [
                Container(
                  padding: const EdgeInsets.all(12),
                  decoration: BoxDecoration(
                    color: isGranted ? Colors.green.withOpacity(0.1) : Theme.of(context).primaryColor.withOpacity(0.1),
                    shape: BoxShape.circle,
                  ),
                  child: Directionality(
                    textDirection: TextDirection.ltr,
                    child: Directionality(textDirection: TextDirection.ltr, child: Icon(
                      isGranted ? PhosphorIconsRegular.checkCircle : icon,
                      color: isGranted ? Colors.green : Theme.of(context).primaryColor,
                      size: 28,
                    )),
                  ),
                ),
                const SizedBox(width: 16),
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        title,
                        style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 16),
                      ),
                      const SizedBox(height: 4),
                      Text(
                        description,
                        style: TextStyle(color: Colors.grey.shade600, fontSize: 13),
                      ),
                    ],
                  ),
                ),
                if (!isGranted) ...[
                  const SizedBox(width: 12),
                  const Directionality(
                    textDirection: TextDirection.ltr,
                    child: Directionality(textDirection: TextDirection.ltr, child: Icon(PhosphorIconsRegular.caretLeft, color: Colors.grey)),
                  ),
                ]
              ],
            ),
          ),
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    final allGranted = _smsGranted || _notificationGranted;

    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        title: const Text('إعداد الصلاحيات', style: TextStyle(fontWeight: FontWeight.bold)),
        backgroundColor: Colors.white,
        elevation: 0,
      ),
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.symmetric(horizontal: 24.0, vertical: 16.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              Container(
                padding: const EdgeInsets.all(20),
                decoration: BoxDecoration(
                  color: Theme.of(context).primaryColor.withOpacity(0.05),
                  borderRadius: BorderRadius.circular(16),
                  border: Border.all(color: Theme.of(context).primaryColor.withOpacity(0.2)),
                ),
                child: Row(
                  children: [
                    Directionality(textDirection: TextDirection.ltr, child: Icon(PhosphorIconsRegular.info, color: Theme.of(context).primaryColor, size: 28)),
                    const SizedBox(width: 16),
                    Expanded(
                      child: Text(
                        'لضمان التقاط الحوالات بشكل آلي وسريع، يرجى تفعيل الصلاحيات التالية. لا يمكن للتطبيق العمل بدونها.',
                        style: TextStyle(color: Colors.grey.shade800, height: 1.5, fontSize: 13),
                      ),
                    ),
                  ],
                ),
              ),
              const SizedBox(height: 32),
              _buildPermissionItem(
                icon: PhosphorIconsRegular.chatCircleText,
                title: 'قراءة الرسائل (SMS)',
                description: 'لالتقاط رسائل الحوالات الواردة من المحافظ.',
                isGranted: _smsGranted,
                onTap: _smsGranted ? null : _requestSmsPermission,
              ),
              const SizedBox(height: 20),
              _buildPermissionItem(
                icon: PhosphorIconsRegular.bellRinging,
                title: 'قراءة الإشعارات',
                description: 'لالتقاط إشعارات تطبيقات البنوك عند استلام مبالغ.',
                isGranted: _notificationGranted,
                onTap: _notificationGranted ? null : _requestNotificationPermission,
              ),
              const Spacer(),
              ElevatedButton(
                onPressed: allGranted ? _finish : null,
                style: ElevatedButton.styleFrom(
                  backgroundColor: allGranted ? Theme.of(context).primaryColor : Colors.grey.shade300,
                  foregroundColor: allGranted ? Colors.white : Colors.grey.shade500,
                  padding: const EdgeInsets.symmetric(vertical: 20),
                  shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
                  elevation: allGranted ? 5 : 0,
                ),
                child: const Text(
                  'بدء الاستخدام',
                  style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildPermissionItem({
    required IconData icon,
    required String title,
    required String description,
    required bool isGranted,
    required VoidCallback? onTap,
  }) {
    return AnimatedContainer(
      duration: const Duration(milliseconds: 300),
      padding: const EdgeInsets.all(20),
      decoration: BoxDecoration(
        color: isGranted ? Colors.green.withOpacity(0.05) : Colors.white,
        borderRadius: BorderRadius.circular(20),
        border: Border.all(
          color: isGranted ? Colors.green : Colors.grey.shade200,
          width: 2,
        ),
        boxShadow: [
          if (!isGranted)
            BoxShadow(color: Colors.black.withOpacity(0.02), blurRadius: 10, offset: const Offset(0, 4)),
        ],
      ),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(
              color: isGranted ? Colors.green : Theme.of(context).primaryColor.withOpacity(0.1),
              shape: BoxShape.circle,
            ),
            child: Directionality(
              textDirection: TextDirection.ltr,
              child: Directionality(textDirection: TextDirection.ltr, child: Icon(
                isGranted ? PhosphorIconsRegular.check : icon,
                color: isGranted ? Colors.white : Theme.of(context).primaryColor,
                size: 24,
              )),
            ),
          ),
          const SizedBox(width: 16),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(title, style: const TextStyle(fontWeight: FontWeight.w900, fontSize: 16)),
                const SizedBox(height: 6),
                Text(description, style: TextStyle(color: Colors.grey.shade600, fontSize: 13, height: 1.4)),
                const SizedBox(height: 16),
                if (!isGranted)
                  InkWell(
                    onTap: onTap,
                    borderRadius: BorderRadius.circular(8),
                    child: Container(
                      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
                      decoration: BoxDecoration(
                        color: Theme.of(context).primaryColor,
                        borderRadius: BorderRadius.circular(8),
                      ),
                      child: const Text('تفعيل الصلاحية', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold, fontSize: 12)),
                    ),
                  )
                else
                  const Row(
                    children: [
                      Directionality(textDirection: TextDirection.ltr, child: Directionality(textDirection: TextDirection.ltr, child: Icon(PhosphorIconsRegular.shieldCheck, color: Colors.green, size: 16))),
                      SizedBox(width: 6),
                      Text('تم التفعيل', style: TextStyle(color: Colors.green, fontWeight: FontWeight.bold, fontSize: 13)),
                    ],
                  )
              ],
            ),
          ),
        ],
      ),
    );
  }
}

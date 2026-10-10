import 'package:flutter/material.dart';
import 'package:phosphor_flutter/phosphor_flutter.dart';
import 'dart:async';
import '../services/method_channel_service.dart';

class DashboardTab extends StatefulWidget {
  final List<Map<String, dynamic>> transactions;
  final bool isServiceRunning;
  final String serverStatus;
  final Color serverStatusColor;
  final VoidCallback onToggleService;

  const DashboardTab({
    Key? key,
    required this.transactions,
    required this.isServiceRunning,
    required this.serverStatus,
    required this.serverStatusColor,
    required this.onToggleService,
  }) : super(key: key);

  @override
  State<DashboardTab> createState() => _DashboardTabState();
}

class _DashboardTabState extends State<DashboardTab> {
  Timer? _countdownTimer;
  final List<Map<String, String>> _wallets = [
    {
      'name': 'جيب',
      'package': 'com.ahd.jaib',
      'image': 'assets/images/wallets/jaib.png'
    },
    {
      'name': 'جوالي',
      'package': 'com.ama.wecashmobileapp',
      'image': 'assets/images/wallets/jawaly.png'
    },
    {
      'name': 'الكريمي',
      'package': 'com.KuraimiBank',
      'image': 'assets/images/wallets/kuraimi.png'
    },
    {
      'name': 'ون كاش',
      'package': 'com.one.onecustomer',
      'image': 'assets/images/wallets/one-cash.png'
    },
    {
      'name': 'يمن والت',
      'package': 'com.s2m.yemenpost.customer.android',
      'image': 'assets/images/wallets/yemen-wallet.png'
    },
    {
      'name': 'موبايل موني',
      'package': 'cac.mobilemoney.app',
      'image': 'assets/images/wallets/mobile-money.png'
    },
  ];
  Map<String, bool> _installedWallets = {};

  @override
  void initState() {
    super.initState();
    _checkInstalledWallets();
    // Update UI every second for the countdown
    _countdownTimer = Timer.periodic(const Duration(seconds: 1), (timer) {
      if (mounted) setState(() {});
    });
  }

  @override
  void dispose() {
    _countdownTimer?.cancel();
    super.dispose();
  }

  Future<void> _checkInstalledWallets() async {
    Map<String, bool> statuses = {};
    for (var wallet in _wallets) {
      statuses[wallet['package']!] =
          await MethodChannelService.isPackageInstalled(wallet['package']!);
    }
    if (mounted) {
      setState(() {
        _installedWallets = statuses;
      });
    }
  }

  Widget _buildStatusIndicator() {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
      decoration: BoxDecoration(
        color: widget.serverStatusColor.withOpacity(0.1),
        borderRadius: BorderRadius.circular(20),
        border: Border.all(color: widget.serverStatusColor.withOpacity(0.5)),
      ),
      child: Row(
        mainAxisSize: MainAxisSize.min,
        children: [
          Container(
            width: 8,
            height: 8,
            decoration: BoxDecoration(
              color: widget.serverStatusColor,
              shape: BoxShape.circle,
            ),
          ),
          const SizedBox(width: 8),
          Text(
            widget.serverStatus,
            style: TextStyle(
              color: widget.serverStatusColor,
              fontWeight: FontWeight.bold,
              fontSize: 12,
            ),
          ),
        ],
      ),
    );
  }

  Map<String, String> _getWalletDetails(String? walletName) {
    if (walletName == null) return {'name': 'غير معروف', 'image': ''};
    final lower = walletName.toLowerCase();
    if (lower.contains('jaib'))
      return {'name': 'جيب', 'image': 'assets/images/wallets/jaib.png'};
    if (lower.contains('jawaly'))
      return {'name': 'جوالي', 'image': 'assets/images/wallets/jawaly.png'};
    if (lower.contains('kuraimi'))
      return {'name': 'الكريمي', 'image': 'assets/images/wallets/kuraimi.png'};
    if (lower.contains('one') && lower.contains('cash'))
      return {'name': 'ون كاش', 'image': 'assets/images/wallets/one-cash.png'};
    if (lower.contains('yemen') && lower.contains('wallet'))
      return {
        'name': 'يمن والت',
        'image': 'assets/images/wallets/yemen-wallet.png'
      };
    if (lower.contains('mobile') && lower.contains('money'))
      return {
        'name': 'موبايل موني',
        'image': 'assets/images/wallets/mobile-money.png'
      };
    return {'name': walletName, 'image': ''};
  }

  Widget _buildTransactionItem(Map<String, dynamic> tx) {
    IconData statusIcon;
    Color statusColor;
    Widget statusWidget;
    final walletDetails = _getWalletDetails(tx['wallet']);

    if (tx['status'] == 'checking') {
      statusColor = Colors.orange;

      // Calculate remaining time
      final timestamp =
          tx['timestamp'] ?? DateTime.now().millisecondsSinceEpoch;
      final elapsed = DateTime.now().millisecondsSinceEpoch - timestamp;
      final remainingSecs = 60 - (elapsed / 1000).floor();

      if (remainingSecs > 0) {
        statusWidget = Row(
          mainAxisSize: MainAxisSize.min,
          children: [
            const SizedBox(
              width: 14,
              height: 14,
              child: CircularProgressIndicator(
                  strokeWidth: 2, color: Colors.orange),
            ),
            const SizedBox(width: 6),
            Text('$remainingSecs ثانية',
                style: const TextStyle(
                    color: Colors.orange,
                    fontSize: 12,
                    fontWeight: FontWeight.bold)),
          ],
        );
      } else {
        statusWidget = const Directionality(
            textDirection: TextDirection.ltr,
            child: Icon(PhosphorIconsRegular.clock,
                color: Colors.orange, size: 20));
      }
    } else if (tx['status'] == 'automated' || tx['status'] == 'success') {
      statusIcon = PhosphorIconsRegular.checkCircle;
      statusColor = Colors.green;
      statusWidget = Directionality(
          textDirection: TextDirection.ltr,
          child: Icon(statusIcon, color: statusColor, size: 24));
    } else if (tx['status'] == 'failed') {
      statusIcon = PhosphorIconsRegular.xCircle;
      statusColor = Colors.red;
      statusWidget = Directionality(
          textDirection: TextDirection.ltr,
          child: Icon(statusIcon, color: statusColor, size: 24));
    } else {
      statusIcon = PhosphorIconsRegular.info;
      statusColor = Colors.blue;
      statusWidget = Directionality(
          textDirection: TextDirection.ltr,
          child: Icon(statusIcon, color: statusColor, size: 24));
    }

    return Container(
      margin: const EdgeInsets.only(bottom: 12),
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(16),
        boxShadow: [
          BoxShadow(
            color: Colors.black.withOpacity(0.02),
            blurRadius: 10,
            offset: const Offset(0, 4),
          ),
        ],
        border: Border.all(color: Colors.grey.shade100),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Row(
                children: [
                  Container(
                    width: 34,
                    height: 34,
                    decoration: BoxDecoration(
                      color: walletDetails['image']!.isNotEmpty
                          ? Colors.white
                          : Theme.of(context).primaryColor.withOpacity(0.1),
                      shape: BoxShape.circle,
                      border: walletDetails['image']!.isNotEmpty
                          ? Border.all(color: Colors.grey.shade200)
                          : null,
                    ),
                    padding: EdgeInsets.all(
                        walletDetails['image']!.isNotEmpty ? 2 : 8),
                    child: walletDetails['image']!.isNotEmpty
                        ? ClipOval(
                            child: Image.asset(walletDetails['image']!,
                                fit: BoxFit.contain),
                          )
                        : Directionality(
                            textDirection: TextDirection.ltr,
                            child: Icon(PhosphorIconsRegular.wallet,
                                color: Theme.of(context).primaryColor,
                                size: 18)),
                  ),
                  const SizedBox(width: 12),
                  Text(
                    tx['sender'] ?? 'Unknown',
                    style: const TextStyle(
                        fontWeight: FontWeight.w900, fontSize: 16),
                  ),
                ],
              ),
              Text(
                '${tx['amount']} ${tx['currency']}',
                style: TextStyle(
                    fontWeight: FontWeight.w900,
                    fontSize: 16,
                    color: Theme.of(context).primaryColor),
              ),
            ],
          ),
          const Padding(
            padding: EdgeInsets.symmetric(vertical: 8.0),
            child: Divider(),
          ),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    walletDetails['name']!,
                    style: TextStyle(color: Colors.grey.shade600, fontSize: 12),
                  ),
                  const SizedBox(height: 4),
                  Text(
                    tx['date'] ?? '',
                    style: TextStyle(color: Colors.grey.shade400, fontSize: 11),
                  ),
                ],
              ),
              Container(
                padding:
                    const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
                decoration: BoxDecoration(
                  color: statusColor.withOpacity(0.1),
                  borderRadius: BorderRadius.circular(12),
                ),
                child: Row(
                  children: [
                    statusWidget,
                    const SizedBox(width: 6),
                    Text(
                      tx['status'] == 'checking'
                          ? 'قيد المعالجة'
                          : (tx['status'] == 'automated'
                              ? 'مؤكد آلياً'
                              : (tx['status'] == 'failed'
                                  ? 'فشل التأكيد'
                                  : 'حوالة عادية')),
                      style: TextStyle(
                          color: statusColor,
                          fontWeight: FontWeight.bold,
                          fontSize: 12),
                    ),
                  ],
                ),
              )
            ],
          ),
        ],
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    int totalAutomated =
        widget.transactions.where((t) => t['status'] == 'automated').length;
    int totalNormal = widget.transactions
        .where((t) => t['status'] == 'regular' || t['status'] == 'checking')
        .length;

    // Top 5 only
    final recentTransactions = widget.transactions.take(5).toList();

    return SafeArea(
      child: Padding(
        padding: const EdgeInsets.symmetric(horizontal: 24.0, vertical: 16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            // Server Status Banner - Highly Visible
            Container(
              padding: const EdgeInsets.symmetric(vertical: 16, horizontal: 24),
              decoration: BoxDecoration(
                gradient: LinearGradient(
                  colors: widget.serverStatus == 'متصل نشط'
                      ? [Colors.green.shade600, Colors.green.shade400]
                      : (widget.serverStatus == 'غير متصل'
                          ? [Colors.red.shade600, Colors.red.shade400]
                          : [Colors.orange.shade600, Colors.orange.shade400]),
                  begin: Alignment.topLeft,
                  end: Alignment.bottomRight,
                ),
                borderRadius: BorderRadius.circular(16),
                boxShadow: [
                  BoxShadow(
                    color: (widget.serverStatus == 'متصل نشط'
                            ? Colors.green
                            : (widget.serverStatus == 'غير متصل'
                                ? Colors.red
                                : Colors.orange))
                        .withOpacity(0.4),
                    blurRadius: 12,
                    offset: const Offset(0, 4),
                  ),
                ],
              ),
              child: Row(
                children: [
                  Container(
                    padding: const EdgeInsets.all(12),
                    decoration: BoxDecoration(
                      color: Colors.white.withOpacity(0.2),
                      shape: BoxShape.circle,
                    ),
                    child: Directionality(
                        textDirection: TextDirection.ltr,
                        child: Icon(
                          widget.serverStatus == 'متصل نشط'
                              ? PhosphorIconsRegular.checkCircle
                              : (widget.serverStatus == 'غير متصل'
                                  ? PhosphorIconsRegular.warningCircle
                                  : PhosphorIconsRegular.spinner),
                          color: Colors.white,
                          size: 28,
                        )),
                  ),
                  const SizedBox(width: 16),
                  Expanded(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        const Text(
                          'حالة السيرفر',
                          style: TextStyle(
                              color: Colors.white70,
                              fontSize: 13,
                              fontWeight: FontWeight.bold),
                        ),
                        const SizedBox(height: 4),
                        Text(
                          widget.serverStatus,
                          style: const TextStyle(
                              color: Colors.white,
                              fontSize: 20,
                              fontWeight: FontWeight.w900),
                        ),
                      ],
                    ),
                  ),
                ],
              ),
            ),
            const SizedBox(height: 24),

            // Statistics Cards
            Row(
              children: [
                Expanded(
                  child: Container(
                    padding: const EdgeInsets.all(16),
                    decoration: BoxDecoration(
                      color: Colors.green.withOpacity(0.1),
                      borderRadius: BorderRadius.circular(16),
                      border: Border.all(color: Colors.green.withOpacity(0.3)),
                    ),
                    child: Column(
                      children: [
                        const Directionality(
                            textDirection: TextDirection.ltr,
                            child: Icon(PhosphorIconsRegular.checkCircle,
                                color: Colors.green, size: 28)),
                        const SizedBox(height: 8),
                        const Text('مؤكدة آلياً',
                            style: TextStyle(
                                color: Colors.green,
                                fontWeight: FontWeight.bold)),
                        Text(totalAutomated.toString(),
                            style: const TextStyle(
                                fontSize: 24,
                                fontWeight: FontWeight.w900,
                                color: Colors.green)),
                      ],
                    ),
                  ),
                ),
                const SizedBox(width: 16),
                Expanded(
                  child: Container(
                    padding: const EdgeInsets.all(16),
                    decoration: BoxDecoration(
                      color: Colors.blue.withOpacity(0.1),
                      borderRadius: BorderRadius.circular(16),
                      border: Border.all(color: Colors.blue.withOpacity(0.3)),
                    ),
                    child: Column(
                      children: [
                        const Directionality(
                            textDirection: TextDirection.ltr,
                            child: Icon(PhosphorIconsRegular.info,
                                color: Colors.blue, size: 28)),
                        const SizedBox(height: 8),
                        const Text('حوالات عادية',
                            style: TextStyle(
                                color: Colors.blue,
                                fontWeight: FontWeight.bold)),
                        Text(totalNormal.toString(),
                            style: const TextStyle(
                                fontSize: 24,
                                fontWeight: FontWeight.w900,
                                color: Colors.blue)),
                      ],
                    ),
                  ),
                ),
              ],
            ),

            const SizedBox(height: 32),
            // Wallets list
            const Row(
              children: [
                Directionality(
                    textDirection: TextDirection.ltr,
                    child:
                        Icon(PhosphorIconsRegular.wallet, color: Colors.grey)),
                SizedBox(width: 8),
                Text(
                  'المحافظ المدعومة على جهازك',
                  style: TextStyle(fontWeight: FontWeight.w900, fontSize: 18),
                ),
              ],
            ),
            const SizedBox(height: 16),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: _wallets.map((wallet) {
                final isInstalled =
                    _installedWallets[wallet['package']] ?? false;
                return Stack(
                  children: [
                    Container(
                      width: 48,
                      height: 48,
                      decoration: BoxDecoration(
                        color: Colors.white,
                        shape: BoxShape.circle,
                        border: Border.all(
                          color: isInstalled ? Colors.green : Colors.red,
                          width: 3, // wider border
                        ),
                        boxShadow: [
                          if (isInstalled)
                            BoxShadow(
                              color: Colors.green.withOpacity(0.2),
                              blurRadius: 8,
                              offset: const Offset(0, 4),
                            ),
                        ],
                      ),
                      padding: const EdgeInsets.all(6),
                      child: ClipOval(
                        child:
                            Image.asset(wallet['image']!, fit: BoxFit.contain),
                      ),
                    ),
                    Positioned(
                      bottom: 0,
                      right: 0,
                      child: Container(
                        padding: const EdgeInsets.all(2),
                        decoration: BoxDecoration(
                          color: isInstalled ? Colors.green : Colors.red,
                          shape: BoxShape.circle,
                        ),
                        child: Icon(isInstalled ? Icons.check : Icons.close,
                            color: Colors.white, size: 10),
                      ),
                    ),
                  ],
                );
              }).toList(),
            ),

            const SizedBox(height: 32),
            const Row(
              children: [
                Directionality(
                    textDirection: TextDirection.ltr,
                    child: Icon(PhosphorIconsRegular.listDashes,
                        color: Colors.grey)),
                SizedBox(width: 8),
                Text(
                  'آخر 5 عمليات ملتقطة',
                  style: TextStyle(fontWeight: FontWeight.w900, fontSize: 18),
                ),
              ],
            ),
            const SizedBox(height: 16),
            Expanded(
              child: recentTransactions.isEmpty
                  ? Center(
                      child: SingleChildScrollView(
                        child: Column(
                          mainAxisAlignment: MainAxisAlignment.center,
                          mainAxisSize: MainAxisSize.min,
                          children: [
                            Directionality(
                                textDirection: TextDirection.ltr,
                                child: Icon(PhosphorIconsRegular.empty,
                                    size: 60, color: Colors.grey.shade300)),
                            const SizedBox(height: 16),
                            Text(
                              'لا توجد عمليات مسجلة بعد',
                              style: TextStyle(color: Colors.grey.shade500),
                            ),
                          ],
                        ),
                      ),
                    )
                  : ListView.builder(
                      itemCount: recentTransactions.length,
                      itemBuilder: (context, index) {
                        return _buildTransactionItem(recentTransactions[index]);
                      },
                    ),
            ),
          ],
        ),
      ),
    );
  }
}

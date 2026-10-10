import 'package:flutter/material.dart';
import 'package:phosphor_flutter/phosphor_flutter.dart';
import 'dart:convert';
import 'dart:async';
import '../services/method_channel_service.dart';

import 'dashboard_tab.dart';
import 'transactions_tab.dart';
import 'settings_tab.dart';

class MainScreen extends StatefulWidget {
  const MainScreen({Key? key}) : super(key: key);

  @override
  State<MainScreen> createState() => _MainScreenState();
}

class _MainScreenState extends State<MainScreen> {
  int _currentIndex = 0;
  List<Map<String, dynamic>> _transactions = [];
  StreamSubscription? _txSubscription;
  Timer? _pollingTimer;

  bool _isServiceRunning = false;
  String _serverStatus = 'جاري التحقق...';
  Color _serverStatusColor = Colors.orange;

  @override
  void initState() {
    super.initState();
    _checkServiceStatus();
    _pingServer();
    _listenToTransactions();
    
    // Poll the server every 5 seconds for any 'checking' transactions
    _pollingTimer = Timer.periodic(const Duration(seconds: 5), (timer) {
      _pollCheckingTransactions();
    });
  }

  @override
  void dispose() {
    _txSubscription?.cancel();
    _pollingTimer?.cancel();
    super.dispose();
  }

  Future<void> _checkServiceStatus() async {
    final isRunning = await MethodChannelService.isServiceRunning();
    if (mounted) {
      setState(() {
        _isServiceRunning = isRunning;
      });
    }
  }

  Future<void> _toggleService() async {
    if (_isServiceRunning) {
      await MethodChannelService.stopService();
    } else {
      await MethodChannelService.startService();
    }
    await _checkServiceStatus();
  }

  Future<void> _pingServer() async {
    try {
      final responseBody = await MethodChannelService.httpGet('http://10.0.2.2:5000/api/status');
      if (responseBody != null) {
        if (mounted) {
          setState(() {
            _serverStatus = 'متصل نشط';
            _serverStatusColor = Colors.green;
          });
        }
      } else {
        throw Exception('Bad status code');
      }
    } catch (_) {
      if (mounted) {
        setState(() {
          _serverStatus = 'غير متصل';
          _serverStatusColor = Colors.red;
        });
      }
    }
  }

  void _listenToTransactions() {
    _txSubscription = MethodChannelService.transactionsStream.listen((event) {
      if (event is String) {
        final tx = jsonDecode(event) as Map<String, dynamic>;
        
        // Ensure tx has a timestamp for our local 60s countdown
        if (!tx.containsKey('timestamp')) {
          tx['timestamp'] = DateTime.now().millisecondsSinceEpoch;
        }

        setState(() {
          final existingIndex = _transactions.indexWhere((t) => t['tx_id'] != null && t['tx_id'] == tx['tx_id'] && tx['tx_id'] != "");
          if (existingIndex >= 0) {
            _transactions[existingIndex] = tx;
          } else {
            // Check by message if tx_id not found
            final msgIndex = _transactions.indexWhere((t) => t['message'] == tx['message'] && t['date'] == tx['date']);
            if (msgIndex >= 0) {
                _transactions[msgIndex] = tx;
            } else {
                _transactions.insert(0, tx);
            }
          }
        });
      }
    });
  }

  Future<void> _pollCheckingTransactions() async {
    final checkingTxs = _transactions.where((tx) => tx['status'] == 'checking' && tx['tx_id'] != null && tx['tx_id'] != "").toList();
    
    for (var tx in checkingTxs) {
      try {
        final responseBody = await MethodChannelService.httpGet('http://10.0.2.2:5000/api/payments/status/${tx['tx_id']}');
            
        if (responseBody != null) {
          final data = jsonDecode(responseBody);
          if (data['status'] != 'checking') {
            if (mounted) {
              setState(() {
                tx['status'] = data['status'];
              });
            }
          }
        }
      } catch (_) {
        // Ignore network errors, will retry next tick
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    final List<Widget> pages = [
      DashboardTab(
        transactions: _transactions,
        isServiceRunning: _isServiceRunning,
        serverStatus: _serverStatus,
        serverStatusColor: _serverStatusColor,
        onToggleService: _toggleService,
      ),
      TransactionsTab(transactions: _transactions),
      const SettingsTab(),
    ];

    return Scaffold(
      body: IndexedStack(
        index: _currentIndex,
        children: pages,
      ),
      bottomNavigationBar: Container(
        decoration: BoxDecoration(
          boxShadow: [
            BoxShadow(
              color: Colors.black.withOpacity(0.05),
              blurRadius: 10,
              offset: const Offset(0, -5),
            ),
          ],
        ),
        child: BottomNavigationBar(
          currentIndex: _currentIndex,
          onTap: (index) {
            setState(() {
              _currentIndex = index;
            });
          },
          backgroundColor: Colors.white,
          elevation: 0,
          selectedItemColor: Theme.of(context).primaryColor,
          unselectedItemColor: Colors.grey.shade400,
          selectedLabelStyle: const TextStyle(fontWeight: FontWeight.bold),
          items: const [
            BottomNavigationBarItem(
              icon: Directionality(textDirection: TextDirection.ltr, child: Icon(PhosphorIconsRegular.squaresFour)),
              activeIcon: Directionality(textDirection: TextDirection.ltr, child: Icon(PhosphorIconsFill.squaresFour)),
              label: 'لوحة التحكم',
            ),
            BottomNavigationBarItem(
              icon: Directionality(textDirection: TextDirection.ltr, child: Icon(PhosphorIconsRegular.listDashes)),
              activeIcon: Directionality(textDirection: TextDirection.ltr, child: Icon(PhosphorIconsFill.listDashes)),
              label: 'العمليات',
            ),
            BottomNavigationBarItem(
              icon: Directionality(textDirection: TextDirection.ltr, child: Icon(PhosphorIconsRegular.gearSix)),
              activeIcon: Directionality(textDirection: TextDirection.ltr, child: Icon(PhosphorIconsFill.gearSix)),
              label: 'الإعدادات',
            ),
          ],
        ),
      ),
    );
  }
}

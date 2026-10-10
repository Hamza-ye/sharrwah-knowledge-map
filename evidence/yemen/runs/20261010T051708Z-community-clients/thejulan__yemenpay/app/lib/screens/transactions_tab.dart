import 'package:flutter/material.dart';
import 'package:phosphor_flutter/phosphor_flutter.dart';

class TransactionsTab extends StatefulWidget {
  final List<Map<String, dynamic>> transactions;

  const TransactionsTab({Key? key, required this.transactions})
      : super(key: key);

  @override
  State<TransactionsTab> createState() => _TransactionsTabState();
}

class _TransactionsTabState extends State<TransactionsTab> {
  String _filterType = 'all'; // all, automated, regular
  String _filterWallet = 'all'; // all, KuraimiIMB, Jaib, etc.

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
      statusWidget = Row(
        mainAxisSize: MainAxisSize.min,
        children: [
          const SizedBox(
            width: 14,
            height: 14,
            child:
                CircularProgressIndicator(strokeWidth: 2, color: Colors.orange),
          ),
          const SizedBox(width: 6),
          Text('قيد الانتظار',
              style: const TextStyle(
                  color: Colors.orange,
                  fontSize: 12,
                  fontWeight: FontWeight.bold)),
        ],
      );
    } else if (tx['status'] == 'automated' || tx['status'] == 'success') {
      statusIcon = PhosphorIconsRegular.checkCircle;
      statusColor = Colors.green;
      statusWidget = Icon(statusIcon, color: statusColor, size: 24);
    } else if (tx['status'] == 'failed') {
      statusIcon = PhosphorIconsRegular.xCircle;
      statusColor = Colors.red;
      statusWidget = Icon(statusIcon, color: statusColor, size: 24);
    } else {
      statusIcon = PhosphorIconsRegular.info;
      statusColor = Colors.blue;
      statusWidget = Icon(statusIcon, color: statusColor, size: 24);
    }

    return Container(
      margin: const EdgeInsets.only(bottom: 12),
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: Colors.grey.shade200),
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
    // Filter logic
    var filteredList = widget.transactions.where((tx) {
      bool matchesType = true;
      bool matchesWallet = true;

      if (_filterType == 'automated') {
        matchesType = tx['status'] == 'automated';
      } else if (_filterType == 'regular') {
        matchesType = tx['status'] == 'regular';
      }

      if (_filterWallet != 'all') {
        final w = tx['wallet'].toString().toLowerCase();
        matchesWallet = w.contains(_filterWallet.toLowerCase());
      }

      return matchesType && matchesWallet;
    }).toList();

    return SafeArea(
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          Container(
            padding: const EdgeInsets.all(24),
            color: Colors.white,
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const Text(
                  'سجل العمليات',
                  style: TextStyle(fontWeight: FontWeight.w900, fontSize: 24),
                ),
                const SizedBox(height: 16),
                Row(
                  children: [
                    Expanded(
                      child: Container(
                        padding: const EdgeInsets.symmetric(horizontal: 12),
                        decoration: BoxDecoration(
                          color: Colors.grey.shade100,
                          borderRadius: BorderRadius.circular(12),
                        ),
                        child: DropdownButtonHideUnderline(
                          child: DropdownButton<String>(
                            value: _filterType,
                            isExpanded: true,
                            icon: const Directionality(
                                textDirection: TextDirection.ltr,
                                child: Icon(PhosphorIconsRegular.caretDown)),
                            items: const [
                              DropdownMenuItem(
                                  value: 'all', child: Text('جميع العمليات')),
                              DropdownMenuItem(
                                  value: 'automated',
                                  child: Text('مؤكدة آلياً')),
                              DropdownMenuItem(
                                  value: 'regular', child: Text('عادية')),
                            ],
                            onChanged: (v) {
                              if (v != null) setState(() => _filterType = v);
                            },
                          ),
                        ),
                      ),
                    ),
                    const SizedBox(width: 12),
                    Expanded(
                      child: Container(
                        padding: const EdgeInsets.symmetric(horizontal: 12),
                        decoration: BoxDecoration(
                          color: Colors.grey.shade100,
                          borderRadius: BorderRadius.circular(12),
                        ),
                        child: DropdownButtonHideUnderline(
                          child: DropdownButton<String>(
                            value: _filterWallet,
                            isExpanded: true,
                            icon: const Directionality(
                                textDirection: TextDirection.ltr,
                                child: Icon(PhosphorIconsRegular.caretDown)),
                            items: const [
                              DropdownMenuItem(
                                  value: 'all', child: Text('جميع المحافظ')),
                              DropdownMenuItem(
                                  value: 'kuraimi', child: Text('الكريمي')),
                              DropdownMenuItem(
                                  value: 'jaib', child: Text('جيب')),
                            ],
                            onChanged: (v) {
                              if (v != null) setState(() => _filterWallet = v);
                            },
                          ),
                        ),
                      ),
                    ),
                  ],
                ),
              ],
            ),
          ),
          Expanded(
            child: Padding(
              padding:
                  const EdgeInsets.symmetric(horizontal: 24.0, vertical: 16.0),
              child: filteredList.isEmpty
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
                              'لا توجد نتائج مطابقة',
                              style: TextStyle(color: Colors.grey.shade500),
                            ),
                          ],
                        ),
                      ),
                    )
                  : ListView.builder(
                      itemCount: filteredList.length,
                      itemBuilder: (context, index) {
                        return _buildTransactionItem(filteredList[index]);
                      },
                    ),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildFilterChip(String label, String value, String currentValue,
      Function(String) onSelected) {
    final isSelected = value == currentValue;
    return ChoiceChip(
      label: Text(label),
      selected: isSelected,
      onSelected: (selected) {
        if (selected) onSelected(value);
      },
      selectedColor: Theme.of(context).primaryColor.withOpacity(0.2),
      labelStyle: TextStyle(
        color:
            isSelected ? Theme.of(context).primaryColor : Colors.grey.shade700,
        fontWeight: isSelected ? FontWeight.bold : FontWeight.normal,
      ),
      backgroundColor: Colors.grey.shade100,
    );
  }
}

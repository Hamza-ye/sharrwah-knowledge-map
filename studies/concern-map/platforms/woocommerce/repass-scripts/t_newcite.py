import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import newcite as n
print(n.R('includes/admin/settings/class-wc-settings-general.php', "'title'    => __( 'Selling location(s)'", "'type'     => 'select',"))
print(n.Web('https://woocommerce.com/document/woopayments/fraud-and-disputes/managing-disputes/', 'A red bubble next to the Payments > Disputes menu item.', 'Dispute notifications'))

#!/usr/bin/env bash
# The test store's database as one run under woocommerce/raw/runs/<run-id>/: where WooCommerce and WooPayments hold
# what the store's pages show (the store's country, the payments account, orders, tax rates).
#   capture/woocommerce/db_snapshot.sh <label>
#   wordpress.sql   the whole database (mariadb-dump), as the store holds it
#   options.tsv     the options table (option_name, autoload, option_value), one row per option
#   run.json        kind db, time, server and dump versions
set -euo pipefail
label="$1"
root="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$root"
run_id="$(date -u +%Y%m%dT%H%M%SZ)-$label"
dir="woocommerce/raw/runs/$run_id"
mkdir -p "$dir"
dc() { docker compose --env-file .env -f capture/woocommerce/compose.yaml "$@"; }
pw="$(grep '^WOO_DB_PASSWORD=' .env | cut -d= -f2-)"
started="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
dc exec -T db mariadb-dump -uroot -p"$pw" --skip-dump-date wordpress > "$dir/wordpress.sql"
dc exec -T db mariadb -uroot -p"$pw" --batch -e \
  "SELECT option_name, autoload, option_value FROM wp_options ORDER BY option_name" wordpress > "$dir/options.tsv"
server="$(dc exec -T db mariadb -uroot -p"$pw" -N -e 'SELECT VERSION()')"
cat > "$dir/run.json" <<EOF
{
  "run_id": "$run_id", "platform": "woocommerce", "label": "$label", "kind": "db", "started": "$started",
  "ended": "$(date -u +%Y-%m-%dT%H:%M:%SZ)", "tool": "mariadb-dump (MariaDB $server)", "database": "wordpress",
  "script": {"path": "capture/woocommerce/db_snapshot.sh", "sha256": "$(sha256sum "$0" | cut -d' ' -f1)"}
}
EOF
echo "$dir"

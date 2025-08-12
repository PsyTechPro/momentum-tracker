import yfinance as yf
import warnings
from datetime import datetime, timedelta, timezone
import pandas as pd
import json
import os

warnings.filterwarnings("ignore")

# ---- Settings ----
SYMBOLS = ["BTC-USD", "ETH-USD", "SOL-USD", "AAPL"]
LOOKBACK_DAYS = 60  # momentum window (calendar days)
# ------------------

# Use UTC to match GitHub Actions / cron time
now_utc = datetime.now(timezone.utc)

end_date = now_utc.date()                      # today (UTC)
start_date = end_date - timedelta(days=LOOKBACK_DAYS)

results = []

for symbol in SYMBOLS:
    # Pull a little extra history to be safe
    data = yf.download(
        symbol,
        start=(start_date - timedelta(days=3)).strftime("%Y-%m-%d"),
        end=(end_date + timedelta(days=1)).strftime("%Y-%m-%d"),
        interval="1d",
        auto_adjust=True,
        progress=False
    )

    closes = data.get("Close", pd.Series(dtype=float)).dropna()
    if len(closes) >= 2:
        first = float(closes.iloc[0])
        last = float(closes.iloc[-1])
        momentum = (last / first) - 1.0
        momentum_pct = f"{momentum:.2%}"
    else:
        momentum = None
        momentum_pct = None

    results.append({
        "symbol": symbol,
        "start_price": float(closes.iloc[0]) if len(closes) >= 1 else None,
        "end_price": float(closes.iloc[-1]) if len(closes) >= 1 else None,
        "momentum": round(momentum, 6) if momentum is not None else None,
        "momentum_pct": momentum_pct
    })

payload = {
    "generated_at_utc": now_utc.isoformat(),
    "lookback_days": LOOKBACK_DAYS,
    "start_date": start_date.isoformat(),
    "end_date": end_date.isoformat(),
    "assets": results
}

with open("momentum.json", "w", encoding="utf-8") as f:
    json.dump(payload, f, indent=2)

# Print results in GitHub Actions log
print("\nMomentum Results:")
for asset in results:
    print(f"{asset['symbol']}: {asset['momentum_pct']} "
          f"(from {asset['start_price']:.2f} to {asset['end_price']:.2f})")

print("Wrote momentum.json")

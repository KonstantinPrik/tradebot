# =========================
# Trading
# =========================
SYMBOL = "BTCUSDT"
TESTNET = True

API_KEY = ""
API_SECRET = ""

# =========================
# Risk management
# =========================
RISK_PER_TRADE = 0.005      # 0.5% риска на сделку
SL_PCT = 0.002              # 0.2% стоп
LEVERAGE = 2

DAILY_MAX_LOSS = 0.02       # 2% макс убыток в день
MAX_TRADES_PER_DAY = 10

# =========================
# Strategy filters
# =========================
IMPULSE_PCT = 0.12          # импульс %
VOL_MULTIPLIER = 1.6        # объём x раз выше среднего
MIN_VOLATILITY = 0.08       # мин волатильность %
SPREAD_MAX = 0.05           # макс спред %

# =========================
# Cooldown / protection
# =========================
COOLDOWN_SECONDS = 60

# =========================
# Telegram alerts
# =========================
TELEGRAM_TOKEN = ""
TELEGRAM_CHAT_ID = ""

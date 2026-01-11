from statistics import mean
from config import IMPULSE_PCT, VOL_MULTIPLIER, MIN_VOLATILITY, SPREAD_MAX


class Strategy:
  def check_signal(self, candles, spread):
    closes = [c["close"] for c in candles]
    vols = [c["volume"] for c in candles]
    impulse = (closes[-1] - closes[-10]) / closes[-10] * 100
    volume_ratio = vols[-1] / mean(vols[:-1])
    volatility = (max(closes[-20:]) - min(closes[-20:])) / closes[-1] * 100
    if spread > SPREAD_MAX:
     return None, impulse, volume_ratio, volatility
    if impulse > IMPULSE_PCT and volume_ratio > VOL_MULTIPLIER and volatility > MIN_VOLATILITY:
      return "Buy", impulse, volume_ratio, volatility
    return None, impulse, volume_ratio, volatility
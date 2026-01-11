from config import RISK_PER_TRADE, SL_PCT, LEVERAGE


class PositionSizer:
  def calculate_qty(self, balance, price):
    risk_usdt = balance * RISK_PER_TRADE
    position_value = risk_usdt / SL_PCT
    position_value *= LEVERAGE
    qty = position_value / price
    return round(qty, 6)
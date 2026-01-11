import asyncio
from live.datafeed_async import DataFeedAsync
from live.trader_async import TraderAsync
from strategy.strategy import Strategy
from risk.risk_manager import RiskManager
from risk.position_sizer import PositionSizer
from risk.daily_guard import DailyGuard
from logs.trade_logger import TradeLogger
from infra.notifier import Notifier
from config import SYMBOL


async def main():
  trader = TraderAsync()
  strategy = Strategy()
  risk = RiskManager()
  pos_sizer = PositionSizer()
  notifier = Notifier()


  balance = 1000 # заглушка, заменить на live баланс
  daily = DailyGuard(balance)
  logger = TradeLogger()

  async def on_candles(msg):
    if not risk.can_trade():
      return
    spread = await trader.get_spread(SYMBOL)
    signal, impulse, vol_ratio, volatility = strategy.check_signal([msg], spread)
    if signal and daily.can_trade(balance):
      price = float(msg["p"])
      qty = pos_sizer.calculate_qty(balance, price)
      await trader.market_order(SYMBOL, signal, qty)
      sl = price * (1 - 0.001)
      tp = price * (1 + 0.0018)
      await trader.set_sl_tp(SYMBOL, sl, tp)
      risk.on_trade_open()
      daily.register_trade()
      logger.log(signal, price, impulse, vol_ratio, volatility)
      notifier.send(f"Entered {signal} @ {price}")


  feed = DataFeedAsync(SYMBOL, on_candles)
  await feed.start()

asyncio.run(main())
from pybit.unified_trading import HTTP
from config import API_KEY, API_SECRET, TESTNET


class TraderAsync:
  def __init__(self):
    self.session = HTTP(testnet=TESTNET, api_key=API_KEY, api_secret=API_SECRET)


async def market_order(self, symbol, side, qty):
  return self.session.place_order(category="linear", symbol=symbol, side=side, orderType="Market", qty=qty)


async def set_sl_tp(self, symbol, sl, tp):
  return self.session.set_trading_stop(category="linear", symbol=symbol, stopLoss=str(sl), takeProfit=str(tp))


async def get_spread(self, symbol):
  ob = self.session.get_orderbook(category="linear", symbol=symbol, limit=1)
  bid = float(ob["result"]["b"][0][0])
  ask = float(ob["result"]["a"][0][0])
  return (ask - bid) / bid * 100
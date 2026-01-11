import asyncio
from pybit.unified_trading import WebSocket


class DataFeedAsync:
  def __init__(self, symbol, callback, testnet=True):
    self.ws = WebSocket(testnet=testnet, channel_type="linear")
    self.symbol = symbol
    self.callback = callback


  async def start(self):
    self.ws.trade_stream(symbol=self.symbol, callback=self.on_trade)


  async def on_trade(self, msg):
    await self.callback(msg)
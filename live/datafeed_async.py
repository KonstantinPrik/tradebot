import asyncio
from pybit.unified_trading import WebSocket


class DataFeedAsync:
    def __init__(self, symbol, on_trade_async, testnet=True):
        self.symbol = symbol
        self.on_trade_async = on_trade_async
        self.ws = WebSocket(testnet=testnet, channel_type="linear")

    def _callback(self, msg):
        # Эта функция синхронная → безопасно прокидываем в asyncio
        loop = asyncio.get_event_loop()
        loop.call_soon_threadsafe(
            asyncio.create_task,
            self.on_trade_async(msg)
        )

    async def start(self):
        # ВАЖНО: сюда передаём только sync callback
        self.ws.trade_stream(
            symbol=self.symbol,
            callback=self._callback
        )

        # держим процесс живым
        while True:
            await asyncio.sleep(1)

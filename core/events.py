class Event:
  async def handle(self, bus): pass


class MarketEvent(Event): pass
class SignalEvent(Event): pass
class OrderEvent(Event): pass
class FillEvent(Event): pass
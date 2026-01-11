import asyncio
from core.bus import EventBus


class Engine:
  def __init__(self):
    self.bus = EventBus()


async def run(self):
  while True:
    event = await self.bus.get()
  await event.handle(self.bus)
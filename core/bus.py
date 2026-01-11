import asyncio


class EventBus:
  def __init__(self):
    self.queue = asyncio.Queue()


async def put(self, event):
  await self.queue.put(event)


async def get(self):
  return await self.queue.get()
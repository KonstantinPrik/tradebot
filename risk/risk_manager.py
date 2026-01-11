import time


class RiskManager:
  def __init__(self, cooldown=30):
    self.last_trade_time = 0
    self.position_open = False
    self.cooldown = cooldown


def can_trade(self):
  return (time.time() - self.last_trade_time) > self.cooldown and not self.position_open


def on_trade_open(self):
  self.position_open = True
  self.last_trade_time = time.time()


def on_trade_close(self):
  self.position_open = False
import datetime

from config import DAILY_MAX_LOSS, MAX_TRADES_PER_DAY


class DailyGuard:
  def __init__(self, start_balance):
    self.start_balance = start_balance
    self.trades = 0
    self.date = datetime.date.today()


def can_trade(self, current_balance):
  if datetime.date.today() != self.date:
    self.start_balance = current_balance
    self.trades = 0
    self.date = datetime.date.today()


  if self.trades >= MAX_TRADES_PER_DAY:
    return False
  if (self.start_balance - current_balance) / self.start_balance > DAILY_MAX_LOSS:
    return False
  return True


def register_trade(self):
  self.trades += 1
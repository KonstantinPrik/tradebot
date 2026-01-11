import csv
from datetime import datetime


class TradeLogger:
  def __init__(self, file="trades.csv"):
    self.file = file
    with open(self.file, "a", newline="") as f:
      writer = csv.writer(f)
      if f.tell() == 0:
        writer.writerow(["time", "side", "price", "impulse", "volume_ratio", "volatility"])


def log(self, side, price, impulse, volume_ratio, volatility):
  with open(self.file, "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([datetime.utcnow().isoformat(), side, price, round(impulse,4), round(volume_ratio,2), round(volatility,4)])
import requests
from config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID


class Notifier:
  def send(self, text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": TELEGRAM_CHAT_ID, "text": text})
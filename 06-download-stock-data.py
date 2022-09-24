import time
from datetime import datetime

import requests

ticker = input("Enter a ticker symbol: ")
from_date = input("Enter start date (YYYY/MM/DD): ")
to_date = input("Enter end date (YYYY/MM/DD): ")

from_datetime = datetime.strptime(from_date, "%Y/%m/%d")
to_datetime = datetime.strptime(to_date, "%Y/%m/%d")

from_epoch = int(time.mktime(from_datetime.timetuple()))
to_epoch = int(time.mktime(to_datetime.timetuple()))

url = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={from_epoch}&period2={to_epoch}&interval=1d&events=history&includeAdjustedClose=true"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}

content = requests.get(url, headers=headers).content

with open(f"{ticker.lower()}.csv", "wb") as f:
    f.write(content)

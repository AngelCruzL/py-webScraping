from locale import currency

import requests
from bs4 import BeautifulSoup


def get_currency(in_currency, out_currency):
    url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1"
    content = requests.get(url).text
    soup = BeautifulSoup(content, "html.parser")
    rate = soup.find("span", {"class": "ccOutputRslt"}).get_text()
    rate = float(rate[:-4])

    return rate


print(get_currency("USD", "MXN"))

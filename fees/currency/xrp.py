import requests

from fees import Fee

def get_fee():
  currency = 'XRP'
  url = "https://data.ripple.com/v2/network/fees?interval=day&limit=1&descending=true"

  try:
    response = requests.get(url=url)
    data = response.json()
    latest = data['rows'][0]
    return Fee(
      currency,
      latest['avg'],
      latest['min']
    )
  except Exception as e:
    return Fee(currency, 0, 0)


def gas_price(gas_quantity, gwei):
  return gwei / 10 / 100000000
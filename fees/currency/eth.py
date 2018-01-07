import requests

from fees import Fee

def get_fee():
  currency = 'ETH'
  url = "https://ethgasstation.info/json/ethgasAPI.json"
  gas_quantity = 21001 # Min gas quantity

  try:
    response = requests.get(url=url)
    data = response.json()
    # response is in Gwei * 10
    return Fee(
      currency,
      gas_price(gas_quantity, data['fastest']),
      gas_price(gas_quantity, data['safeLow'])
    )
  except Exception as e:
    return Fee(currency, 0, 0)


def gas_price(gas_quantity, gwei):
  return gwei / 10 / 100000000
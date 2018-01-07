import requests

from fees import Fee

def get_fee():
    currency = 'BTC'
    url = "https://bitcoinfees.earn.com/api/v1/fees/recommended"
    satoshi = 100000000

    try:
        response = requests.get(url=url)
        data = response.json()
        return Fee(currency, data['fastestFee'] / satoshi, data['hourFee'] / satoshi)
    except Exception as e:
        return Fee(currency, 0, 0)
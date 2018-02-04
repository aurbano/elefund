from .currency import btc
from .currency import eth
from .currency import xrp


class Calculator:
    def __init__(self, fee_store):
        self.fee_store = fee_store
        self.calculators = {
            'BTC': btc,
            'ETH': eth,
            'XRP': xrp
        }

    def start(self):
        for currency in self.calculators:
          self.fee_store[currency] = self.calculators[currency].get_fee()

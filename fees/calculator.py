from .currency import btc
from .currency import eth
from .currency import xrp

from state import fee_store


class Calculator:
    def __init__(self):
        self.fee_store = fee_store
        self.calculators = {
            'BTC': btc,
            'ETH': eth,
            'XRP': xrp
        }

    def start(self):
        for currency in self.calculators:
          self.fee_store[currency] = self.calculators[currency].get_fee()

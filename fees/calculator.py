from .currency import btc

from state import fee_store

class Calculator ():
    def __init__(self):
        self.fee_store = fee_store

    def start(self):
        self.fee_store['BTC'] = btc.get_fee()
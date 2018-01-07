import pprint
from .currency import btc

class Calculator ():
    def __init__(self, fee_store):
        self.fee_store = fee_store

    def start(self):
        self.fee_store['BTC'] = btc.get_fee()
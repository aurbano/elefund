#!/usr/bin/env python3

class ExchangeRate(object):
    def __init__(self, from_currency, to_currency, exchange, rates):
        self.from_currency = from_currency
        self.to_currency = to_currency
        self.exchange = exchange
        self.rates = rates

class Rates(object):
    def __init__(self, buy, sell, fee):
        self.buy = buy
        self.sell = sell
        self.fee = fee
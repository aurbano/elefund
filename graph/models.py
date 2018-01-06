#!/usr/bin/env python3

class ExchangeRate(object):
    def __init__(self, from_currency, to_currency, exchange, rates):
        self.from_currency = from_currency
        self.to_currency = to_currency
        self.exchange = exchange
        self.rates = rates

    def __eq__(self, other):
        print(other)
        return self.__dict__ == other.__dict__
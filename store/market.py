#!/usr/bin/env python3

import networkx as nx

class Market(object):
    """A market object that exposes arbitrage specific calculation and shortest path routines"""

    def __init__(self):
        self._graph = nx.MultiDiGraph()

    def add_or_update_exchange_rates(self, exchange_rates):
        for exchange_rate in exchange_rates:
            self._graph.add_edge(exchange_rate.from_currency, exchange_rate.to_currency,
                                 exchange=exchange_rate.exchange, rate=exchange_rate.rates.buy,
                                 fee=exchange_rate.rates.fee)
            self._graph.add_edge(exchange_rate.to_currency, exchange_rate.from_currency,
                                 exchange=exchange_rate.exchange, rate=exchange_rate.rates.sell,
                                 fee=exchange_rate.rates.fee)

    def get_exchange_rates(self):
        for edge in self._graph.edges(data=True):
            print(edge)

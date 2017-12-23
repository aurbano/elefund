#!/usr/bin/env python3

import networkx as nx

class Market(object):
    """A market object that exposes arbitrage specific calculation and shortest path routines"""

    def __init__(self):
        self._graph = nx.Graph()

    def add_or_update_exchange_rates(self, exchange_rates):
        for exchange_rate in exchange_rates:
            from_currency = exchange_rate.from_currency
            self._graph.add_node(from_currency)

            to_currency = exchange_rate.to_currency
            self._graph.add_node(to_currency)

            print(from_currency)
            print(to_currency)
            print(exchange_rate)
            print(exchange_rate.rates.buy)
            print(exchange_rate.rates.sell)
            print(exchange_rate.rates.fee)
            self._graph.add_edge(from_currency, to_currency)
            self._graph.add_edge(to_currency, from_currency)

    def get_exchange_rates(self):
        return [node for node in self._graph.nodes]
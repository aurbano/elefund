#!/usr/bin/env python3

import networkx as nx

class Market(object):
    """A market object that exposes rate update and shortest path routines"""

    def __init__(self):
        self._graph = nx.MultiDiGraph()

    def add_or_update_exchange_rate(self, from_currency, to_currency, exchange, rate):
        from_node = self._create_node_object(exchange, from_currency)
        to_node = self._create_node_object(exchange, to_currency)
        key = from_node+'>'+to_node

        print('ADD %s' % key)
        self._graph.add_edge(from_node, to_node, key=key, rate=rate)

    def get_rate(self, arc):
        from_node = self._create_node_object(arc.exchange, arc.from_currency)
        to_node = self._create_node_object(arc.exchange, arc.to_currency)
        key = from_node+'>'+to_node

        print('GR %s' % key)
        print(self._graph.get_edge_data(from_node, to_node, key=key))
        return self._graph.get_edge_data(from_node, to_node, key=key)['rate']

    def _create_node_object(self, exchange, currency):
        return currency+'@'+exchange
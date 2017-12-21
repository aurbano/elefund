#!/usr/bin/env python3

import networkx as nx

class Market(object):
    """A market object that exposes arbitrage specific calculation and shortest path routines"""

    def __init__(self):
        _graph = nx.Graph()

    def add_or_update_exchange_quotes(self, exchange_quotes):
        print('Not implemented')

    def get_exchange_quotes(self):
        print('Not implemented')
        

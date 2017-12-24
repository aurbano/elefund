# -*- coding: utf-8 -*-

import os
import sys
import networkx as nx
import pprint

# -----------------------------------------------------------------------------

this_folder = os.path.dirname(os.path.abspath(__file__))
root_folder = os.path.dirname(os.path.dirname(this_folder))
sys.path.append(root_folder + '/python')
sys.path.append(this_folder)

# -----------------------------------------------------------------------------

import ccxt  # noqa: E402

# -----------------------------------------------------------------------------
bitfinex = ccxt.bitfinex()
kraken = ccxt.kraken()


withdrawalFees = [
	'Bitfinex,ETH,0.005',
	'Kraken,ETH,0.01',
	'Bitfinex,BTC,0.0005',
	'Kraken,BTC,0.001'
	]

arcs = []
nodes = []
G=nx.DiGraph()

class Node:
	def __init__(self, exchange, currency):
		self.exchange = exchange
		self.currency = currency

	def __hash__(self):
		return hash(self.exchange) + hash(self.currency)

	def __str__(self):
		return self.currency + "@" + self.exchange.name

	def __repr__(self):
		return self.currency + "@" + self.exchange.name


class Arc(object):
	def __init__(self, fromCurrency, toCurrency, exchange, price):
		self.toCurrency = toCurrency
		self.fromCurrency = fromCurrency
		self.exchange = exchange
		self.price = price

	def __str__(self):
		return "From " + str(self.fromCurrency) + " to " + str(self.toCurrency) + " with weight= " + str(self.price)

	def __repr__(self):
		return "From " + str(self.fromCurrency) + " to " + str(self.toCurrency) + " with weight= " + str(self.price)



def create_currency_pair(exchange, fromCurrency, toCurrency):
	orderbook = exchange.fetch_order_book (createSymbol(fromCurrency, toCurrency))
	bid = orderbook['bids'][0][0] if len (orderbook['bids']) > 0 else None
	ask = orderbook['asks'][0][0] if len (orderbook['asks']) > 0 else None
	spread = (ask - bid) if (bid and ask) else None

	fromNode = Node(exchange, fromCurrency)
	toNode = Node(exchange, toCurrency)
	nodes.append(fromNode)
	nodes.append(toNode)


	print(exchange.id, 'market price', { 'bid': bid, 'ask': ask, 'spread': spread })
	fromToArc = Arc(fromNode, toNode, exchange, bid)
	arcs.append(fromToArc)
	toFromArc = Arc(toNode, fromNode, exchange, ask)
	arcs.append(toFromArc)


def createSymbol(fromCurrency, toCurrency):
	return fromCurrency + "/" + toCurrency


def linkExchanges():
	for each in nodes:
		for compare in nodes:
			if (each.currency == compare.currency and each.exchange != compare.exchange): 
				withdrawalFee = getWithdrawalFee(each.exchange, each.currency)
				withdrawalArc = Arc(each, compare, each.exchange, withdrawalFee)
				arcs.append(withdrawalArc)

def getWithdrawalFee(exchange, currency):
	for withdrawalFee in withdrawalFees:
		split = withdrawalFee.split(',')
		if (split[0]+split[1] == exchange.name+currency):
			print ("Withdrawal fee = " + str(split[2]))
			return split[2]

def addToGraph():
	G.add_nodes_from(nodes)

	weighted_edges = []
	for arc in arcs:
		print("Adding " + str(arc))
		weighted_edges.append([arc.fromCurrency, arc.toCurrency, arc.price])
	G.add_weighted_edges_from(weighted_edges)


create_currency_pair(bitfinex, 'ETH', 'BTC')
create_currency_pair(kraken, 'ETH', 'BTC')

linkExchanges()

addToGraph()

pprint.pprint(nx.floyd_warshall(G))


from .spread_calculator import SpreadCalculator
from .arc import Arc

class PathFinder(object):

	spread_calculator = SpreadCalculator()
	hard_coded = [
			Arc('ETH', 'BTC', 'Kraken'),
			Arc('BTC', 'XRP', 'Kraken'),
			Arc('XRP', 'XRP', 'Kraken'),
			Arc('XRP', 'BTC', 'Qryptos'),
			Arc('BTC', 'ETH', 'Qryptos'),
			Arc('ETH', 'ETH', 'Qryptos')
	]
	updated_arcs = []
	strategies = []


	def __init__(self, graph):
		self.graph = graph
		self.strategies = [
			hard_coded
		]

	def start():
		while True:
			arc = self.updated_arcs.get()
			for each in self.hard_coded:
				if each == arc:
					spread = self.calc_path_spread(self.hard_coded)
					print spread


	def arc_updated(self, arc):
		updated_arcs.append(arc)


	def calc_path_spread(self, path):
		dictionary = []
		for each_arc in path:
			current_rate = self.graph.get_rate(each_arc)
			dictionary.append({'arc': each_arc, 'rate': current_rate})
		return self.spread_calculator.calc(dictionary)
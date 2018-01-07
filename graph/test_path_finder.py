from .path_finder import PathFinder
from .arc import Arc
from .mock_graph import MockGraph

graph = MockGraph()

path_finder = PathFinder(graph)

def test_arc_updated_calculates_spread():

	graph.add_rate(Arc('ETH', 'BTC', 'Kraken'), 1)
	graph.add_rate(Arc('BTC', 'XRP', 'Kraken'), 1)
	graph.add_rate(Arc('XRP', 'XRP', 'Kraken'), 1)
	graph.add_rate(Arc('XRP', 'BTC', 'Qryptos'), 1)
	graph.add_rate(Arc('BTC', 'ETH', 'Qryptos'), 1)
	graph.add_rate(Arc('ETH', 'ETH', 'Qryptos'), 1)

	path_finder.arc_updated(Arc('ETH', 'BTC', 'Kraken'))
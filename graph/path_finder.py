from .spread_calculator import SpreadCalculator
from .arc import Arc
from multiprocessing import Queue
import threading


class PathFinder:
    spread_calculator = SpreadCalculator()
    hard_coded = [
        Arc('ETH', 'BTC', 'kraken'),
        Arc('BTC', 'XRP', 'kraken'),
        Arc('XRP', 'XRP', 'kraken'),
        Arc('XRP', 'BTC', 'bittrex'),
        Arc('BTC', 'ETH', 'bittrex'),
        Arc('ETH', 'ETH', 'bittrex')
    ]
    strategies = []

    def __init__(self, graph, updated_arcs):
        self.graph = graph
        self.updated_arcs = updated_arcs
        self.strategies = [
            self.hard_coded
        ]

    def start_pricing(self):
        path_finder_calc = threading.Thread(target=self.__run_pricing, args=())
        path_finder_calc.setDaemon(True)
        path_finder_calc.start()
        return path_finder_calc

    def __run_pricing(self):
        while True:
            arc = self.updated_arcs.get(True)
            for each in self.hard_coded:
                if each == arc:
                    print('Found %s', each)
                    spread = self.calc_path_spread(self.hard_coded)
                    print(spread)

    def calc_path_spread(self, path):
        dictionary = []
        for each_arc in path:
            current_rate = self.graph.get_rate(each_arc)
            dictionary.append({'arc': each_arc, 'rate': current_rate})
        return self.spread_calculator.calc(dictionary)

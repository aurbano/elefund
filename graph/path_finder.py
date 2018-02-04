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
    updated_arcs = Queue(maxsize=1000)
    strategies = []

    def __init__(self, graph):
        self.graph = graph
        self.strategies = [
            self.hard_coded
        ]

    def start_pricing(self):
        path_finder_calc = threading.Thread(target=self.__run_pricing, args=())
        path_finder_calc.setDaemon(True)
        path_finder_calc.start()
        return self

    def __run_pricing(self):
        while True:
            arc = self.updated_arcs.get(True)
            for each in self.hard_coded:
                if each == arc:
                    print('Found %s', each)
                    spread = self.calc_path_spread(self.hard_coded)
                    print(spread)

    def arc_updated(self, arc):
        self.updated_arcs.put(arc)

    def calc_path_spread(self, path):
        dictionary = []
        for each_arc in path:
            current_rate = self.graph.get_rate(each_arc)
            dictionary.append({'arc': each_arc, 'rate': current_rate})
        return self.spread_calculator.calc(dictionary)

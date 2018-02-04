#!/usr/bin/env python3

from pricer import Pricer
from graph import Market
from fees import Calculator
from graph import PathFinder
from multiprocessing import Queue


updated_arcs = Queue(maxsize=1000) #shared queue between strats and graph
market = Market(updated_arcs)
path_finder = PathFinder(market, updated_arcs).start_pricing()


fee_store = {}

pricer = Pricer(market).start()


Calculator(fee_store).start()


print('fees')
print(fee_store)

pricer.join()
path_finder.join()
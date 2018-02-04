#!/usr/bin/env python3

from pricer import Pricer
from graph import Market
from fees import Calculator
from graph import PathFinder

market = Market()
path_finder = PathFinder(market).start_pricing()
market.add_arc_update_listener(path_finder)
fee_store = {}

pricer = Pricer(market).start()


Calculator(fee_store).start()


print('fees')
print(fee_store)

pricer.join()
path_finder.join()
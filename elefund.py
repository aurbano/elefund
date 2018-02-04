#!/usr/bin/env python3

from pricer import Pricer
from fees import Calculator
from graph import PathFinder

from state import market, updated_arcs, fee_store


path_finder = PathFinder(market, updated_arcs).start_pricing()
pricer = Pricer(market).start()
Calculator(fee_store).start()

print('fees')
print(fee_store)

pricer.join()
path_finder.join()
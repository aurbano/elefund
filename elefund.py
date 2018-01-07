#!/usr/bin/env python3

from pricer import Pricer
from graph import Market
from fees import Calculator
from graph import PathFinder

market = Market()
fee_store = {}

#pricer = Pricer(market).start()
PathFinder(market).start()

Calculator(fee_store).start()


print('fees')
print(fee_store)

#pricer.join()
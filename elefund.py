#!/usr/bin/env python3

from pricer import Pricer
from graph import Market
from fees import Calculator

market = Market()
fee_store = {}

Calculator(fee_store).start()

print('Transaction Fees')
print(fee_store)

pricer = Pricer(market).start()

pricer.join()
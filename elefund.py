#!/usr/bin/env python3

from pricer import Pricer
from fees import Calculator
from state import fee_store

Calculator().start()

print('Transaction Fees')
print(fee_store)

pricer = Pricer().start()

pricer.join()
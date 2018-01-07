#!/usr/bin/env python3

from pricer import Pricer
from fees import Calculator
from state import fee_store

pricer = Pricer().start()
Calculator().start()

print('fees')
print(fee_store)

#pricer.join()
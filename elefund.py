#!/usr/bin/env python3

from pricer import Pricer
from graph import Market

market = Market()

Pricer(market).run()
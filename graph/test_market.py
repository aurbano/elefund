#!/usr/bin/env python3

from decimal import Decimal as D

from .market import Market
from .arc import Arc

def test_whenArcIsAddedToMarketItReturnsRateForArc():
    market = Market()
    arc = Arc('KRAKEN', 'BTC', 'ETH')
    market.add_or_update_exchange_rate(arc, D(1.5))

    assert market.get_rate(arc) == D(1.5)

def test_whenArcIsUpdatedInMarketItReturnsUpdatedRate():
    market = Market()
    arc = Arc('KRAKEN', 'BTC', 'ETH')
    market.add_or_update_exchange_rate(arc, D(1.0))
    market.add_or_update_exchange_rate(arc, D(2))

    assert market.get_rate(Arc('KRAKEN', 'BTC', 'ETH')) == D(2)
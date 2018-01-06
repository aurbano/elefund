#!/usr/bin/env python3

from decimal import Decimal as D

from .market import Market
from .arc import Arc

def test_whenExchangeRateIsAddedToMarketItReturnsRateForArc():
    market = Market()
    market.add_or_update_exchange_rate('BTC', 'ETH', 'KRAKEN', D(1.5))

    assert market.get_rate(Arc('BTC', 'ETH', 'KRAKEN')) == D(1.5)

def test_whenArcIsUpdatedInMarketItReturnsUpdatedRate():
    market = Market()
    market.add_or_update_exchange_rate('BTC', 'ETH', 'KRAKEN', D(1.0))
    market.add_or_update_exchange_rate('BTC', 'ETH', 'KRAKEN', D(2))

    assert market.get_rate(Arc('BTC', 'ETH', 'KRAKEN')) == D(2)
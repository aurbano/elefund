#!/usr/bin/env python3

from decimal import Decimal as D

from .market import Market
from .models import ExchangeRate, Rates

def test_whenAMarketIsInitializedThenItReturnsCorrectMarketrates():
    market = Market()

    input_market_rates = [ExchangeRate('BTC','ETH','BITFINEX', Rates(D(0.0100001010),D(5.12412412412),D(0.0012322))),
                          ExchangeRate('ETH','XMR', 'KRAKEN', Rates(D(1.10),D(2.5),D(0.00168)))]
    market.add_or_update_exchange_rates(input_market_rates)

    actual_market_rates = market.get_exchange_rates()
    assert len(actual_market_rates) == 2
    assert actual_market_rates == input_market_rates

def test_givenInitialisedMarketWhenItIsUpdatedThenItReturnsUpdatedMarketrates():
    market = Market()

    market.add_or_update_exchange_rates([ExchangeRate('BTC','ETH','KRAKEN',Rates(D(1),D(2),D(1.5))),
                                         ExchangeRate('BTC','ETH','BITFINEX',Rates(D(3),D(4),D(3.5)))])

    market_rates_update = [ExchangeRate('BTC','ETH','KRAKEN',Rates(D(5),D(6),D(5.5))),
                           ExchangeRate('ETH','XMR','BITFINEX',Rates(D(7),D(8),D(7.5))),
                           ExchangeRate('XMR','BTC','GDAX',Rates(D(9),D(10),D(9.5)))]
    market.add_or_update_exchange_rates(market_rates_update)

    actual_market_rates = market.get_exchange_rates()
    assert len(actual_market_rates) == 3
    assert actual_market_rates == market_rates_update

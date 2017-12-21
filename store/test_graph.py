import pytest
from graph import MarketGraph

def test_whenAMarketGraphIsInitializedThenItReturnsCorrectMarketState():
    input_market_state = [ExchangeQuote('BITFINEX','BTC','ETH',Prices(D(0.0100001010),D(5.12412412412))),\
            ExchangeQuote('KRAKEN','ETH','XMR',ExchangePrice(D(1.10),D(2.5)))]
    market_graph = MarketGraph()
    market_graph.add_or_update_exchange_quotes(input_market_state)

    actual_market_state = market_graph.get_exchange_quotes()
    assert len(actual_market_state) == 2
    assert actual_market_state == input_market_state

def test_givenInitialisedMarketGraphWhenItIsUpdatedThenItReturnsUpdatedMarketState():
    market_graph = MarketGraph()
    market_graph.add_or_update_exchange_quotes(ExchangeQuote('KRAKEN','BTC','ETH',Prices(D(1),D(2))),\
            ExchangeQuote('BITFINEX','BTC','ETH',Prices(D(3),D(4))))

    market_state_update = [ExchangeQuote('KRAKEN','BTC','ETH',Prices(D(5),D(6))),\
            ExchangeQuote('BITFINEX','ETH','XMR',Prices(D(7),D(8))),\
            ExchangeQuote('GDAX','XMR','XMR',Prices(D(9),D(10)))]
    market_graph.add_or_update_exchange_quotes(market_state_update)

    actual_market_state = market_graph.get_exchange_quotes()
    assert len(actual_market_state) == 3
    assert actual_market_state == market_state_update

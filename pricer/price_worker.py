import logging
import pprint
import time

from .ticker import MarketTicker

logger = logging.Logger('catch_all')


def get_prices(queue, price_callback, market_callback):
    while True:
        market = queue.get()
        try:
            get_price(market, price_callback)
        except Exception as e:
            logger.error(e)
        finally:
            queue.task_done()
            time.sleep(5)
            market_callback(market)
        time.sleep(60)


def get_price(market, price_callback):
    if market['api'].symbols == None:
        print('WARN: Unauth at %s - trying to use the order book' % (market['name']))
        currency_pairs = [
            ['ETH', 'BTC']
        ]
        for currencies in currency_pairs:
            try:
                orderbook = market['api'].fetch_order_book(currencies[0] + "/" + currencies[1])
                bid = orderbook['bids'][0][0] if len (orderbook['bids']) > 0 else None
                ask = orderbook['asks'][0][0] if len (orderbook['asks']) > 0 else None
                price_callback(MarketTicker(currencies[0], currencies[1], market['name'], ask, bid))
            except Exception as e:
                print('WARN: fetch_order_book failed for %s' % (market['name']))
    else:
        try:
            tickers = market['api'].fetch_tickers()
            for pair in tickers:
                currencies = pair.split('/')
                price_callback(MarketTicker(currencies[0], currencies[1], market['name'], tickers[pair]['ask'], tickers[pair]['bid']))
        except Exception as e:
            for symbol in market['api'].symbols:
                ticker = market['api'].fetch_ticker(symbol)
                currencies = symbol.split('/')                
                price_callback(MarketTicker(currencies[0], currencies[1], market['name'], ticker['ask'], ticker['bid']))
import logging
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

def get_price(market, price_callback):
    if market['api'].symbols == None:
        print('WARN: Unauth at %s' % (market['name']))
    else:
        try:
            tickers = market['api'].fetch_tickers()
            #pprint.pprint(tickers)
            for pair in tickers:
                currencies = pair.split('/')
                price_callback(MarketTicker(currencies[0], currencies[1], market['name'], tickers[pair]['ask']))
        except Exception as e:
            for symbol in market['api'].symbols:
                ticker = market['api'].fetch_ticker(symbol)
                currencies = symbol.split('/')                
                price_callback(MarketTicker(currencies[0], currencies[1], market['name'], ticker['ask']))
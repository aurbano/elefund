import logging
import pprint
import time

from .ticker import Ticker

logger = logging.Logger('catch_all')

def get_prices(queue, callback):
    prices = []
    try:
        if market['api'].symbols == None:
            print('WARN: Unauth at %s' % (market['name']))
        else:
            try:
                tickers = market['api'].fetch_tickers()
                #pprint.pprint(tickers)
                for pair in tickers:
                    currencies = pair.split('/')
                    fx_from = currencies[0]
                    fx_to = currencies[1]
                    ask = tickers[pair]['ask']
                    bid = tickers[pair]['bid']
                    # store it both ways
                    prices.append({
                        'market': market['name'],
                        'from': fx_from,
                        'to': fx_to,
                        'price': ask,
                    })
                    prices.append({
                        'market': market['name'],
                        'from': fx_to,
                        'to': fx_from,
                        'price': 1 / ask,
                    })
            except Exception as e:
                for symbol in market['api'].symbols:
                    ticker = market['api'].fetch_ticker(symbol)
                    currencies = symbol.split('/')
                    fx_from = currencies[0]
                    fx_to = currencies[1]
                    ask = ticker['ask']
                    bid = ticker['bid']
                    # store it both ways
                    prices.append({
                        'market': market['name'],
                        'from': fx_from,
                        'to': fx_to,
                        'price': ask,
                    })
                    prices.append({
                        'market': market['name'],
                        'from': fx_to,
                        'to': fx_from,
                        'price': 1 / ask,
                    })
                    time.sleep(1)
    except Exception as e:
        logger.error(e)
    finally:
        return prices
import logging
import pprint

logger = logging.Logger('catch_all')

def get_prices(market):
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
                print('ERROR: %s does not allow getting all tickers at once' % (market['name']))
    except Exception as e:
        logger.error(e)
    finally:
        return prices
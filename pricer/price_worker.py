import logging
import pprint

logger = logging.Logger('catch_all')

def get_prices(market):
    prices = []
    try:
        if market['api'].symbols == None:
            print('WARN: Unauth at %s' % (market['name']))
        else:
            print('%s ------------------' % (market['name']))
            try:
                tickers = market['api'].fetch_tickers()
                #pprint.pprint(tickers)
                for pair in tickers:
                    currencies = pair.split('/')
                    fx_from = currencies[0]
                    fx_to = currencies[1]
                    ask = tickers[pair]['ask']
                    bid = tickers[pair]['bid']
                    print('  From %s to %s - %d' % (fx_from, fx_to, ask));
            except Exception as e:
                print('  Exchange does not allow getting all tickers at once')
    except Exception as e:
        logger.error(e)
    finally:
        return prices
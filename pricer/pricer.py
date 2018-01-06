import time
import ccxt
from multiprocessing.pool import ThreadPool

from .price_worker import get_prices

class Pricer ():
    def __init__(self):
        self.update_markets()

    def run(self):
        print('----- Creating thread pool')
        pool = ThreadPool(10)
        results = pool.map(get_prices, self.markets)
        pool.close()
        pool.join()
        print('----- Thread pool is done')
        print(results)
        #time.sleep(1)
        #self.run()

    def update_markets(self):
        markets = []
        for market_name in ccxt.exchanges:
            cctx_market = getattr(ccxt, market_name);
            market_api = cctx_market()
            markets.append({'name': market_name, 'api': market_api})
        self.markets = markets
        
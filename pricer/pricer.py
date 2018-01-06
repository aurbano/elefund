from Queue import Queue
from threading import Thread
import time
import ccxt

from .price_worker import get_prices

class Pricer ():
    def __init__(self, market):
        self.market = market
        #self.update_markets()
        self.market_queue = Queue(maxsize=0)
        self.pool = []
        for i in range(10):
            worker = Thread(target=get_prices, args=(self.market_queue, self.new_price))
            worker.setDaemon(True)
            self.pool.append(worker)

    def run(self):
        print('----- Creating thread pool')
        pool = ThreadPool(10)
        results = pool.map(get_prices, self.markets)
        pool.close()
        pool.join()
        print('----- Thread pool is done')
        print(results)
        #for result in results:
        #    market.add_or_update_exchange_rate(result['market'], result['from'], result['to'], result['price'])
        #time.sleep(1)
        #self.run()

    def update_markets(self):
        markets = []
        for market_name in ccxt.exchanges:
            cctx_market = getattr(ccxt, market_name);
            market_api = cctx_market()
            markets.append({'name': market_name, 'api': market_api})
        self.markets = markets
        
    def new_price(self, price):
        print('Received a new price')
        print(price)
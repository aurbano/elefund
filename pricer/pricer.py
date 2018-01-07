from multiprocessing import JoinableQueue
import threading
import ccxt

from .price_worker import get_prices

class Pricer ():
    def __init__(self, market_store):
        self.market_store = market_store
        self.market_queue = JoinableQueue(maxsize=0)
        self.pool = []
        for i in range(10):
            worker = threading.Thread(target=get_prices, args=(self.market_queue, self.new_price, self.market_done))
            worker.setDaemon(True)
            worker.start()
            self.pool.append(worker)

    def start(self):
        pricer = threading.Thread(target=self.__run, args=())
        pricer.setDaemon(True)
        pricer.start()
        return pricer

    def __run(self):
        while True:
            self.populate_market_queue()
            self.market_queue.join()

    def populate_market_queue(self):
        for market_name in ccxt.exchanges:
            cctx_market = getattr(ccxt, market_name);
            market_api = cctx_market()
            self.market_queue.put({'name': market_name, 'api': market_api})
        
    def new_price(self, ticker):
        self.market_store.add_or_update_exchange_rate(ticker.from_currency, ticker.to_currency, ticker.exchange, ticker.ask)
        self.market_store.add_or_update_exchange_rate(ticker.to_currency, ticker.from_currency, ticker.exchange, 1 / ticker.bid)

    def market_done(self, market):
        self.market_queue.put(market)
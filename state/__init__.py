from graph import Market
from multiprocessing import Queue

updated_arcs = Queue(maxsize=1000) #shared queue between strats and graph
market = Market(updated_arcs)
fee_store = {}

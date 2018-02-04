import ccxt
import pprint
import logging

logger = logging.Logger('catch_all')

pp = pprint.PrettyPrinter(indent=4)


for market_name in ccxt.exchanges:
	cctx_market = getattr(ccxt, market_name);
	market_api = cctx_market()

	print(market_name)
	try:
		pprint(market_api.load_markets())
	except Exception as e:
		logger.error(e)

exit()


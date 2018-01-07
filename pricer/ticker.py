class MarketTicker():
    def __init__(self, from_currency, to_currency, exchange, ask, bid):
        self.to_currency = to_currency
        self.from_currency = from_currency
        self.exchange = exchange
        self.ask = ask
        self.bid = bid

    def __str__(self):
        return "From " + str(self.from_currency) + " to " + str(self.to_currency)

    def __repr__(self):
        return "From " + str(self.from_currency) + " to " + str(self.to_currency)

    def __eq__(self, other):
        return self.from_currency == other.from_currency \
               and self.to_currency == other.to_currency \
               and self.exchange == other.exchange
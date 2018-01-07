class Fee(object):
    def __init__(self, currency, fastestFee, halfHourFee, hourFee):
        self.currency = currency
        self.fastestFee = fastestFee
        self.halfHourFee = halfHourFee
        self.hourFee = hourFee

    def __str__(self):
        return "Fee for " + str(self.currency) + ": " + str(self.fastestFee)

    def __repr__(self):
        return "Fee for " + str(self.currency) + ": " + str(self.fastestFee)

    def __eq__(self, other):
        return self.currency == other.currency
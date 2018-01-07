class Fee(object):
    def __init__(self, currency, fastest, slowest):
        self.currency = currency
        self.fastest = fastest
        self.slowest = slowest

    def __str__(self):
        return "Fees for %s [Fastest %s] [Slowest %s]" % (self.currency, self.fastest, self.slowest)

    def __repr__(self):
        return "Fees for %s [Fastest %s] [Slowest %s]" % (self.currency, self.fastest, self.slowest)

    def __eq__(self, other):
        return self.currency == other.currency
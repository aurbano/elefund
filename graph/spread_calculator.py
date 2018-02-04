class SpreadCalculator(object):

    # fee_provider = FeeProvider()

    def calc(self, path):
        i = 1;
        current_amount = self.move_through(1, path[0]['arc'], path[0]['rate'])
        print ('Starting with %s. Rate = %d. After moving through amount = %d' % (
        path[0]['arc'], path[0]['rate'], current_amount))
        while i < len(path) - 1:
            current_amount = self.move_through(current_amount, path[i]['arc'], path[i]['rate'])
            print ('After moving through %s. Amount = %d' % (path[i]['arc'], current_amount))
            i += 1
        return current_amount

    def move_through(self, amount, arc, rate):
        # fee = fee_provider.get_fee(arc.from_currency, arc.to_currency, arc.exchange)
        # fee = 0.25 * amount
        fee = 0.1
        return (amount - fee) * rate

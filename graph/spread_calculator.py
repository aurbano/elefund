


class SpreadCalculator:

	fee_provider = FeeProvider()

	def calc(path):
		i = 1;
		current_amount = move_through(1, arc, rate)
		print ('Starting with ' + arc '. Rate = ' + rate + '. Amount after moving through = ' + current_amount)
		while (i < len(path) - 1):
			current_amount = move_through(current_amount, path[i].arc, path[i].rate)
			print('After moving through ' + arc + ', amount = ' + current_amount)
		return current_amount


	def move_through(amount, arc, rate):
		#fee = fee_provider.get_fee(arc.from_currency, arc.to_currency, arc.exchange)
		fee = 0.25 * amount
		return (amount - fee) * rate
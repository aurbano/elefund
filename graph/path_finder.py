




class Path_finder:
	hard_coded = [
		Arc('ETH', 'BTC', 'Kraken')
		Arc('BTC', 'XRP', 'Kraken')
		Arc('XRP', 'XRP', 'Kraken')
		Arc('XRP', 'BTC', 'Qryptos')
		Arc('BTC', 'ETH', 'Qryptos')
		Arc('ETH', 'ETH', 'Qryptos')
	]

	strategies = [
		hard_coded
	]


	def arc_updated(arc):
		for each in hard_coded:
			if each == arc:
				spread = calc_path_spread(hard_coded)
				subscriber.publish(hard_coded, spread)


	def calc_path_spread(path):
		dictionary = []
		for each_arc in path:
			current_rate = graph.get_rate(each_arc)
			dictionary[each_arc] = current_rate
		return spread_calculator.calc(dictionary)
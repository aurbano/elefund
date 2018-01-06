
class MockGraph(object):

	rates = {}

	def add_rate(self, arc, rate):
		self.rates[arc] = rate

	def get_rate(self, arc):
		return self.rates[arc]

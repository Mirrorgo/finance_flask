import backtrader as bt

class SmallCapStrategy(bt.Strategy):
	def __init__(self):
		self.sma = bt.indicators.SimpleMovingAverage(self.data, period=20)
	
	def next(self):
		if self.data.close[0] > self.sma[0]:
			self.buy()
		elif self.data.close[0] < self.sma[0]:
			self.sell()

import backtrader as bt

# 创建策略
class TestStrategy(bt.Strategy):

	def log(self, txt, dt=None):
		''' Logging function for this strategy'''
		dt = dt or self.datas[0].datetime.date(0)
		print('%s, %s' % (dt.isoformat(), txt))

	def __init__(self):
		# Keep a reference to the "close" line in the data[0] dataseries
		self.dataclose = self.datas[0].close

	def next(self):
		# Simply log the closing price of the series from the reference
		self.log('Close, %.2f' % self.dataclose[0])

		if self.dataclose[0] < self.dataclose[-1]:
		# current close less than previous close

			if self.dataclose[-1] < self.dataclose[-2]:
				# previous close less than the previous close

				# BUY, BUY, BUY!!! (with all possible default parameters)
				self.log('BUY CREATE, %.2f' % self.dataclose[0])
				print('股票总值: %.2f, 资金量: %.2f' % (self.broker.getvalue(), self.broker.getcash()))
				# print(self.broker.getposition(data=None))
				# print(self.broker.getposition())
				# cerebro.broker.getvalue()
				self.buy()

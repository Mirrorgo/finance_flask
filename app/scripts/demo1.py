# 暂时用来测试策略，之后会改成通用的函数接口
import backtrader as bt
import pandas as pd
import os


if __name__ == '__main__':

	# 初始化模型
	cerebro = bt.Cerebro()
	# 设定初始资金
	cerebro.broker.setcash(100000.0)

	# 策略执行前的资金
	print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

	# 加载离线数据文件
	fileName="000001.XSHE.csv"
	filePath = os.path.join(os.path.abspath(os.curdir),"app","scripts","data",fileName)
	data = pd.read_csv(filePath)  # 替换为你的离线数据文件路径

	# 转换数据为适用于 Backtrader 的格式
	data['datetime'] = pd.to_datetime(data['datetime'])
	data = data.set_index('datetime')
	data = bt.feeds.PandasData(dataname=data)

	# 创建策略
	class TestStrategy(bt.Strategy):

		def log(self, txt, dt=None):
			''' Logging function for this strategy'''
			dt = dt or self.datas[0].datetime.date(0)
			print('%s, %s' % (dt.isoformat(), txt))

		# def notify_trade(self, trade):
		# 	if not trade.isclosed:
		# 		return
		# 	print('股票总值: %.2f, 资金量: %.2f' % (self.broker.getvalue(), self.broker.getcash()))

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


	class SmallCapStrategy(bt.Strategy):
		def __init__(self):
			self.sma = bt.indicators.SimpleMovingAverage(self.data, period=20)
		
		def next(self):
			if self.data.close[0] > self.sma[0]:
				self.buy()
			elif self.data.close[0] < self.sma[0]:
				self.sell()
	# 加载数据
	cerebro.adddata(data)

	# 加载策略
	cerebro.addstrategy(TestStrategy)
	# cerebro.addstrategy(SmallCapStrategy)

	cerebro.run()

	# 策略执行后的资金
	print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
    
	# # 自定义策略
	# class MyStrategy(bt.Strategy):
	# 	def __init__(self):
	# 		# 初始化策略参数

	# 	def next(self):
	# 		# 策略逻辑


	# # 添加策略
	# cerebro.addstrategy(MyStrategy)

    





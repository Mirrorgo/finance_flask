import backtrader as bt
import pandas as pd
import os


# STAR: 通用策略
class SmallCapStrategy(bt.Strategy):
	def __init__(self,stockList):
		self.stocks = stockList
		self.data = {}
		for stock in self.stocks:
			print("name",stock)
			self.data[stock] = self.getdatabyname(stock)
		self.order = None  # 用于存储当前交易订单
		# STAR一些策略的内容
		self.sma = bt.indicators.SimpleMovingAverage(self.data[stock], period=20)
		
	def log(self, txt, dt=None):
		''' Logging function for this strategy'''
		dt = dt or self.datas[0].datetime.date(0)
		print('%s, %s' % (dt.isoformat(), txt))

	def notify_order(self, order):
		if order.status in [order.Submitted, order.Accepted]:
            # Buy/Sell order submitted/accepted to/by broker - Nothing to do
			return

        # Check if an order has been completed
        # Attention: broker could reject order if not enough cash
		if order.status in [order.Completed]:
			if order.isbuy():
				self.log(
					'BUY EXECUTED, Price: %.2f, Cost: %.2f, Comm %.2f' %
					(order.executed.price,
						order.executed.value,
						order.executed.comm))
				self.buyprice = order.executed.price
				self.buycomm = order.executed.comm
			else:  # Sell
				self.log('SELL EXECUTED, Price: %.2f, Cost: %.2f, Comm %.2f' %
							(order.executed.price,
							order.executed.value,
							order.executed.comm))
			print(order.data._name)
			self.bar_executed = len(self)

		elif order.status in [order.Canceled, order.Margin, order.Rejected]:
			self.log('Order Canceled/Margin/Rejected')

		self.order = None

	def next(self):
		# print("=====")
		for stock, data in self.data.items():
			# 限制资金不足时无法买入
			if self.should_buy(data):
				cash_available = self.broker.getcash()
				stake = self.sizer.getsizing(data,True) # 每次买入股票的量
				price = data.close[0]
				cost = stake*price
				# print(f"@{cost},{cash_available}")
				if cash_available >= cost:
					self.buy(data)
				else:
					print(f"资金不足，无法买入{stock}")

			elif self.should_sell(data):
				stake = self.sizer.getsizing(data,False) # 每次卖出股票的量
				if self.position and (self.getposition(data).size >= stake):
					self.sell(data)
				else:
					print(f"持仓不足，无法卖出{stock}")
		print('当前总资产价值: %.2f, 当前现金量: %.2f' % (self.broker.getvalue(), self.broker.getcash()))
		for stock, position in self.broker.positions.items():
			quantity = position.size
			avg_price = position.price
			print(f"持仓：{stock._name}，数量：{quantity}")
			# print(f"持仓：{stock._name}，数量：{quantity}，平均购买价格：{avg_price}")
			# 平均购买价格*数量!=当前持有的股票市值,so可能对不上

	def should_buy(self, data):
		# STAR编写你的买入条件判断逻辑
		# 返回 True 表示应该买入，否则返回 False
		# return data.close[0] > data.close[-1] and data.volume[0] > data.volume[-1]
		return data.close[0] > self.sma[0]

	def should_sell(self, data):
		# STAR编写你的卖出条件判断逻辑
		# 返回 True 表示应该卖出，否则返回 False
		# return self.position.size > 0 and data.close[0] < data.close[-1]
		return data.close[0] < self.sma[0]

# 程序入口
if __name__ == '__main__':
	# 创建 Cerebro 回测引擎✅
	cerebro = bt.Cerebro() 

	# 设置初始资金✅TODO:设置传入参数cash
	cerebro.broker.setcash(100000)
	
	# 设置每次的交易量
	# Add a FixedSize sizer according to the stake(国内1手是100股，最小的交易单位)
	cerebro.addsizer(bt.sizers.FixedSize, stake=100)
        
	# 策略执行前的资金✅
	print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

	stockList = ['000001.XSHE', '002829.XSH', '603707.XSHG'] 
	# 添加数据
	# for stock in cerebro.strategy.data.items():  
	for stock in stockList:  
		# 加载离线数据文件
		filePath = os.path.join(os.path.abspath(os.curdir),"app","scripts","data",(stock+".csv"))
		data = pd.read_csv(filePath)  # 替换为你的离线数据文件路径

		# 转换数据为适用于 Backtrader 的格式
		data['datetime'] = pd.to_datetime(data['datetime'])
		data = data.set_index('datetime')
		data = bt.feeds.PandasData(dataname=data)
		cerebro.adddata(data,name=stock)
	# 添加策略✅
	cerebro.addstrategy(SmallCapStrategy,stockList=stockList)

	# 运行回测
	cerebro.run()

	# 打印最终资金量
	print('总资产价值: %.2f, 现金量: %.2f' % (cerebro.broker.getvalue(), cerebro.broker.getcash()))

	# 总资产价值 = 现金+持有的股票市值
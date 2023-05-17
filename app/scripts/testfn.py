# 暂时用来测试策略，之后会改成通用的函数接口
import backtrader as bt
import pandas as pd
import os

from strategy1 import TestStrategy
# from app.scripts.strategy2 import SmallCapStrategy
# from app.scripts.strategy1 import MultiStrategy


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
	
	# 加载数据
	cerebro.adddata(data)

	# 加载策略
	cerebro.addstrategy(TestStrategy)

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


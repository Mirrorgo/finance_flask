import sys
import backtrader as bt
import pandas as pd
import os
import importlib
# from ..scripts.fn_28 import MyStrategy

def strategyLoader(strategy_class):
	# 创建 Cerebro 回测引擎✅
	cerebro = bt.Cerebro() 

	# 设置初始资金✅TODO:设置传入参数cash
	cerebro.broker.setcash(100000)
	
	# 设置每次的交易量
	# Add a FixedSize sizer according to the stake(国内1手是100股，最小的交易单位)
	cerebro.addsizer(bt.sizers.FixedSize, stake=100) # TODO 支持修改stake
        
	# 策略执行前的资金✅
	print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

	stockList = ['000001.XSHE', '002829.XSH', '603707.XSHG'] # 设置输入的内容
	# 添加数据
	for stock in stockList:  
		# 加载离线数据文件
		filePath = os.path.join(os.path.abspath(os.curdir),"app","scripts","data",(stock+".csv"))
		data = pd.read_csv(filePath)  

		# 转换数据为适用于 Backtrader 的格式
		data['datetime'] = pd.to_datetime(data['datetime'])
		data = data.set_index('datetime')
		data = bt.feeds.PandasData(dataname=data)
		cerebro.adddata(data,name=stock)
	# 添加策略✅
	cerebro.addstrategy(strategy_class,stockList=stockList)

	# 运行回测
	cerebro.run()

	# 打印最终资金量
	print('总资产价值: %.2f, 现金量: %.2f' % (cerebro.broker.getvalue(), cerebro.broker.getcash()))

	# 总资产价值 = 现金+持有的股票市值


# importlib封装的工具方法
def import_class(module_path, class_name):
    try:
        module = importlib.import_module(module_path)
        class_obj = getattr(module, class_name)
        return class_obj
    except ImportError:
        print(f"Failed to import module {module_path}")
    except AttributeError:
        print(f"Class {class_name} not found in module {module_path}")
        
def execute_method_from_module(module_path, method_name, *args, **kwargs):
    try:
        module = importlib.import_module(module_path)
        method = getattr(module, method_name)
        result = method(*args, **kwargs)
        return result
    except ImportError:
        print(f"Failed to import module {module_path}")
    except AttributeError:
        print(f"Method {method_name} not found in module {module_path}")
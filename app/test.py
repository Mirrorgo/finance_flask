import os
import sys
from utils.index import file_runner
import importlib
import sys



def import_class(module_path, class_name):
	# module = importlib.import_module(module_path, 'scripts')
	# # module = importlib.import_module("scripts.fn_28")
	# class_obj = getattr(module, class_name)

	# 创建模块规范对象
	spec = importlib.util.spec_from_file_location("fn_28", module_path)
	# 创建模块对象
	module = importlib.util.module_from_spec(spec)
	# 将模块对象添加到sys.modules中
	sys.modules[spec.name] = module
	# 执行模块中的代码
	spec.loader.exec_module(module)
	# 现在你可以使用module来访问导入的模块中的类、函数等
	# 访问类
	class_obj = module.MyStrategy
	return class_obj


# module_path=".fn_28"

# 指定要导入的文件路径
module_path = os.path.join(os.path.abspath(os.curdir),"app","scripts",f"fn_{28}.py")

print("module_path",module_path)
class_name = "MyStrategy"  # 输入要引入的类名称
strategy_class = import_class(module_path, class_name)
print(strategy_class,"strategy_class")





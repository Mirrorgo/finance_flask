from utils.index import *


path = get_path("testfn")
result = file_runner(path)
# result =file_reader(path)
print(result,"hello")


# result2 =  file_updater(path,"print('快乐嗷嗷嗷啊')")
# print(result2,"happy")
# print(get_sys_code())
# posix , nt , java， 对应linux/windows/java虚拟机

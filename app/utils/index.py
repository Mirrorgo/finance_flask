import subprocess
import json
import os
from .strategy import strategyLoader

test_file_path = "./app/scripts/test.py"


def test_fn(a, *args, b):
    print(a, *args, b)

# posix,nt,java， 对应linux/windows/java虚拟机
def get_sys_code():
    if(os.name== "nt"): 
        return "gbk"
    return "utf-8"


def file_runner(path, *args):
    # strategyLoader("28")
    result = subprocess.run(["python", path, *args],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        lines = result.stdout.decode(get_sys_code()).splitlines()
        obj = {
            "result":eval(lines[0]),
            "dates":eval(lines[1]),
            "endValue":eval(lines[2]),
            "yieldRate":eval(lines[3]),
            "info":"运行成功"
        }
        return obj
        # return json.dumps(obj=obj)
    else:
        print(result.stderr.decode(get_sys_code()))
        obj = {
            "info":result.stderr.decode(get_sys_code()) # 传递的报错
        }
        return obj


def file_reader(path):
    # path为以项目跟根目录为初始目录的相对路径
    file_content = ""
    with open(path, 'r',encoding='utf-8') as f:  # with方式可以避免没有关闭资源文件产生错误
        # print ("文件名为: ", f.name)
        # print("读取的数据为:")
        file_content = f.read()
        # print(file_content)
    return file_content


def file_updater(path, file_content):
    with open(path, 'w',encoding='utf-8') as f:  # with方式可以避免没有关闭资源文件产生错误
        f.write(file_content)
    return True


def result_wrapper(result):
    # TODO　转成枚举的形式,比如result_wrapper.success, result_wrapper.failure
    response = {}
    response["code"] = 20000
    response["message"] = "success"
    response["data"] = result
    return json.dumps(response)


def get_path(fileName):
    # return "./app/scripts/"+fileName+".py"
    # 这样应该可以避免系统差异造成的路径问题
    return os.path.join(os.path.abspath(os.curdir),"app","scripts",f"fn_{fileName}.py")



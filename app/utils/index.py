import subprocess
import json
import os

test_file_path = "./app/scripts/test.py"


def test_fn(a, *args, b):
    print(a, *args, b)


def file_runner(path, *args):
    result = subprocess.run(["python3", path, *args],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        print(result.stdout.decode())
        return result.stdout.decode()
    else:
        print(result.stderr.decode())
        return result.stderr.decode()


def file_reader(path):
    # path为以项目跟根目录为初始目录的相对路径
    file_content = ""
    with open(path, 'r') as f:  # with方式可以避免没有关闭资源文件产生错误
        # print ("文件名为: ", f.name)
        # print("读取的数据为:")
        file_content = f.read()
        # print(file_content)
    return file_content


def file_updater(path, file_content):
    with open(path, 'w') as f:  # with方式可以避免没有关闭资源文件产生错误
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
    return os.path.join(os.path.abspath(os.curdir),"app","scripts",(fileName+".py"))


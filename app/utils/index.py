import subprocess
import json
test_file_path = "./app/scripts/test.py"

def file_runner(path):
    result = subprocess.run(["python3", path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        print(result.stdout.decode())
        return result.stdout.decode()
    else:
        print(result.stderr.decode())


def file_reader(path):
	# path为以项目跟根目录为初始目录的相对路径
	file_content = ""
	with open(path, 'r') as f: # with方式可以避免没有关闭资源文件产生错误
		# print ("文件名为: ", f.name)
		# print("读取的数据为:")
		file_content = f.read()
		# print(file_content)	
	return file_content


def result_wrapper(result):
    # TODO　转成枚举的形式,比如result_wrapper.success, result_wrapper.failure
	response={}
	response["code"] = "20000"
	response["message"] = "success"
	response["data"]=result
	return json.dumps(response)
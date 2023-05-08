import sys
from flask import Flask
import subprocess
import json
# 引入自定义的工具函数
from utils.index import *

app = Flask(__name__)

def script_runner(cmd):
    res_mark = '[res_json]'
    subp = subprocess.Popen(cmd, encoding='utf-8', stdout=subprocess.PIPE)
    out, err = subp.communicate()
    res = None
    for line in out.splitlines():
        if line.startswith((res_mark, )):
            res = json.loads(line.replace(res_mark, '', 1))
            break
    return res

@app.route("/",methods=['GET'])
def hello_world():
	return "<p>Hello, World!</p>"

@app.get("/lwz/algorithm/file/get")
def get_file():
	# TODO 改成读取文件的接口
	result = file_reader(test_file_path)
	return result_wrapper(result)

@app.get("/lwz/algorithm/file/run")
def run():
	# cmd = 'python3 ./scripts/test.py'
	# cmd = "ls"
	# res = script_runner(cmd)
	# print(res)
	result = file_runner(test_file_path)
	print(result)
	return result_wrapper(result)




	
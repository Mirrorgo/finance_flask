from flask import Flask, request
# 引入自定义的工具函数
from utils.index import *

app = Flask(__name__)

@app.route("/",methods=['GET'])
def hello_world():
	return "<p>Hello, World!</p>"

@app.get("/lwz/algorithm/file/get")
def get_file():
	path =  request.args.get("path") # 获取path参数
	# TODO 改成读取文件的接口
	result = file_reader(path)
	return result_wrapper(result)

@app.get("/lwz/algorithm/file/run")
def run():
	path =  request.args.get("path") # 获取path参数
	# print("my args",request.args)
	result = file_runner(path,"1","22","333")
	return result_wrapper(result)


	
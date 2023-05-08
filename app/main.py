from flask import Flask, request
from flask_cors import CORS
# 引入自定义的工具函数
from utils.index import *

app = Flask(__name__)
CORS(app)

@app.route("/",methods=['GET'])
def hello_world():
	return "<p>Hello, World!</p>"

@app.get("/lwz/algorithm/file/get")
def get_file():
	# path =  request.args.get("path") # 获取path参数
	fileName = request.args.get('fileName')
	path = get_path(fileName)
	# TODO 改成读取文件的接口
	result = file_reader(path)
	return result_wrapper(result)

@app.get("/lwz/algorithm/file/run")
def run():
	fileName = request.args.get('fileName')
	path = get_path(fileName)
	# print("my args",request.args)
	# result = file_runner(path,"1","22","333") # 更多参数输入
	result = file_runner(path)
	return result_wrapper(result)


	
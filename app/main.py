from flask import Flask, request
from flask_cors import CORS
# 引入自定义的工具函数
from utils.index import *

app = Flask(__name__)
CORS(app)


@app.route("/", methods=['GET'])
def test_function():
    return "<p>Hello, World!</p>"


@app.get("/lwz/algorithm/file/get")
def get_file():
    # path =  request.args.get("path") # 获取path参数
    fileName = request.args.get('fileName')
    path = get_path(fileName)
    result = file_reader(path)
    return result_wrapper(result)


@app.get("/lwz/algorithm/file/run")
def run():
    fileName = request.args.get('fileName')
    path = get_path(fileName)
    # print("my args",request.args)
    result = file_runner(path,"1","22","333") # 更多参数输入
    # result = file_runner(path)
    return result_wrapper(result)


@app.post("/lwz/algorithm/file/update")
def update():
    content = request.json.get("content")
    fileName = request.json.get("fileName")
    path = get_path(fileName)
    result = file_updater(path, content)
    return result_wrapper(result)


@app.get("/lwz/algorithm/file/create")
# TODO post请求
def create():
    id = request.args.get('id')  # 算法Id
    path = get_path(id)
    # # 根据id新建文件
    # with open(path, 'w') as f:
    #     f.write('')
    source_file = open(get_path("template"), 'r')
    target_file = open(path, 'w')
    # 从源文件中读取内容并写入目标文件
    content = source_file.read()
    target_file.write(content)
    # 关闭文件
    source_file.close()
    target_file.close()

    return result_wrapper(True)

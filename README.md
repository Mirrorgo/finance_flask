```
./app/
├── __pycache__ 每次运行自动生成,不用管,可删
│   └── main.cpython-38.pyc 
├── main.py 主函数,程序入口
├── scripts 算法脚本文件
│   ├── 1.py 
│   ├── 2.py
│   ├── 28.py
│   ├── 31.py
│   ├── 32.py
│   ├── 33.py
│   ├── 34.py
│   ├── test.py
│   └── utils 其他算法脚本文件使用的通用工具函数文件夹
│       └── common.py 
└── utils
    ├── __pycache__ 每次运行自动生成,不用管,可删
    │   └── index.cpython-38.pyc 
    └── index.py 主函数main.py使用的工具函数
```

# 使用方法
## (Unix Bash)linux&macOS
* `. .venv/bin/activate`
* `export FLASK_APP="./app/main.py"`
<!-- * `pip install Flask`
* `pip install Flask-Cors` -->
* `flask run`
## (PowerShell)windows
* 删掉.venv文件夹
* `py -3 -m venv .venv`
* `.venv\Scripts\activate`
* `$env:FLASK_APP = ".\app\main.py"`
* `pip install Flask`
* `pip install Flask-Cors`
* `flask run`
  

> * https://flask.palletsprojects.com/en/2.3.x/installation/
> * https://flask.palletsprojects.com/en/1.1.x/cli/

---
# 用到的第三方库
* Flask
* Flask-Cors

---



连接数据库
* 通过请求spring-boot来获取数据

vscode选中虚拟环境中的Python以获得更优的代码提示体验
![](docs/images/2023-05-09-11-28-06.png)


TODO
前端携带日期参数发送请求到后端并运行脚本
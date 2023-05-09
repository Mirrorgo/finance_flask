```
├── README.md
├── app
│   ├── __init__.py
│   ├── api
│   │   ├── __init__.py
│   │   └── views.py
│   ├── auth
│   │   ├── __init__.py
│   │   ├── forms.py
│   │   ├── templates
│   │   │   └── auth.html
│   │   └── views.py
│   ├── extensions.py
│   ├── forms.py
│   ├── main
│   │   ├── __init__.py
│   │   ├── errors.py
│   │   ├── models.py
│   │   ├── templates
│   │   │   └── index.html
│   │   └── views.py
│   └── models.py
├── config.py
├── fabfile.py
├── manage.py
├── migrations
├── requirements
│   ├── common.txt
│   ├── dev.txt
│   └── prod.txt
└── unit_tests
```

# 使用方法
* `. .venv/bin/activate`
* `export FLASK_APP="./app/main.py"`
* `flask run`


连接数据库
* 通过请求spring-boot来获取数据

vscode选中虚拟环境中的Python以获得更优的代码提示体验
![](docs/images/2023-05-09-11-28-06.png)
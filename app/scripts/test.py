
import os
import subprocess
import json

def script_res(res_content):
    '''
    返回方法
    '''
    # 设置一个进程返回标记
    res_mark = '[res_json]'
    # 通过打印的方式返回
    print('{}{}'.format(res_mark, json.dumps(res_content, ensure_ascii=False)))
# ————————————————
# 版权声明：本文为CSDN博主「什么都干的派森」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/weixin_43721000/article/details/121764485
print('hello test')
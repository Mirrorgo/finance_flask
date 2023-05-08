
import json
import sys

def script_res(res_content):
    '''
    返回方法
    '''
    # 设置一个进程返回标记
    res_mark = '[res_json]'
    # 通过打印的方式返回
    print('{}{}'.format(res_mark, json.dumps(res_content, ensure_ascii=False)))
print('hello test')

args = sys.argv

def test_fn(a,*args):
    print(a,*args)
print(args,"wow")


test_fn("看看:","oooo",'1','2',"bbbb")
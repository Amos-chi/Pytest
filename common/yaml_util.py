# Time : 2023/2/2 10:00
import os

import yaml

def get_obj_path():
    return os.path.dirname(__file__).split('common')[0]         # 获取当前文件的路径

def read_yaml(yamldir):

    obj_path = get_obj_path()
    with open(obj_path + yamldir,'r',encoding='utf-8') as f:
        value = yaml.load(stream=f,Loader=yaml.FullLoader) # yanl.load 语法
        return value

if __name__ == '__main__':
    print(read_yaml(r'testcases\user_manage\user_info.yml'))
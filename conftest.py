# Time : 2023/2/1 14:16
import pytest

def read_yml():
    return ['cassie','qiangzhuang','jeo']

@pytest.fixture(scope='function',params=read_yml(),ids=['aa','bb','cc'],name='db')
def sql_func(request):
    #print(request.param)
    print('执行sql查询')
    yield request.param
    print('关闭数据库链接')
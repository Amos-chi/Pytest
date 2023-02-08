# Time : 2023/2/2 10:02
import pytest
from common.yaml_util import clean_yaml

proxies = {
    'http': 'http://127.0.0.1:4780',
    'https': 'http://127.0.0.1:4780'
}

@pytest.fixture(scope='function')
def sco_session1():
    print('sco_session ++++++++++++++++++++++++++++')
    yield
    pass
    print('用例测试结束')

if __name__ == '__main__':
    sco_session1()
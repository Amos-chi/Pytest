# Time : 2023/2/2 10:02
import pytest
import requests

from common.requests_util import RequestUtil

proxies = {
    'http': 'http://127.0.0.1:4780',
    'https': 'http://127.0.0.1:4780'
}

@pytest.fixture(scope='function')
def get_Authorization():
    url= 'https://api-staging.hitalentech.com:8888/user/api/v3/login'
    data = {
        'username' : 'amos.chi',
        'password' : 'ipg@95054'

    }
    resp = RequestUtil.session.request('post',url=url, json=data, proxies=proxies)
    token = resp.json()['credential']['access_token']
    Authorization = 'Bearer ' + token
    print('运行了get_Authorization---------------------------------------------')
    return Authorization

if __name__ == '__main__':
    get_Authorization()
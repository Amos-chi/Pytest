# Time : 2023/2/2 13:33
import pytest
import requests

from common.yaml_util import read_yaml


class TestIPGAPI:

    proxies = {
        'http': 'http://127.0.0.1:4780',
        'https': 'http://127.0.0.1:4780'
    }

    Authorization = ''

    def test_get_token(self,get_Authorization):
        TestIPGAPI.Authorization = get_Authorization


    @pytest.mark.parametrize('userinfo',read_yaml('testcases/ipg_api/data.yml'))
    def test_ipg_api(self,userinfo):
        print(userinfo['name'])
        url = userinfo['url']
        json = userinfo['data']
        headers = { 'Authorization': TestIPGAPI.Authorization}

        resp = requests.post(url,json=json,headers=headers,proxies=TestIPGAPI.proxies)

        assert resp.status_code == 200




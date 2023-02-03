# Time : 2023/2/2 13:33
import pytest
from common.requests_util import RequestUtil
from common.yaml_util import read_yaml, read_yamlfile
proxies = {
        'http': 'http://127.0.0.1:4780',
        'https': 'http://127.0.0.1:4780'
    }

class TestIPGAPI:


    @pytest.mark.parametrize('userinfo',read_yamlfile('/testcases/ipg_api/cases_parameter.yml'))
    def test_ipg_api(self,userinfo):
        print(userinfo['name'])
        url = userinfo['url']
        json = userinfo['data']
        headers = { 'Authorization': read_yaml('Authorization')}
        resp = RequestUtil().send_requests(method='post',url=url,json=json,headers=headers,proxies=proxies)

        assert resp.status_code == 200

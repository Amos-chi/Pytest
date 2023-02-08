# Time : 2023/2/2 13:33
import pytest
from common.requests_util import RequestUtil
from common.yaml_util import read_yaml, read_yamlfile

proxies = {
        'http': 'http://127.0.0.1:4780',
        'https': 'http://127.0.0.1:4780'
    }

class TestIPGAPI:


    @pytest.mark.parametrize('parameter',read_yamlfile('/testcases/companies/cases_parameter.yml'))
    def test_ipg_api(self,parameter):
        print(parameter['name'])
        url = parameter['url']
        json = parameter['data']
        headers = { 'Authorization': read_yaml('Authorization')}
        resp = RequestUtil().send_requests(method='post',url=url,json=json,headers=headers,proxies=proxies)

        assert resp.status_code == 200

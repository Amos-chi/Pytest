# Time : 2023/2/2 15:37
import requests


class RequestUtil:
    proxies = {
        'http': 'http://127.0.0.1:4780',
        'https': 'http://127.0.0.1:4780'
    }
    session = requests.session()  # 在单个用例内 共享token

    def send_requests(self,method,url,data,**kwargs):
        method = str(method).lower()
        resp = ''
        if method == 'get':
            resp = RequestUtil.session.request(method, url, params=data, **kwargs)
        elif method == 'post':
            resp = RequestUtil.session.request(method, url, json=data, **kwargs)

        return resp
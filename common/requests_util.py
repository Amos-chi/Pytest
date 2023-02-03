# Time : 2023/2/2 15:37
import requests


class RequestUtil:

    sess = requests.session()

    #封装 统一请求
    def send_requests(self,**kwargs):

        resp = RequestUtil.sess.request(**kwargs)

        return resp
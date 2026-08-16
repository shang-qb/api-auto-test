import requests
import json
import logging


class RequestUtil:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def send_request(self, method, url, **kwargs):
        """统一请求方法"""
        url = self.base_url + url
        logging.info(f"请求方式: {method}, 请求地址: {url}")
        if 'json' in kwargs:
            logging.info(f"请求体: {json.dumps(kwargs['json'], ensure_ascii=False)}")
        if 'params' in kwargs:
            logging.info(f"请求参数: {kwargs['params']}")

        response = self.session.request(method, url, **kwargs)

        logging.info(f"响应状态码: {response.status_code}")
        try:
            logging.info(f"响应数据: {response.text[:500]}")
        except Exception:
            pass
        return response

    def get(self, url, **kwargs):
        return self.send_request('GET', url, **kwargs)

    def post(self, url, **kwargs):
        return self.send_request('POST', url, **kwargs)

    def put(self, url, **kwargs):
        return self.send_request('PUT', url, **kwargs)

    def delete(self, url, **kwargs):
        return self.send_request('DELETE', url, **kwargs)

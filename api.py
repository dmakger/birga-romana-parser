import requests
from requests import Response

from models import _Model


class Api:
    def __init__(self):
        # self.parent_url = 'http://localhost:8000/api'
        self.parent_url = 'http://api.birgaromana.ru/api'

    def post_many(self, url: str, data: list[_Model]):
        print(f"Всего компаний: {len(data)}")
        for i in range(len(data)):
            self.post(url, data[i], i+1)

    def post(self, url: str, data: _Model, num=None):
        _url = self.get_url(url)
        print(data.body())
        response = requests.post(_url, json=data.body())
        self._show(response, num)

    def _show(self, response: Response, num=None):
        _num = ' ' if num is None else num
        if response.status_code == 201:
            print(f"{_num}. {response.status_code} {response.json()}")
        else:
            print(f"{_num}. Ошибка: {response.status_code}")

    def get_url(self, url: str):
        if url.startswith(self.parent_url):
            return url
        return f"{self.parent_url}/{url}"

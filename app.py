from api import Api
from config import URL_MOEX
from soup import Parser


class App:
    def __init__(self):
        self.body = []

    def start(self):
        parsing_data = self.get_parsing_data()
        self.send_api(parsing_data)

    def get_parsing_data(self):
        return Parser(URL_MOEX).start()

    def send_api(self, data):
        print('Сохранение на сервер')
        Api().post_many('stock/smart-add/', data)
        print('Успешно!')

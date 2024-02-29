from config import URL_MOEX
from soup import Parser


class App:
    def __init__(self):
        self.body = []

    def start(self):
        self.get_parsing_data()

    def get_parsing_data(self):
        data = Parser(URL_MOEX).start()
        for x in data:
            print(x.body())

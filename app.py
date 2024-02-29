from config import URL_SBER
from soup.soup import Parser


class App:
    def __init__(self):
        self.body = []

    def start(self):
        self.get_parsing_data()

    def get_parsing_data(self):
        Parser(URL_SBER).start()
        pass

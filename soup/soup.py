from bs4 import BeautifulSoup
import requests
import urllib.request as urllib2

from soup.typeWeb import TypeWEB


class Parser:
    def __init__(self, url: str, type_web: str = None ):
        self.url = url
        self.type_web = TypeWEB.BCS
        if type_web is not None:
            self.type_web = type_web

    def start(self):
        page = self.get_scheme()
        print(page)
        # Ищем все ссылки на странице
        # links = page.find_all('a')
        # for link in links:
        #     print(link.get('href'))

    def get_scheme(self):
        page = self.get_page()
        print(page)
        scheme = page
        if self.type_web == TypeWEB.BCS:
            scheme = page.find(id='chart')
        return scheme

    def get_page(self):
        proxy = urllib2.ProxyHandler({'http': '130.0.89.75:8080'})

        # Create an URL opener utilizing proxy
        opener = urllib2.build_opener(proxy)
        urllib2.install_opener(opener)
        request = urllib2.Request(self.url)
        request.add_header('User-Agent',
                           'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15')
        result = urllib2.urlopen(request)
        data = result.read()
        soup = BeautifulSoup(data, 'html.parser')
        return soup
        # ptag = soup.find('p', {'class', 'text-primary'}).text
        # print
        # ptag

        # response = requests.get(self.url)
        # html_content = response.text
        #
        # # Создаем объект BeautifulSoup
        # return BeautifulSoup(html_content, 'html.parser')



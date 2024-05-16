from typing import Optional

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

from models import Company, Stock, CompanyToStock


class Parser:
    def __init__(self, url: str):
        self.url = url

    def start(self):
        browser = self.get_browser()
        tables = self.get_tables_html(browser)
        browser.quit()
        return self.tables_to_objects(tables)

    def tables_to_objects(self, tables: list[str]):
        print('Форматирование таблицы')
        objects: list[CompanyToStock] = []
        for table in tables:
            soup = BeautifulSoup(table, 'html.parser')
            rows = soup.find_all('tr')
            for row in rows:
                cells = row.find_all('td')
                if len(cells) == 0:
                    continue
                cost = self.cell_to_float(cells[2])
                if cost is None:
                    continue
                company = Company(title=cells[1].text.strip(), code=cells[0].text.strip())
                stock = Stock(cost=cost)
                objects.append(CompanyToStock(company, stock))
        print('Успешно!')
        return objects

    def cell_to_float(self, cell) -> Optional[float]:
        cost = ''.join(cell.text.split()).replace(',', '.')
        if cost == '-':
            return None
        return float(cost)

    def get_tables_html(self, browser):
        is_exit = False
        table = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".ui-table__container table")))
        tables_html = []
        while not is_exit:
            tables_html.append(table.get_attribute('innerHTML'))

            all_buttons = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'div.UiPagination_paginationContainer_3SG3W')))

            buttons = all_buttons.find_elements(By.CSS_SELECTOR, 'button')
            button_next = buttons[-1]
            if button_next.get_attribute('disabled') is not None:
                is_exit = True
                continue
            button_next.click()
        return tables_html

        # Пропускает пользовательское соглашение

    def get_browser(self):
        options = Options()
        options.add_argument("--window-size=1000,800")  # Установите размер окна браузера
        browser = webdriver.Chrome(options=options)
        browser.get(self.url)
        self.skip_user_agreement(browser)
        return browser

    def skip_user_agreement(self, browser):
        # Ждем, пока не появится элемент с id='chart'
        element = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#disclaimer-modal .btn2-primary")))
        # Кликаем на элемент
        element.click()

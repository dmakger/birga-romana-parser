from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

import config

url = config.URL_SBER
browser = webdriver.Chrome()

# Открываем страницу
browser.get(url)


# Ждем, пока не появится элемент с id='chart'
wait = WebDriverWait(browser, 10)
element = wait.until(EC.presence_of_element_located((By.ID, 'disclaimer-modal')))
button = element.find_element(By.CLASS_NAME, 'btn2.btn2-primary')
button.click()

# Получаем HTML-код страницы
element = wait.until(EC.presence_of_element_located((By.ID, 'chart')))
html = browser.page_source

# Закрываем браузер
browser.quit()

# Создаем объект BeautifulSoup
with open('test.txt', 'w', encoding='utf-8') as f:
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)
    f.write(soup.prettify())

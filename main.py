import json
import sys
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

url = 'https://www.amazon.com.br/'+ sys.argv[1]
search = 'livro de programação'

option = Options()
option.headless = True
driver = webdriver.Firefox(options=option)

driver.get(url)

driver.find_element_by_id('twotabsearchtextbox').send_keys(search)
driver.find_element_by_id('nav-search-submit-button').click()

products_html = driver.find_elements_by_xpath("//div[@class='a-section a-spacing-medium']")
products_list = []

for i in range(len(products_html)):
    html_content = products_html[i].get_attribute('innerHTML')
    soup = BeautifulSoup(html_content, 'lxml')
    
    title = soup.find('span', class_='a-size-base-plus a-color-base a-text-normal')
    image = soup.find('img', class_='s-image')
    price = soup.find('span', class_='a-price-whole')
    decimal = soup.find('span', class_='a-price-fraction')
    currency = soup.find('span', class_='a-price-symbol')

    products_list.append({
        'title': title.text if title else '',
        'image': image['src'] if image else '',
        'price':  price.text + decimal.text if price else '',
        'currency': currency.text if currency else ''
    })

driver.quit()

with open('data.json', 'w') as data:
    json.dump(products_list, data, indent=4, ensure_ascii=False)

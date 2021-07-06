from selenium import webdriver
from selenium.common import exceptions as selenium_err
from selenium.webdriver.firefox.options import Options

# Setting web driver options
option = Options()
option.headless = True

def perform_search(search):
    driver = webdriver.Firefox(options=option)
    url = 'https://www.amazon.com.br/'
    driver.get(url)

    try:
        # Send search to Amazon's search bar
        driver.find_element_by_id('twotabsearchtextbox').send_keys(search)
        #Clicks to perform search
        driver.find_element_by_id('nav-search-submit-button').click()
    except selenium_err.NoSuchElementException:
        raise Exception("Error: no such HTML element")
    else:
        return driver
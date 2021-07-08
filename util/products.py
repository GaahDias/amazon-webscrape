from bs4 import BeautifulSoup

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

LOAD_SECONDS = 3

def product_template(soup):
    # Get data in the html with BeautifulSoup
    title = soup.find('span', class_='a-size-base-plus a-color-base a-text-normal')
    image = soup.find('img', class_='s-image')
    price = soup.find('span', class_='a-price-whole')
    decimal = soup.find('span', class_='a-price-fraction')
    currency = soup.find('span', class_='a-price-symbol')

    # Passes html data to string and creates product object
    product = ({
        'title': title.text if title else '',
        'image': image['src'] if image else '',
        'price':  price.text + decimal.text if price else '',
        'currency': currency.text if currency else ''
    })
    
    return product

def get_page_data(driver):
    products_list = []
    
    try:
        # Wait for page to load
        WebDriverWait(driver, LOAD_SECONDS).until(EC.presence_of_element_located((By.XPATH, "//li[@class='a-selected']//a")))
        # Select products
        products_html = driver.find_elements_by_xpath("//div[@class='a-section a-spacing-medium']")
    except NoSuchElementException:
        print("ERROR: Can't load page products")
        return "ERROR: Can't load page."
        
    # Loop through all products in page
    for i in range(len(products_html)):
        print(f'Getting {i} products')
        product_html = products_html[i].get_attribute('innerHTML')
        soup = BeautifulSoup(product_html, 'lxml')
        products_list.append(product_template(soup))
        
    return products_list

        
def get_products(driver):
    products_dict = {}
    
    # Loop through three pages, and get products info
    for i in range(3):
        try:
            print(f"PAGE {i}:")
            # Waits for page to load
            WebDriverWait(driver, LOAD_SECONDS).until(EC.presence_of_element_located((By.XPATH, "//li[@class='a-last']//a")))
            next_page = driver.find_element_by_xpath("//li[@class='a-last']//a")
        except (TimeoutException, NoSuchElementException):
            print("ABORTING: Page loading took too much time.")
            next_page = False
            return "ERROR: Can't load page."
        finally:
            products_dict[f'page{i+1}'] = get_page_data(driver)
            if next_page:
                next_page.click()
            else:
                break
        
    print('Quitting application...')
    driver.quit()
    return products_dict
            
        
def get_products_by_page(driver, page):
    products_dict = {}
    page_index = ''
    
    if page > 5:
        page = 5
    
    while page_index != str(page):
        try:
            # Wait for page to load
            WebDriverWait(driver, LOAD_SECONDS).until(EC.presence_of_element_located((By.XPATH, "//li[@class='a-last']//a")))
            # Get page selector info
            next_page = driver.find_element_by_xpath("//li[@class='a-last']//a")
            page_index = driver.find_element_by_xpath("//li[@class='a-selected']//a").text
        except (TimeoutException, NoSuchElementException):
            print("ABORTING: Page loading took too much time.")
            next_page = False
            return "ERROR: Can't load page."
        finally:
            # Check if there's a next page, if not, quits driver and returns the dict
            if next_page:
                next_page.click()

    products_dict[f'page{page_index}'] = get_page_data(driver)
      
    print('Quitting application...')
    driver.quit()
    return products_dict
    
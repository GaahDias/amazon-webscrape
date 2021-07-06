from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import exceptions as selenium_err
from selenium.webdriver.firefox.options import Options

# Setting web driver options
option = Options()
option.headless = True

def perform_initial_search(search):
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
        
def get_products(search, **kwargs):
    products_list = []
    driver = perform_initial_search(search)
    
    # Loop through pages
    for i in range(kwargs['pages'] if kwargs else 10):
        # Sleep so the page can load
        sleep(0.85)
        
        try:
            # Get next page element
            next_page = driver.find_element_by_xpath("//li[@class='a-last']//a")
        except:
            print("Last page")
            next_page = False
        finally:
            # Getting container with products data, and adding a new 'page' to products_list
            products_html = driver.find_elements_by_xpath("//div[@class='a-section a-spacing-medium']")
            products_list.append([])

            # Loop through all products in page
            for j in range(len(products_html)):
                print(f"PAGE {i}: Getting {j} products")
                html_content = products_html[j].get_attribute('innerHTML')
                soup = BeautifulSoup(html_content, 'lxml')
                
                products_list[i].append(product_template(soup))
            # Check if there's a next page, if not, quits driver and returns the list
            if next_page:
                next_page.click()
            else:
                break
            
    driver.quit()
    return products_list

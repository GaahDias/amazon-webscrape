from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

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

def get_page_data(driver, url):
    driver.get(url)
    products_list = []
    # Getting container with products data, and adding a new 'page' to products_list
    products_html = driver.find_elements_by_xpath("//div[@class='a-section a-spacing-medium']")

    # Loop through all products in page
    for i in range(len(products_html)):
        print(f'Getting {i} products')
        html_content = products_html[i].get_attribute('innerHTML')
        soup = BeautifulSoup(html_content, 'lxml')
        
        products_list.append(product_template(soup))
        
    return products_list

        
def get_products(driver, **kwargs):
    products_dict = {}
    
    # Loop through pages
    for i in range(kwargs['pages'] if kwargs else 10):
        # Sleep so the page can load
        driver.implicitly_wait(1)
        
        try:
            # Get next page element
            next_page = driver.find_element_by_xpath("//li[@class='a-last']//a")
        except Exception:
            print("WARNING: Last page")
            next_page = False
        finally:
            # Check if there's a next page, if not, quits driver and returns the dict
            if next_page:
                driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't') 
                products_dict[f'page{i+1}'] = get_page_data(driver, next_page.get_attribute("href"))
            else:
                break
            
    print('Quitting application...')
    driver.quit()
    return products_dict
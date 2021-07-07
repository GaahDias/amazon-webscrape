import json
import sys
from util.products import get_products
from util.search import perform_search

if __name__ == "__main__":
    driver = perform_search(sys.argv[1])
    products = get_products(driver, pages=3)

    with open('data.json', 'w') as data:
        json.dump(products, data, indent=4, ensure_ascii=False)

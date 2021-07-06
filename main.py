import json
import sys
from util.products import get_products

products = get_products(sys.argv[1])

with open('data.json', 'w') as data:
    json.dump(products, data, indent=4, ensure_ascii=False)

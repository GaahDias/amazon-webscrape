import json
from flask import Flask, jsonify

from util.products import get_products_by_page, get_products
from util.search import perform_search

app = Flask(__name__)

@app.route("/search-product/<name>")
def products(name):
    driver = perform_search(name)
    products = get_products(driver)
    
    return jsonify(products)

@app.route("/search-product/<name>/<int:page>")
def products_by_page(name, page):
    driver = perform_search(name)
    products = get_products_by_page(driver, page)
    
    return jsonify(products)
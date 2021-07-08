# API: Amazon Web Scraping

### Simple webscrape for getting data about Amazon products. Made with Selenium (using firefox webdriver), BeautifulSoup, and Flask.

### The API:
I've done two possible routes for the API, a more generic one for getting data of the first three pages, and another one for searching the products on a specific page. The limit for the second one is **five pages.**

> /search-product/*name* (Will return data of the first 3 pages)

> /search-product/*name*/*page* (Will return data from the page of your choice)

The returned json should look something like this:

```json

{
  "page1": [
    {
      "currency": "R$",
      "image": "https://m.media-amazon.com/images/I/61fphdlA-kS._AC_UL320_.jpg",
      "price": "149,99",
      "title": "heyaa Adaptador Bluetooth compatível com Switch/Lite/PS4/PS5, Transmissor de áudio sem fio BT 5.0 com baixa latência USB C para A Conversor para          fones de ouvido Bluetooth Fones de ouvido"
    },
    {
      "currency": "R$",
      "image": "https://m.media-amazon.com/images/I/619Kosxok1S._AC_UL320_.jpg",
      "price": "2.799,00",
      "title": "Console PlayStation 4 Mega Pack 18 - Ghost of Tsushima, God of War e Ratchet & Clank"
    },
```

It's also important to notice that I'm searching on **amazon.com.br**, not **amazon.com**.

### How to execute:

Install the dependencies:
> pip install lxml bs4 selenium flask

Also, for running the firefox webdriver, you must install geckodriver:
> `wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz`

> `tar -xvzf geckodriver*`

> `chmod +x geckodriver`

> `sudo mv geckodriver /usr/local/bin/`

Then, just run with:
> `flask run`

After that, you can test the API on your browser, Insomnia, or via console with:
>`curl address/search-product/name/page`  

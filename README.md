# Amazon WS

### Simple webscrape for getting data about Amazon products. Made with Selenium (using firefox webdriver), and BeautifulSoup

### How to execute:

Install the dependencies:
> pip install lxml bs4 selenium

Also, for running the firefox webdriver, you must install geckodriver:
> wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz

> tar -xvzf geckodriver*

> chmod +x geckodriver

> sudo mv geckodriver /usr/local/bin/

Then, just run it with:
> python main.py

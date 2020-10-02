from bs4 import BeautifulSoup
import requests

url = "http://www.cbr.ru/scripts/XML_daily.asp"
page = requests.get(url)
soup = BeautifulSoup(page.text, "lxml").find_all('valute')

for i in soup:
    numcode = i.find('numcode').text
    charcode = i.find('charcode').text
    name = i.find('name').text
    value = i.find('value').text
    if(numcode == '344'):
        print(numcode, " ", charcode, " ", name, " ", value)

from time import sleep
from helium import * 
from bs4 import BeautifulSoup

url = 'https://nordvpn.com/servers/tools/'
browser = start_chrome(url, headless=True)
sleep(1)
soup = BeautifulSoup(browser.page_source, 'html.parser')

server = (soup.find('h5', {'class': 'Title mb-3'}).text)

print(server)

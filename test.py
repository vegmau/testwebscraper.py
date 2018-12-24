#!/usr/bin/env python
# from selenium import webdriver as driver
from bs4 import BeautifulSoup as soup
from requests_html import HTMLSession
from tqdm import tqdm
from time import time
import json
import sys

# setting program launch/start time so we can record program execution duration
st_time = time()

# setting some basic starting vars
url = r'https://www.alternate.nl/html/listings/1472811138409?tk=7&lk=94962&page=1&size=40&showFilter=true'
dict = {}

# The selenium way.. (slower)
# def req_web:
#     global sauce
#     web = driver.Firefox()
#     web.get(url=url)
#     sauce = soup(web.page_source, features='lxml')


# the request-html way.. (faster)
def req_web(url):
    session = HTMLSession()
    req = session.get(url)
    req.html.render
    sauce = soup(req.html.html, features='lxml')
    return sauce


def read_page():
    containers = sauce.find_all("div", {"class":"listRow"})
    for e, container in enumerate(containers):
        container = container
    return container

sauce = req_web(url)
container = sauce.find_all('div', {'class':'listRow'})
# for i, y in tqdm(enumerate(sauce.find_all('a', href=True))):
#      dict.update({'link{}'.format(i):y['href']})

with open('data.json', 'w') as json_file:
    jdict = json.dumps(dict)
    json_file.write(jdict)


with open('data.json', 'r') as json_file:
    dict = json_file.read()

print(dict)

# printing program exection duration before ending program
print('Program execution duration is {} seconds..'.format(time()-st_time))

# ONLY FOR SELENIUM WEBDRIVER:
# close this webdriver browser instance
# web.close()
# # closes all webdrivers gracefully and ends all driver processes.
# web.quit()

# exit progam
sys.exit()

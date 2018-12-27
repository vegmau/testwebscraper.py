#!/usr/bin/env python
# from selenium import webdriver as driver
from bs4 import BeautifulSoup as soup
from requests_html import HTMLSession
from multiprocessing import Pool
from tqdm import tqdm
from time import time
import jsonpy
import sys


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
    global containers
    containers = sauce.find_all("div", {"class":"listRow"})
    with open("page.html", "w") as page:
        page.write(str(containers))


def get_items(containers):
    data = open("data.json", "w")
    for container in tqdm(containers):
        container.find("span", {"class":"name"})
        print(container)

    data.close()


if __name__ == "__main__":
    # setting program exection start time so we can record program execution duration
    st_time = time()
    # setting some basic starting vars
    url = r'https://www.alternate.nl/html/listings/1472811138409?tk=7&lk=94962&page=1&size=40&showFilter=true'
    dict = {}
    lst = []

    sauce = req_web(url)
    read_page()

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

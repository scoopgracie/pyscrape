#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
class Page:
    def __init__(self, soup, request):
        self.page = soup
        self.request = request

caching = True
__cache = {}
def get(url):
    if caching and url in __cache.keys():
        return __cache[url]
    else:
        request = requests.get(url)
        soup = BeautifulSoup(request.text, features='lxml')
        response = Page(soup, request)
        if caching:
            __cache[url] = response
        return response

def empty_cache():
    global __cache
    __cache = {}

#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
class Page:
    def __init__(self, soup, request):
        self.page = soup
        self.request = request

caching = True
__cache = {}
def get(url, use_cache = True):
    if caching and use_cache and url in __cache.keys():
        return __cache[url]
    else:
        request = requests.get(url)
        soup = BeautifulSoup(request.text, features='lxml')
        response = Page(soup, request)
        if caching and use_cache:
            __cache[url] = response
        return response


def uncache(url):
    global __cache
    del __cache[url]


def empty_cache():
    global __cache
    __cache = {}

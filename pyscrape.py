#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
class Page:
    '''Page - Page.page = beautiful soup object; Page.request = requests request object'''
    def __init__(self, soup, request):
        self.page = soup
        self.request = request

caching = True
__cache = {}
def get(url, use_cache = True):
    '''get(url, use_cache=True) - get url, skip cache if use_cache == False, will probably raise a Beautiful Soup or Requests exception on error'''
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
    '''uncache(url) - remove url from the cache, raise ValueError if page not in cache'''
    global __cache
    del __cache[url]


def empty_cache():
    '''empty_cache() - empty the cache'''
    global __cache
    __cache = {}

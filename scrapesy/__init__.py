'''scrapesy - easy web scraper and file downloader
provides downloading with cache as well as parsing in get() function
'''
import requests
from bs4 import BeautifulSoup

class Page:
    '''Page - a Web page
    Page.page is a BeautifulSoup object
    Page.request is a requests request object
    '''
    def __init__(self, soup, request):
        self.page = soup
        self.request = request


caching = True
__cache = {}


def cache_check(url):
    ''' cache_check(url) - check if url should be cached
    overwrite for custom cache control (return True if url should be cached,
    False otherwise)
    '''
    return True #By default, cache everything


def get(url, use_cache = True):
    '''get(url, use_cache=True) - get url, skip cache if use_cache == False, will probably raise a Beautiful Soup or Requests exception on error'''
    if caching and use_cache and cache_check(url) and url in __cache.keys():
        return __cache[url]
    else:
        request = requests.get(url)
        soup = BeautifulSoup(request.text, features='lxml')
        response = Page(soup, request)
        if caching and use_cache and cache_check(url):
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

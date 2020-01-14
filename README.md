# pyscrape
[![Build Status](https://api.travis-ci.com/scoopgracie/pyscrape.svg?branch=master)](https://travis-ci.com/scoopgracie/pyscrape)

Easy and Pythonic way to get and parse a Web page

## Usage

To get a `Page` object, use `pyscrape.get(url)`. The `Page` object has two
properties, `page` and `request`. `page` is a `BeautifulSoup` object.
`request` is a Requests `Response` object.

### Caching

By default, PyScrape implements a cache, allowing for near-instantaneous
results on pages that have been requested previously. This cache operates
automatically, and it operates transparently to any code that does not
specifically interact with it. It is possible to use PyScrape without any
understanding of the cache.

However, it is possible to disable the cache. Simply run `pyscrape.caching =
False`. To re-enable it, use `pyscrape.caching = True`.

To empty the cache, call `pyscrape.empty_cache()`.

TO remove a single page from the cache, call `pyscrape.uncache(url)`.

Run `demo.py` for a demonstration of the impact of the cache.

## Requirements

* Beautiful Soup 4
* Requests
* Python 3 (it may work on 2.7, but is not tested)

# pyscrape
Easy and Pythonic way to get and parse a Web page

## Usage

To get a `Page` object, use `pyscrape.get(url)`. The `Page` object has two
properties, `page` and `request`. `page` is a `BeautifulSoup` object.
`request` is a Requests `Response` object.

### Caching

By default, PyScrape implements a cache, allowing for near-instantaneous
results on pages that have been requested previously. However, it is possible
to disable this cache. Simply run `pyscrape.caching = False`. To re-enable it,
use `pyscrape.caching = True`. Run `demo.py` for a demonstration of the cache.

## Requirements

* Beautiful Soup 4
* Requests
* Python 3 (it may work on 2.7, but is not tested)

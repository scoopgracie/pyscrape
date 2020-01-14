#!/usr/bin/env python3
import pyscrape
expect = 'ScoopGracie'

print('fetching first time')
a = pyscrape.get('https://scoopgracie.com/').page.h1.string
if a != expect:
    print('got {} (expected {})'.format(a, expect))
    exit(1)

print('fetching again')
b = pyscrape.get('https://scoopgracie.com/').page.h1.string
if b != expect:
    print('got {} (expected {})'.format(b, expect))
    exit(1)

print('skipping cache and fetching')
c = pyscrape.get('https://scoopgracie.com/', use_cache=False).page.h1.string
if c != expect:
    print('got {} (expected {})'.format(c, expect))
    exit(1)

print('uncaching and fetching')
pyscrape.uncache('https://scoopgracie.com/')
if pyscrape.__cache != {}:
    print('cache is not empty after uncache')
    exit(1)
d = pyscrape.get('https://scoopgracie.com/').page.h1.string
if d != expect:
    print('got {} (expected {})'.format(d, expect))
    exit(1)


print('disabling cache and fetching')
pyscrape.caching = False
e = pyscrape.get('https://scoopgracie.com/').page.h1.string
if e != expect:
    print('got {} (expected {})'.format(e, expect))
    exit(1)

print('clearing cache')
pyscrape.empty_cache()
if pyscrape.__cache != {}: #Note: this is poor practice, don't interact
    #directly with __cache ouside test scripts
    print('cache is not empty')
    exit(1)

print('setting selective caching to none and fetching')
pyscrape.caching = True
old_cache_check = pyscrape.cache_check
def return_false(url):
    return False
pyscrape.cache_check = return_false
f = pyscrape.get('https://scoopgracie.com/').page.h1.string
if pyscrape.__cache != {}:
    print('cache is not empty')
    exit(1)
if f != expect:
    print('got {} (expected {})'.format(f, expect))
    exit(1)

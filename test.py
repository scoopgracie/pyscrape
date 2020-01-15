#!/usr/bin/env python3
import scrapesy
expect = 'ScoopGracie'

print('fetching first time')
a = scrapesy.get('https://scoopgracie.com/').page.h1.string
if a != expect:
    print('got {} (expected {})'.format(a, expect))
    exit(1)

print('fetching again')
b = scrapesy.get('https://scoopgracie.com/').page.h1.string
if b != expect:
    print('got {} (expected {})'.format(b, expect))
    exit(1)

print('skipping cache and fetching')
c = scrapesy.get('https://scoopgracie.com/', use_cache=False).page.h1.string
if c != expect:
    print('got {} (expected {})'.format(c, expect))
    exit(1)

print('uncaching and fetching')
scrapesy.uncache('https://scoopgracie.com/')
if scrapesy.__cache != {}:
    print('cache is not empty after uncache')
    exit(1)
d = scrapesy.get('https://scoopgracie.com/').page.h1.string
if d != expect:
    print('got {} (expected {})'.format(d, expect))
    exit(1)


print('disabling cache and fetching')
scrapesy.caching = False
e = scrapesy.get('https://scoopgracie.com/').page.h1.string
if e != expect:
    print('got {} (expected {})'.format(e, expect))
    exit(1)

print('clearing cache')
scrapesy.empty_cache()
if scrapesy.__cache != {}: #Note: this is poor practice, don't interact
    #directly with __cache ouside test scripts
    print('cache is not empty')
    exit(1)

print('setting selective caching to none and fetching')
scrapesy.caching = True
old_cache_check = scrapesy.cache_check
def return_false(url):
    return False
scrapesy.cache_check = return_false
f = scrapesy.get('https://scoopgracie.com/').page.h1.string
if scrapesy.__cache != {}:
    print('cache is not empty')
    exit(1)
if f != expect:
    print('got {} (expected {})'.format(f, expect))
    exit(1)

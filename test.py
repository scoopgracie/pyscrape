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
if a != expect:
    print('got {} (expected {})'.format(b, expect))
    exit(1)
print('disabling cache and fetching')
pyscrape.caching = False
c = pyscrape.get('https://scoopgracie.com/').page.h1.string
if a != expect:
    print('got {} (expected {})'.format(c, expect))
    exit(1)
print('clearing cache')
pyscrape.clear_cache()
if pyscrape.__cache != {}: #Note: this is poor practice, don't interact
    #directly with __cache ouside test scripts
    print('cache is not empty')
    exit(1)

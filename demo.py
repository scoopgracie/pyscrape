#!/usr/bin/env python3
import pyscrape
print('fetching first time')
print(pyscrape.get('https://scoopgracie.com/').page.h1.string)
print('fetching again')
print(pyscrape.get('https://scoopgracie.com/').page.h1.string)
print('disabling cache and fetching')
pyscrape.caching = False
print(pyscrape.get('https://scoopgracie.com/').page.h1.string)

#!/usr/bin/env python3
import scrapesy
print('fetching first time')
print(scrapesy.get('https://scoopgracie.com/').page.h1.string)
print('fetching again')
print(scrapesy.get('https://scoopgracie.com/').page.h1.string)
print('disabling cache and fetching')
scrapesy.caching = False
print(scrapesy.get('https://scoopgracie.com/').page.h1.string)

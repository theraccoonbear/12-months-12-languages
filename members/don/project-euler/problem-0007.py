#!/usr/bin/python
import math
import string
import euler

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

plist = []
n = 0

while len(plist) < 10001:
	n += 1
	if euler.isPrime(n):
		plist.append(n)
		
print plist[-1]
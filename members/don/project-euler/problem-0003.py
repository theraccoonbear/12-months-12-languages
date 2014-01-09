#!/usr/bin/python

# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
#
# http://en.wikipedia.org/wiki/Prime_factorization

import math

magic = 600851475143

primeStatus = {}

def isPrime(n):
	if not n in primeStatus: 
		if n % 2 == 0:
			primeStatus[n] = False
		else:
			upper = int(math.ceil(math.sqrt(n)))
			primeStatus[n] = True
			for i in range(upper, 1, - 1):
				if n % i == 0:
					primeStatus[n] = False
					break
	
	return primeStatus[n]


biggest = 0

for x in range(0, 10000):
	if isPrime(x):
		if magic % x == 0:
			biggest = x
			
print "Biggest: " + `biggest`


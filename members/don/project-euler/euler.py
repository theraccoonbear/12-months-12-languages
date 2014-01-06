#!/usr/bin/python
import math

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
	if not primeStatus[n]:
		for mult in range(2,10):
			primeStatus[mult*n] = False
	return primeStatus[n]

def listPrimes(start, end):
	primes = []
	for x in range(start, end + 1):
		if isPrime(x):
			primes.append(x)
	return primes


def isPalindrome(n):
	n = str(n);
	length = len(n);
	half = int(math.floor(length / 2))
	left = n[0:half];
	right = (n[length-half:length])[::-1]
	return left == right

def checkDiv(n):
	for d in range(1, 20):
		if n % d != 0:
			return False
	return True

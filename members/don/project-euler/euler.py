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
	return primeStatus[n]

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

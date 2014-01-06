#!/usr/bin/python

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import math
import string
import euler

small_primes = (2,3,5,7,11,13,17,19);

total = 1;
pf = list();
div_cnt = 1;
for_lcm = range(1,20);

# Iterate through each of the primes
for prime in small_primes:
	print "CHECKING PRIME: " + `prime`
	while (div_cnt != 0):
		div_cnt = 0;
		for i in range(0, len(for_lcm)):
			padded = `for_lcm[i]`.rjust(5)
			
			if (for_lcm[i] % prime == 0):
				print padded + ' factored by ' + `prime` + " to " + `(for_lcm[i] / prime)`
				div_cnt += 1
				for_lcm[i] /= prime;
			else:
				print padded + " not factorable"

		if (div_cnt > 0):
			print "\n ...again...\n"
			pf.append(prime)
		else:
			print `prime` + " COMPLETED";
	div_cnt = 1

for x in pf:
	total *= x

factors = ", ".join(str(x) for x in pf)

print "\nFactors: " + factors

print "\nAnswer: " + `total`;


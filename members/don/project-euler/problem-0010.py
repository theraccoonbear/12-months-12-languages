#!/usr/bin/python
import sys
import math
import string
import euler
import operator

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

primes = euler.listPrimes(1, 2000000)

print reduce(operator.add, primes, 1)
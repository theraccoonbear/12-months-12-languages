#!/usr/bin/python

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

import math
import euler


biggest = 0

for x in range(100, 999):
	for y in range(100, 999):
		candidate = x * y
		
		if candidate > biggest and euler.isPalindrome(candidate):
			biggest = candidate
			
print biggest
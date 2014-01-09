#!/usr/bin/python
import math
import string
import euler

#The sum of the squares of the first ten natural numbers is,
#
#1^2 + 2^2 + ... + 10^2 = 385
#The square of the sum of the first ten natural numbers is,
#
#(1 + 2 + ... + 10)^2 = 552 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
#
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

sum_of_squares = 0
square_of_sums = 0

for x in range(1, 101):
	sum_of_squares += math.pow(x, 2)
	square_of_sums += x

square_of_sums = math.pow(square_of_sums, 2)

diff = square_of_sums - sum_of_squares

print sum_of_squares
print square_of_sums
print diff
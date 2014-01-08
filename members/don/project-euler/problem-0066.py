#!/usr/bin/python
import sys
import math
import string
import euler
import operator

#Consider quadratic Diophantine equations of the form:
#
#x^2 - Dy^2 = 1
#
#For example, when D=13, the minimal solution in x is 649^2 - 13*180^2 = 1.
#
#It can be assumed that there are no solutions in positive integers when D is square.
#
#By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:
#
#3^2 - 2*22 = 1
#2^2 - 3*12 = 1
#9^2 - 5*42 = 1
#5^2 - 6*22 = 1
#8^2 - 7*32 = 1
#
#Hence, by considering minimal solutions in x for D <= 7, the largest x is obtained when D=5.
#
#Find the value of D <= 1000 in minimal solutions of x for which the largest value of x is obtained.

def testDiophantine(x, y, D):
	return math.pow(x, 2) - (D * math.pow(y, 2))

biggest = 0
D_at_biggest = 0
smallest = 10000

for D in range(1, 1000):
	smallest = 10000
	success = False
	for y in range(1, 1000):
		ysquared = math.pow(y, 2)
		dtimesysq = D * ysquared
		for x in range(1, 10000):
			xsquared = math.pow(x, 2)
			success = xsquared - dtimesysq == 1
			if success:
				if (x < smallest):
					smallest = x
					break
		if success:
			break
	if success:
		#print "Smallest x for D = " + `D` + ' is ' + `smallest`
		if (smallest > biggest):
			biggest = smallest
			D_at_biggest = D
			print "New biggest x is " + `biggest` + ' when D = ' + `D`
	if not D % 10:
		print D

print "D: " + `D_at_biggest`
#!/usr/bin/python
total = 0
last_fib = 1
current_fib = 2

while current_fib < 4000000:
    if current_fib % 2 == 0:
        total = total + current_fib
    tmp = current_fib
    current_fib = current_fib + last_fib
    last_fib = tmp
    
#for x in range(1, 1000):
 #   if x % 3 == 0 or x % 5 == 0:
  #      total = total + x
        
print total


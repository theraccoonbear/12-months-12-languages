'''002 Even Fibonacci Numbers

   add the even Fibonacci numbers less than 4,000,000
'''

a = 0
b = 1
total = 0

while b < 4000000:
    c = a + b
    a = b
    b = c
    if c % 2 == 0:
        total += c

print(total)

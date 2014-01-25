"""
10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

primes = [2]
sieve = list(range(3,500000, 2))
p = 3

while len(sieve) > 0:
    p = sieve[0]
    primes.append(p)
    sieve.pop(0)
    for x in sieve:
        if x % p == 0: sieve.remove(x)
    
    print(len(primes))
    
    if len(primes) == 10001: break
    

print(primes[-1])

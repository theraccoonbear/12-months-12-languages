import itertools

def isPalindrome(n):
    return str(n) == str(n)[::-1]

pairs = tuple(itertools.combinations_with_replacement(range(100,1000), 2))
palindromes = []


for n in reversed(pairs):
    p = n[0]*n[1]
    if isPalindrome(p):
        palindromes.append(p)

print(max(palindromes))

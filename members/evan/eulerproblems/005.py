import itertools

factors = list(range(1,21))

pairs = itertools.combinations(factors, 2)
 
products = []

for n in pairs:
    products.append(n[0]*n[1])

print(products)
print(max(products, key=products.count))

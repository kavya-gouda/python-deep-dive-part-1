l1 = [1, 2, 3]
l2 = [10, 20, 30]
l3 = [100, 200, 300]
def fact(n):
    return 1 if n <= 1 else n * fact(n - 1)
result = map(fact, l2)
print(list(result))

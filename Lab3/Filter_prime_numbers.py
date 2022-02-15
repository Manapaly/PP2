from function1 import is_prime
mylist = list(map(int, input().split()))
res = list(filter(lambda x: is_prime(x), mylist))
print(res)

import math

def IsItPrime(k):
    if k==1 or k==2 or k==3: return True
    if k%2 == 0: return False
    for i in range (2, k):
        if k % i == 0:
            return False
    return True

a, b = map(int, input().split())
if (IsItPrime(a) == True) and (b % 2 == 0) and a<500:
    print("Good job!")
else:
    print("Try next time!")
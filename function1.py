def grams_to_ounces(grams):
    return 28.3495231 * grams

def Fahrenheit_to_Celsius(temp):
    return (5/9)*(temp - 32)

def solve(numheads, numlegs):
    chicken = (4*numheads - numlegs)/2
    rabbits = (numlegs - 2*numheads)/2
    return (int(chicken), int(rabbits))

def is_prime(n):
    if n == 1: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(mylist):
    result = []
    for i in mylist:
        if is_prime(i):
            result.append(i)
    return result

from itertools import permutations
def all_permutation(s):
    perms = [''.join(i) for i in permutations(s)]
    return perms
    
def reversed_string(s):
    ml = s.split()
    result = ""
    for i in ml:
        result = i + " " + result 
    return result

# print(reversed_string('We are ready'))
def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i]==3 and nums[i+1]==3: return True
    return False

def spy_game(nums):
    res = []
    for i in nums:
        if i==0 or i==7: res.append(i)
    for i in range(2,len(res)):
        if res[i]==7 and res[i-1]==0 and res[i-2]==0: return True
    return False
import math
def volume_of_a_sphere(r):
    return (4/3) * math.pi * (r**3)
# print(volume_of_a_sphere(4))

def unique_element_of_list(mylist):
    dict = {}
    for i in mylist:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    result = []
    for k,v in dict.items():
        if v==1: result.append(k)
    return result
# print(unique_element_of_list([1,2,3,1,2,5,4,6,7,8,33,4,45,34,34,0,5]))
def polindrome(s):
    for i in range(int(len(s)/2)):
        if s[i] != s[len(s)-1-i]: return False
    return True
# print(polindrome('abba'))
def histogram(mylist):
    a = max(mylist)
    b = len(mylist)
    result = [[' ' for i in range(a)] for j in range(b)]
    # return result
    for i in range(b):
        for j in range(mylist[i]):
            result[i][j] = '*'
    for i in range(b):
        for j in range(a):
            print(result[i][j],end='')
        print()
# histogram([1,1,1])
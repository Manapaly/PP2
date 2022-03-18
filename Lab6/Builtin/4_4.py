from math import sqrt
from time import sleep
a = int(input())
b = int(input())


x = compile('sleep(b/1000)\nans = sqrt(a)','4_4.py','exec')
exec(x)
print(f'Square root of {a} after {b} miliseconds is {ans}')

#4 Python program that invoke square root function after specific milliseconds.

from time import sleep
from math import sqrt
a = int(input())
b = int(input())
sleep(b/1000)
print(f'Square root of {a} after {b} miliseconds is {sqrt(a)}')
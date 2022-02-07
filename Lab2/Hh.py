from math import sqrt

def distance(x1, y1, x2, y2):
    return sqrt((x2-x1)**2+(y2-y1)**2)

x0, y0 = map(int,input().split())
n = int(input())

list = []
for i in range(n):
    w = []
    x, y = map(int,input().split())
    myorder = "{} {}"
    w.append(distance(x, y, x0, y0))
    w.append(myorder.format(x, y))
    list.append(w)

for i in sorted(list):
    print(i[1])


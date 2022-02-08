n = int(input())
a = []
for i in range(n):
    b = []
    for j in range(n):
        b.append('#')
    a.append(b)

if n % 2 == 1:
    k = 1
    for i in range(len(a)):
        for j in range(len(a[i])-k):
            a[i][j]='.'
        k = k + 1
else:
    k = 1
    for i in range(len(a)):
        for j in range(k,len(a[i])):
            a[i][j]='.'
        k = k + 1

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j],end = '')
    print()
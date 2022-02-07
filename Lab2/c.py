n = int(input())
a = []
for i in range(n):
    b = []
    for j in range(n):
        b.append(0)
    a.append(b)
for i in range(len(a)):
    for j in range(len(a[i])):
        a[i][i] = i*i
        a[0][j] = j
        a[i][0] = i
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j],end = " ")
    print()
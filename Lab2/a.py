n = list(map(int,input().split()))
m = 0

for i in n:
    for j in range(m, m+n[m]+1):
        if m + n[m]  < n[j] + j:
            m = j
        if m + n[m] + 1 >= len(n):
            print(1)
            exit()
print(0)
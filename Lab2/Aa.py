
n = list(map(int,input().split()))
m = 0
for k in range(len(n)):
    for i in range(m, m+n[m] + 1):
        if m + n[m] >= len(n)-1:
            print(1)
            exit()
        if n[m] + m < n[i] + i:
            m = i
        

    
print(0)

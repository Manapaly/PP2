n = list(map(int,input().split()))
ok = False
for i in range(len(n)):
    if n[i]==0:
        cnt = 0
        for j in range(i):
            if (n[j] - n[i]) == (i - j) : cnt += 1
        if cnt == i: ok = True
        if n[i]==0 and n[i-1] == 1: ok = True
        if cnt == len(n)-1: ok = False
    
     
if ok == True: print(0)
else: print(1)
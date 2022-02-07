
n = list(map(int,input().split()))
n.append(0)
m = 0
cnt0 = 0
cnt = 0
ok = False
for i in range(m, len(n)):
    if n[i] == 0:
        cnt0 = cnt0 + 1
        for j in range(m, i):
            if i-n[j] != i-j:
                m = j
                cnt = cnt + 1
                ok = True
                break
            else: ok = False
if cnt0-1 == cnt : print("Yes")
else: print("No")
        
n = int(input())
mylist = []
def ff(s):
    cnt = 0
    cnt1 = 0
    cnt2 = 0
    for i in range(len(s)):
        if ord(s[i])>=48 and ord(s[i])<=57: cnt = 1
        if ord(s[i])>=65 and ord(s[i])<=90: cnt1 = 1
        if ord(s[i])>=97 and ord(s[i])<=122: cnt2 = 1
    if cnt == 1 and cnt1 == 1 and cnt2 == 1: return True 
    else: return False

for i in range(n):
    s = input()
    if(ff(s)==True) and s not in mylist:
        mylist.append(s)

print(len(mylist))
for i in sorted(mylist):
    print(i)
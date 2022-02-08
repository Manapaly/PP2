def ff(s,e):
    k = ""
    for i in range(len(s)-1, -1, -1):
        if s[i] != ' ': k = s[i] + k
        else:
            e.append(k) 
            k = ""
    e.append(k)
    return e

mylist = []
while True:
    s = input()
    e = []
    if s != '0':
        mylist.append(ff(s,e))
        e = []
    else:
        break
mylist.sort()
for i in mylist:
    print(*reversed(i))
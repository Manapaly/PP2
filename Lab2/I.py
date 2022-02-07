n = int(input())
mylist = []
results = []
for i in range(n):
    x = input()
    if x[0] == '1':
        mylist.append(x[2:len(x)])
    else:
        e = mylist[0]
        mylist.pop(0)
        results.append(e)
print(*results, end = " ")
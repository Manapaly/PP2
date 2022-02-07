
n = list(map(str, input().split()))
mylist = []
for i in n:
    if i[len(i)-1] == '.' or i[len(i)-1] == ',' or i[len(i)-1] == '?' or i[len(i)-1] == '!' or i[len(i)-1] == ':':
        i = i[0:len(i)-1]
        mylist.append(i)
    if i not in mylist:
        mylist.append(i)
print(len(mylist))
for i in sorted(mylist):
    print(i)

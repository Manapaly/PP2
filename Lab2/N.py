mylist = []

while True:
    n = int(input())
    if(n == 0): break
    mylist.append(n) 
    
result = []
for i in range(len(mylist)//2):
    result.append(mylist[i]+mylist[len(mylist) - 1 - i])
if(len(mylist) % 2 == 1):
    result.append(mylist[len(mylist)//2])
print(*result)
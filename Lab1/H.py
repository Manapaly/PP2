s=str(input())
c=str(input())
a = []
for i in range(len(s)):
    if s[i]==c:
        a.append(i)
if(len(a)>2):
    print(a[0], end = " ")
    print(a[len(a)-1])
else:
    for i in range(len(a)):
        print(a[i], end = " ")
  

        
s = input()
if ' ' not in s:
    b = int(input())
    a = int(s)
else:
    k = s.find(" ")
    a = int(s[0:k])
    b = int(s[k+1:len(s)])


a, b
c = []
d = 0
for i in range(a):
    c.append(b + 2*i)
for i in range(len(c)):
    d = d^(c[i])
print(d)
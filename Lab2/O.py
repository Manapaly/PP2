def ff(s):
    if s == 'ZER' : return 0
    if s == 'ONE' : return 1
    if s == 'TWO' : return 2
    if s == 'THR' : return 3
    if s == 'FOU' : return 4
    if s == 'FIV' : return 5
    if s == 'SIX' : return 6
    if s == 'SEV' : return 7
    if s == 'EIG' : return 8
    if s == 'NIN' : return 9
def gg(n):
    if n == '0' : return 'ZER'
    if n == '1' : return 'ONE'
    if n == '2' : return 'TWO'
    if n == '3' : return 'THR'
    if n == '4' : return 'FOU'
    if n == '5' : return 'FIV'
    if n == '6' : return 'SIX'
    if n == '7' : return 'SEV'
    if n == '8' : return 'EIG'
    if n == '9' : return 'NIN'
def last(list):
    t = 0
    for i in list:
        t = t + ff(i)
        t = t * 10
    return int(t/10)
s = input()
k = s.find('+')
list1 = []
list2 = []
#print(k)
r = ""
for i in range(k):
    r = r + s[i]
    if (i+1) % 3 == 0:
        list1.append(r)
        r = ""

for i in range(k+1,len(s)):
    r = r + s[i]
    if (i) % 3 == 0:
        list2.append(r)
        r = ""
result = last(list1) + last(list2)
result = str(result)
for i in result:
    print(gg(i), end="")
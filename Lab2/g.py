a = int(input())
dict = {}
for i in range(a):
    a = list(map(str, input().split()))
    if a[1] not in dict:
        dict[a[1]] = 1
    else:
        dict[a[1]] += 1
b = int(input())
dict1 = {}
for i in range(b):
    c = list(map(str,input().split()))
    if c[1] not in dict1:
        dict1[c[1]] = int(c[2])
    else:
        dict1[c[1]] = dict1[c[1]] + int(c[2])
#print(dict)
#print(dict1)
k = 0
for i in dict.keys():
    if i not in dict1: k = k + dict[i]
    elif dict1[i] - dict[i] < 0: k = k + -1*(dict1[i] - dict[i])
#for v in dict1.keys():
 #   if (dict1[v] - dict[v]) >= 0 : k = k - 1
    
print("Demons left: " + str(k))
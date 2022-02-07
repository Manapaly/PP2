n = int(input())
dict = {}
for i in range(n):
    a, b = map(str,input().split())
    b = int(b)
    if a not in dict.keys():
        dict[a] = b
    else:
        dict[a] += b
max_sum = (max(*dict.values()))
#d = {'a': 10, 'b': 15, 'c': 4}
list_keys = list(dict.keys())
list_keys.sort()
for i in list_keys:
    if(dict[i] == max_sum):
        print(str(i) + " is lucky!")
    else:
        print(str(i) + " has to receive " + str(max_sum - dict[i]) + " tenge")

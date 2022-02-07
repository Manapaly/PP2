s = input()
mylist = []
ok = True
for i in range(len(s)):
    if s[i]=='(' or s[i]=='{' or s[i]=='[': mylist.append(s[i])
    else:
        if(len(mylist)==0):
            ok = False
            break
        else:
            if s[i] == ')' and mylist[len(mylist)-1] != '(':
                ok = False
                break
            if s[i] == '}' and mylist[len(mylist)-1] != '{':
                ok = False
                break
            if s[i] == ']' and mylist[len(mylist)-1] != '[':
                ok = False
                break
        mylist.pop(len(mylist)-1)
if ok == False or len(mylist) > 0:
    print("No")
else:
    print("Yes")



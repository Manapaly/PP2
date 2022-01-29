ans = 0
def ToDecimal(s):
    ans = 0
    for i in range(len(s)):
        ans = ans + (ord(s[i])-ord('0'))*pow(2, len(s)-i-1)
    return ans
def ToDecimalByRecursion(s,i):
    global ans
    ans = ans + (ord(s[i])-ord('0'))*pow(2, len(s)-i-1)
    if i == len(s)-1: return ans
    else: return ToDecimalByRecursion(s,i+1)

s=str(input())
# print(ToDecimal(s))
print(ToDecimalByRecursion(s,0))


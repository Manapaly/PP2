a = int(input())
s = str(input())


if s == "k":
    k = str(input())
    ansFormat = "{:." + k + "f}"
    print(ansFormat.format(a / 1024))
elif s == "b":
    print(a * 1024)
k=int(input())

for i in range(0, k):
    a=int(input())
    if(a<=10):
        print("Go to work!")
    elif a>10 and a<=25:
        print("You are weak")
    elif a>25 and a<=45:
        print("Okay, fine")
    else:
        print("Burn! Burn! Burn Young!")
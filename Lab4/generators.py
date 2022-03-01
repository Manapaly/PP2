ans1 = [i*i for i in range(int(input()))]
print(*ans1)

ans2 = [i for i in range(0,int(input()),2)]
print(*ans2, sep = ', ')

ans3 = [i for i in range(int(input())) if i % 3 == 0 or i % 4 == 0]
print(*ans3)

def first_n(n):
    num = 0
    while num < n:
        if num % 3 == 0 or num % 4 == 0:
            yield num
        num += 1
print(*first_n(1000))

ans4 = [i*i for i in range(10,20)]
print(*ans4)

def num_from_n_to_0(n):
    num = n
    while num >= 0:
        yield num
        num -= 1
print(*num_from_n_to_0(15))
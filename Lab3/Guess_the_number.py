import random
ans = random.randint(1,20)
cnt = 1
t = 'Take a guess.'

print('Hello! What is your name?')
name = input()
print(f'Well, {name}, I am thinking of a number between 1 and 20.')
print(t)
num = int(input())
print()
ss = True
while ss==True:
    if(num>ans):
        print("Your guess is too high.")
        print(t)
        cnt += 1
        num = int(input())
        print()
    if(num<ans):
        print("Your guess is too low.")
        print(t)
        cnt +=1
        num = int(input())
        print()
    if(num==ans):
        print(f'Good job, {name}! You guessed my number in {cnt} guesses!')
        ss = False

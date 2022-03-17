#3 Python program with builtin function that checks whether a passed string is palindrome or not.

def palindrom(sequence):
    for n, m in zip(sequence, reversed(sequence)):
        # print(f'{n} and {m}')
        if n!=m:
            return False
    return True
print(palindrom('a'))
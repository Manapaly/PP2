#5 Python program with builtin function that returns True if all elements of the tuple are true.

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
thistuple1 = ("apple", False, "cherry", "apple", "cherry")
thistuple2 = ("apple", True, "cherry", "apple", "cherry")
print(all(thistuple))
print(all(thistuple1))
print(all(thistuple2))


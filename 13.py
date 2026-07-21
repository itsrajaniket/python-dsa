# Practice Problem: Create a list of 5 fruits. Add a new fruit to the end of the list, then remove the second fruit (at index 1).

fruits = ["apple", "banana", "cherry", "date", "elderberry"]


new = fruits[1:]
print (new)
fruits.pop(1)
print(fruits)
new.append("fig")
print(new)
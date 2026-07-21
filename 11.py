# Exercise 5. Variable Swapping (The In-Place Method)
# Practice Problem: Write a program to swap the values of two variables, a and b, without using a third temporary variable.


a = 5 
b = 10
print(f"Before Swap: a = {a}, b = {b}")

a , b = b , a


print(f"After Swap: a = {a}, b = {b}")



a = a + b
b = a - b
a = a - b

print(f"After Swap: a = {a}, b = {b}")

# Practice Problem: Write a program that calculates the factorial of a given number (e.g., 5!) using a for loop.



num = 5
factorial = 1

# Loop from 1 to num (inclusive)
for i in range(1, num + 1):
    factorial = factorial * i

print(f"The factorial of {num} is {factorial}")
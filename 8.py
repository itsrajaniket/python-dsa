# Practice Problem: Iterate through the first 10 numbers (0–9). In each iteration, print the current number, the previous number, and their sum.

sum = 0
pre=0
for i in range(10):
    sum = sum + i
    # print(sum)
    cur = i
    print(f"Current Number {cur} Previous Number {pre} Sum: {cur+pre}")
    pre=i

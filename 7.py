# # Practice Problem: Write a Python function that accepts two integer numbers. If the product of the two numbers is less than or equal to 1000, return their product; otherwise, return their sum.


# x = int(input("enter number 1 :"))
# y = int(input("enter number 2 :"))

# if (x * y ) <= 1000:
#     print(x*y)
# else:
#     print(x+y)

def pro(x, y):
    if (x * y) <= 1000:
        return x * y
    else:
        return x + y

a = pro(20, 30)
b = pro(40, 30)

print(a, b)

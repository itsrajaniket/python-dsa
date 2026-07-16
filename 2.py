# Python Program - Swap Two Variables in Python 

x = 5
y = 10

# x,y = y,x

y = x + y
x = y - x
y = y - x

print(x,y)

x = y + x
y = x - y
y = x - y

print(x,y)

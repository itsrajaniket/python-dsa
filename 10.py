# Exercise 4. String Slicing and Substring Removal
# Practice Problem: Write a function to remove characters from a string starting from index 0 up to n and return a new string.



def nameget( name , n ):
    reg = name[ n: ]
    return reg

result = nameget("aniketraj" , 4)
print (result)
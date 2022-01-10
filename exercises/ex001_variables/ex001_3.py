#! /usr/bin/env python3
x = "Awesome"  # Global Variable
def myfunc():
    y = "fantastic"  # local variable
    print("Python is " + y)
    global z
    z = "Hard"
    global x
    x = "Funny"
# Using the global keyword, you can create a global variables inside a function and can use this in all the code.

myfunc()

print("Python is " + x) 
print("Python is ", z)


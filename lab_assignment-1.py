#Q.1 print helloworld
#Ans:- 
print('HELLO WORLD')

#OUTPUT:-
# HELLO WORLD

# Q.2 describe local variable and global variable code
#Ans:- 
x = 10

def rohit_function():
    y = 5
    print("Inside the function, local variable y:", y)
    print("Inside the function, global variable x:", x)

rohit_function()

print("Outside the function, global variable x:", x)

#OUTPUT:-

# Inside the function, local variable y: 5
# Inside the function, global variable x: 10
# Outside the function, global variable x: 10

# Q.3 Write a code that describe Indentation error
#Ans:- 

def ajay_function():
    x = 10
    y = 20
    if x < y:
     print("x is less than y")  # This line is incorrectly indented
ajay_function()

#OUTPUT:-

# IndentationError

# Q.4 write a code that describe local and global variable with same name
#Ans:- 

x = 10
def var_function():
    x = 20
    print("Inside the function, local variable x:", x)
var_function()
print("Outside the function, global variable x:", x)

#OUTPUT:-

# Inside the function, local variable x: 20
# Outside the function, global variable x: 10

# Q.5 Write a code for string, int and float input.

#Ans:- 

my_string = " rohit verma"
print("string = ",my_string)

my_int = "56"
print(" integer = ", my_int)

my_float ="25"
print("float=", my_float)

 #OUTPUT:-

# string =   rohit verma
#  integer =  56
# float= 25
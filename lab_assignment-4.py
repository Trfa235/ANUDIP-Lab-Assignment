# Write a program to show the example of following.

# Q.1 Function without Parameters:
# Ans:-
def calculate_square():
    a = 4
    square = a*a
    print(f"The square of {a} is {square}")

calculate_square()

# Output:-

# The square of 4 is 16

# Q.2 Function with Parameter:
# Ans:-
def Employee (firstname,lastname='Staff',  Degination ='Developer'):
         print ( firstname,lastname,'work as a',Degination, 'Developer')

Employee( 'Raman' ,'Sharma','manager')
Employee('Aman')

# Output:-

# Raman Sharma work as a manager Developer
# Aman Staff work as a Developer Developer

# Q.3 Function with Default Parameter:
# Ans:-
def Greet (name="Bhai"):
     print("Hello",name,)

Greet("AJAY")
Greet()

# Output:-

# Hello AJAY
# Hello Bhai

# Q.4 Function with Return Keyword:
# Ans:-

def Age(age):
    if age >= 18:
        return "You are an adult."
    else:
        return "You are a minor."
    
message = Age(20)
print(message)

# Output:-

# You are an adult.

# Q.5 Recursion:
        #   a) WAP to print factorial value of a given number using recursion.
# Ans:-
def factorial(n):
    
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
number = int(input("Enter a number: "))
result = factorial(number)
print("The factorial of",number," is" ,result)

# Output:-

# Enter a number: 5
# The factorial of 5  is 120

        #   b) WAP to display Fibonacci series up to 10 iteration using recursion.
# Ans:-

def fibonacci (n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

# Example
num_terms = 10
print (fibonacci(num_terms))

# Output:-
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

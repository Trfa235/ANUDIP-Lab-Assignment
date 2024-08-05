# Q.1  Write a Python program that takes a number as input and prints "Even" if the number is even and "Odd" if it's odd.
# Ans:-

a=int(input("Enter the number..  "))
if ( a%2)==0:
    print("The number is even")
else:
    print("The number is odd")

# Output:-

# Enter the number..  8
# The number is even

# Enter the number..  7
# The number is odd

# Q.2  Create a Python program that checks whether a person is eligible to vote (18 years or older) based on their age.
# Ans:-

Age=int(input("Enter the candidate age...   "))
if Age< 18:
    print("The candidate is not eligible for vote")
else:
    print("The candidate is  eligible for vote")

# Output:-

# Enter the candidate age...   15
# The candidate is not eligible for vote
      
# Enter the candidate age...   18
# The candidate is  eligible for vote

# Q.3  Write a Python program that determines if a given year is a leap year or not.
# Ans:-

YEAR = int(input('Enter the year ...   '))
if (YEAR%4)==0 and (YEAR%100)==0  or (YEAR%100)==0  and (YEAR%400)==0 :
    print ("The Year ", YEAR, "is leap year")
else:
    print ("The Year ", YEAR, "is not leap year")

# Output:-

# Enter the year ...   2000
# The Year  2000 is leap year

# Enter the year ...   2003
# The Year  2003 is not leap year

# Q.4 Create a Python program that checks if a user-given number is positive, negative, or zero.
# Ans:-

a=int(input("Enter the number..    "))
if a<0:
    print('The number is a Negative Number')
elif a==0:
 print('The number is Zero')
else:
    print('The number is a Positive Number')

# Output:-

# Enter the number..    -5
# The number is a Negative Number

# Enter the number..    5
# The number is a Positive Number

# Enter the number..    0
# The number is Zero

# Q.5  Write a Python program that determines the largest of three numbers entered by the user.
# Ans:-

a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
c = int(input('Enter the third number: '))

if a == b and b == c:
    print('a, b, and c are equal')
elif a == b and a > c:
    print('a and b are equal,but c is the largest number')
elif a == c and a > b:
    print('a and c are equal but b is the largest number')
elif b == c and b > a:
    print('b and c are equal but a is the largest number')
elif a == b and c > a:
    print('a and b are equal, but c is the largest number')
elif a == c and b > a:
    print('a and c are equal, but b is the largest number')
elif b == c and a > b:
    print('b and c are equal, but a is the largest number')
elif a > b and a > c:
    print('a is the largest number')
elif b > a and b > c:
    print('b is the largest number')
else:
    print('c is the largest number')

# Output:-

# Enter the first number: 5
# Enter the second number: 6
# Enter the third number: 7
# c is the largest number
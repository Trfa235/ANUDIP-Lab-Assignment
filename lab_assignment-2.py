# Q.1 Write a program for arithmetic operaters.
# Ans:-

a=5
b=2
print('sum of two number is :-',a+b)
print('Difference of two number is :-',a-b)
print('Product of two number is :-',a*b)
print('Exponent of a number is :-',a**b)
print('Divison of a number is :-',a/b)
print('Floor Divison of a number is :-',a//b)
print('Modulus of a number is :-',a%b)
print('Modulus of a number is :-',b%a)
print('Divison of a number is :-',b/a)
print('Floor Divison of a number is :-',b//a)

# Output:-

# sum of two number is :- 7
# Difference of two number is :- 3 
# Product of two number is :- 10   
# Exponent of a number is :- 25    
# Divison of a number is :- 2.5    
# Floor Divison of a number is :- 2
# Modulus of a number is :- 1      
# Modulus of a number is :- 2      
# Divison of a number is :- 0.4    
# Floor Divison of a number is :- 0

# Q.2 Write a program for Assignment operaters. 
# Ans:-

a = 10
b = 5
# Assignment operator
c = a
print("c = a:", c)  
# Add AND assignment operator
c += b
print("c += b:", c)  
# Subtract AND assignment operator
c -= b
print("c -= b:", c) 
# Multiply AND assignment operator
c *= b
print("c *= b:", c)  
# Divide AND assignment operator
c /= b
print("c /= b:", c)  
# Modulus AND assignment operator
c %= b
print("c %= b:", c)  
# Exponent AND assignment operator
c **= b
print("c *= b:", c)  
# Floor division AND assignment operator
c = 10  
c //= b
print("c //= b:", c)  
# Bitwise AND assignment operator
c = 10  
c &= b
print("c &= b:", c)  
# Bitwise OR assignment operator
c |= b
print("c |= b:", c)  
# Bitwise XOR assignment operator
c ^= b
print("c ^= b:", c)  
#Bitwise left shift assignment operator
c <<= b
print("c <<= b:", c) 
#Bitwise right shift assignment operator
c = 10  
c >>= b
print("c >>= b:", c)  

# Output:-

# c = a: 10
# c += b: 15  
# c -= b: 10  
# c *= b: 50  
# c /= b: 10.0
# c %= b: 0.0 
# c *= b: 0.0 
# c //= b: 2  
# c &= b: 0   
# c |= b: 5   
# c ^= b: 0   
# c <<= b: 0
# c >>= b: 0

# Q.3 Write a program for Bitwise operaters. 
# Ans:-

a = 5  
b = 3  

print("a =", a)
print("b =", b)
# Bitwise AND
print("a & b =", a & b)
# Bitwise OR
print("a | b =", a | b)
# Bitwise XOR
print("a ^ b =", a ^ b)
# Bitwise NOT
print("~a =", ~a)
# Left Shift
print("a << 2 =", a << 2)
# Right Shift
print("b >> 2 =", b >> 2)

# Output:-

# a = 5
# b = 3
# a & b = 1
# a | b = 7
# a ^ b = 6
# ~a = -6
# a << 2 = 20
# b >> 2 = 0

# Q.4 Write a program to calculate greatest of three numbers.
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
# Enter the second number: 5
# Enter the third number: 9
# a and b are equal, but c is the largest number
# Q28. Return second largest of three distinct
# numbers using ternary operator only.

a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
c = int(input('Enter third number: '))

small = a if a < b and a < c else b if b < c else c
big = a if a > b and a > c else b if b > c else c
second_large = (a+b+c) - (small+big)
print(second_large)
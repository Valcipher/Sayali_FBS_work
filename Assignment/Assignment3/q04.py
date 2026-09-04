#Q4. Write a program to input all sides of a triangle and check whether triangle is valid or not.

a = int(input('Enter side 1: '))
b = int(input('Enter side 2: '))
c = int(input('Enter side 3: '))

if a+b > c and b+c > a and a+c > b:
    print('Valid triangle')
else:
    print('Not a valid triangle')
#Q3. Write a program to input angles of a triangle and check whether triangle is valid or not.

a1= int(input('Enter angle 1: '))
a2= int(input('Enter angle 2: '))
a3= int(input('Enter angle 3: '))

if(a1 > 0 and a2 > 0 and a3 > 0 and a1+a2+a3 == 180):
    print('triangle')
else:
    print('not triangle')


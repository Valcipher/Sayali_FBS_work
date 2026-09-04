#Q10. Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)

name = input('Enter your name: ')
gender = input('Enter gender(M/F): ')
age = int(input('Enter age: '))

if( gender == 'F'):
    if(age>=18):
        print(f'{name} is eligible to marry.')
    else:
        print(f'{name} is not eligible to marry.')
else:
    if(age>=21):
        print(f'{name} is eligible to marry.')
    else:
        print(f'{name} is not eligible to marry.')


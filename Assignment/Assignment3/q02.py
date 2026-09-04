#Q2. Write a program to input any alphabet and check whether it is vowel or consonant.

vowels = ['a', 'e', 'i', 'o', 'u']

alpha = input('Enter a char: ')

if(alpha in vowels):
    print('vowel')
else:
    print('consonant')
    


#Q12. Write a program to check if given 3 digit number is a palindrome or not.

num = int(input('Enter a number: '))
temp = num
rev_num = 0

while(temp>0):
    d = temp % 10
    temp = temp // 10
    rev_num = rev_num * 10 +d

if(num == rev_num):
    print('It is a palindrome number.')
else:
    print('It is not a palindrome number.')
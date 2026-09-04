#Q12. Write a program to check if given number is Armstrong number or not.

num = int(input('Enter a number: '))
temp = num
count = 0

while(temp>0):
    count +=1
    temp = temp // 10

temp = num
sum = 0

while(temp>0):
    d = temp % 10
    temp = temp // 10
    sum = sum + (d**count)

if(sum == num):
    print('Armstrong number')
else:
    print('not an armstrong number')
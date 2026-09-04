#Q11. WAP to check if given number Strong Number.

num = int(input('Enter a num: '))
temp = num
sum = 0

while(temp>0):
    d = temp % 10
    temp = temp // 10
    fact = 1
    for i in range(1, d+1):
        fact *= i
    sum += fact
if(sum == num):
    print('Strong number')
else:
    print('Not a strong number')
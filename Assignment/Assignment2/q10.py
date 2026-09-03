#Q10. Write a program to reverse three-digit number.

num = 123
temp = num
rev_num = 0

while(temp>0):
    d = temp % 10
    temp = temp // 10
    rev_num = rev_num * 10 + d
print(rev_num)
















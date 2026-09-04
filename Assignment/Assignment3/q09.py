#Q9. Input 5 subject marks from user and display grade(eg.First class,Second class ..)

s1= int(input('Enter marks for sub1: '))
s2= int(input('Enter marks for sub2: '))
s3= int(input('Enter marks for sub3: '))
s4= int(input('Enter marks for sub4: '))
s5= int(input('Enter marks for sub5: '))

sum = int((s1+ s2+ s3+ s4+ s5)/5)

A = range(81,101)
B = range(61,81)
C = range(41,61) 



if(sum in A):
    print('First class')
elif(sum in B):
    print('Second class')
elif(sum in C):
    print('Class Three')
else:
    print('Fail')
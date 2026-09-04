#Q9. WAP to print all numbers in a range divisible by a given number.

num = int(input('Enter a number: '))

a = int(input('Enter a number: '))


for i in range(1,num+1):
    if(i%a ==0):
        print(i,end=' ')





#Q6. Write a program to calculate profit or loss.

SP = int(input('Enter selling price: '))
CP = int(input('Enter cost price: '))

if(SP>CP):
    print('profit')
elif(CP>SP):
    print('loss')
else:
    print('no profit/loss')





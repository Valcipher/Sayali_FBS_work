#Q8. Write a program to prompt user to enter userid and password. After verifying userid and password display a 4 digit random number and ask user to enter the same. If user enters the same number then show him success message otherwise failed. (Something like captcha)

import random
useId = input('Enter the user Id: ')
password = input('Enter password: ')

if useId == '1234' and password == '123':
    systemcptcha = random.randint(1000,10000)
    print(systemcptcha)

    captcha = int(input('Enter the Captcha: '))

    if captcha == systemcptcha:
        print("You have successfully log in...")
    else:
        print('Invalid Captcha...try again')
else:
    print('Invalid Id and Password.')















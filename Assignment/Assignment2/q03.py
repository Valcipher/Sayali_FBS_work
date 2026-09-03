#Q3. Convert distant given in feet and inches into meter and centimeter.
feet = int(input('Enter value in feet: '))
inch = int(input('Enter value in inch: '))

meter = feet * 0.3048
centimeter = inch * 2.54

print(f'meter = {meter:.2f} and centimeter = {centimeter}')
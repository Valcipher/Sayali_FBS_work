#8. Write a program to convert days into years, weeks and days.

days = 600

years = days // 365
remaining_days = days % 365

months = remaining_days // 30
remaining_days = remaining_days % 30

weeks = remaining_days // 7
remaining_days = remaining_days % 7

print(f'{years}years, {months} months, {weeks}weeks, {remaining_days}days')















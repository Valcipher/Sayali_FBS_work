#Q5. Write a program to enter P, T, R and calculate Compound Interest.

P = 10000
R = 6
T = 2

CI = P*(1+R/100)**T-P

print(f'CI is {CI: .2f}')
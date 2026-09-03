#Q11. Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount.

amount = int(input('Enter amount: '))

notes = [2000, 500, 200, 100, 50, 20, 10]
count = 0

for note in notes:
    count += amount // note
    amount = amount % note

print('Minimum number of notes =', count)
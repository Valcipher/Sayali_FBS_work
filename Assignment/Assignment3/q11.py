#Q11. Accept age of five people and also per person ticket amount and then calculate total
# amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

total = 0
for i in range(5):
    age = int(input('Enter age: '))
    ticket = int(input('Enter ticket amount: '))

    if age < 12:
        ticket = ticket - (ticket * 30 / 100)
    elif age > 59:
        ticket = ticket - (ticket * 50 / 100)

    total = total + ticket

print('Total ticket amount =', total)




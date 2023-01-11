import random

win = [7, 11]
lose = [2, 3, 12]
point = [1, 4, 5, 6, 7, 8, 9, 10]

x = 100


def how_much():
    bet = int(input("Bet: "))
    if bet > x:
        print("Haha funny, try again...")
        how_much()
    elif bet < 0:
        print("Haha funny, try again...")
    else:
        return bet


bet = how_much()

while x > 0:

    (d1, d2) = (random.randint(1, 7), random.randint(1, 7))
    result = d1 + d2
    if result in win:
        x += bet
        print("You rolled a " + str(d1) + " and " + str(d2))
        print("*****" + str(result) + "*****")
        print("YOU WON " + str(bet) + " DOLLARS! | Current Cash: " + str(x))
        input("Press enter to continue...")
        how_much()

    elif result in lose:
        x -= bet
        print("You rolled a " + str(d1) + " and " + str(d2))
        print("*****" + str(result) + "*****")
        print("YOU LOST " + str(bet) + " DOLLARS! | Current Cash: " + str(x))
        input("Press enter to continue...")
        how_much()

    elif result in point:
        print("You rolled a " + str(d1) + " and " + str(d2))
        print("Point - Shoot again!")
        input("Press enter to continue")
        continue

    elif x <= 0:
        print("You have no money left...")
        break
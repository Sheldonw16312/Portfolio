import random

face = ["K", "Q", "J", "A"]
ace = [1, 11]
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
hand1 = []
bhand1 = []
hand2 = []
bhand2 = []
sumh1 = sum(bhand1)
sumh2 = sum(bhand2)
final = 0


def hs2():
    sumh2 = sum(bhand2)
    print("Total2: " + str(sumh2))
    x = input("Player2: Hit(H) or Stay(S)").lower()
    if x == "h":
        draw2()
    elif x == "s":
        hs1()


def hs1():
    sumh1 = sum(bhand1)
    print("Total1: " + str(sumh1))
    x = input("Player1: Hit(H) or Stay(S)").lower()
    if x == "h":
        draw1()
    elif x == "s":
        hs2()


def aces1():
    z = ace[0]  # 1
    x = ace[1]  # 11
    if z + sumh1 == 21:
        bhand1.append(z)
    elif x + sumh1 == 21:
        bhand1.append(x)
    elif sumh1 >= 11:
        bhand1.append(z)
    elif sumh1 <= 10:
        bhand1.append(x)

    hs2()


def aces2():
    z = ace[0]  # 1
    x = ace[1]  # 11
    if z + sumh2 == 21:
        bhand1.append(z)
    elif x + sumh2 == 21:
        bhand2.append(x)
    elif sumh2 >= 11:
        bhand2.append(z)
    elif sumh2 <= 10:
        bhand2.append(x)

    hs1()


def draw2():
    x = random.randint(0, 12)
    d = cards[x]
    hand2.append(d)
    if d == "A":
        aces2()
    elif d in face:
        bhand2.append(10)
    else:
        bhand2.append(d)

    sumh1 = sum(bhand1)
    sumh2 = sum(bhand2)
    x = random.randint(0, 12)
    print("You drew: " + str(d))
    print("Hand2: " + str(hand2))
    print("New Total: " + str(sumh2))

    if sumh1 < 21 and sumh2 < 21:
        hs1()
    elif sumh2 > 21:
        print("Hand 2 bust. Hand 1 Wins!")
    elif sumh2 == 21:
        print("Hand 2 wins!")


def draw1():
    x = random.randint(0, 12)
    d = cards[x]
    hand1.append(d)
    if d == "A":
        aces1()
    elif d in face:
        bhand1.append(10)
    else:
        bhand1.append(d)

    sumh1 = sum(bhand1)
    sumh2 = sum(bhand2)
    x = random.randint(0, 12)
    print("You drew: " + str(d))
    print("Hand: " + str(hand1))
    print("New Total: " + str(sumh1))

    if sumh1 < 21 and sumh2 < 21:
        hs2()
    elif sumh1 > 21:
        print("Hand 1 bust. Hand 2 Wins!")
    elif sumh1 == 21:
        print("Hand 1 wins!")


def start():
    hs1()


# deal = draw()
start()
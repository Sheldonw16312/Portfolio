import random
import time

# TekkenLUL
#
phealth = 100
static_char = ["Heihachi", "King", "Devil Jin", "Yoshimitsu"]
avail_char = ["Heihachi", "King", "Devil Jin", "Yoshimitsu"]


class Players():
    def __init__(self, name, health, victories):
        self.name = name
        self.health = health
        self.victories = victories


p = Players("PH", 100, 0)
c = Players("PH", 100, 0)


# Light(2) > Dodge(4) / Dodge(4) > Heavy(1) / Heavy(1) > Block(3) / Block(3) > Light(2)
# Light(-8) Heavy (-14) Neautral (-4)

def fight():
    print(f"{p.name} Health: {p.health}")
    print(f"{c.name} Health: {c.health}")

    p1 = player()
    p2 = cpu()

    if p.health <= 0 or c.health <= 0:
        if p.health <= 0:
            print(f"{p.name} lost.")
            print(f"{c.name} won!")
            c.victories += 1
        elif c.health <= 0:
            print(f"{c.name} lost.")
            print(f"{p.name} won!")
            p.victories += 1
    elif p1 == 2 and p2 == 4:
        print("Light Beats Dodge")  # Player Attacks CPU
        c.health -= 8
        time.sleep(.5)
        print(f"{c.name} suffered 8 damage.")
        input("Press enter to continue...")
        fight()

    elif p1 == 4 and p2 == 2:
        print("Light Beats Dodge")  # CPU Attacks Player
        p.health -= 8
        time.sleep(.5)
        print(f"{p.name} suffered 8 damage.")
        input("Press enter to continue...")
        fight()

    elif p1 == 1 and p2 == 4:
        print("Dodge Beats Heavy")  # Player Attacks CPU
        time.sleep(1)
        print(f"{p.name} dodged {c.name}'s attack.")
        input("Press enter to continue...")
        fight()

    elif p1 == 4 and p2 == 1:
        print("Dodge Beats Heavy")  # CPU Attacks Player
        time.sleep(.5)
        print(f"{c.name} dodged {p.name}'s attack.")
        input("Press enter to continue...")
        fight()

    elif p1 == 1 and p2 == 3:
        print("Heavy Beats Block")  # Player Attacks CPU
        c.health -= 14
        time.sleep(.5)
        print(f"{c.name} suffered 14 damage.")
        input("Press enter to continue...")
        fight()

    elif p1 == 3 and p2 == 1:
        print("Heavy Beats Block")  #
        p.health -= 14
        time.sleep(.5)
        print(f"{p.name} suffered 14 damage.")
        input("Press enter to continue...")
        fight()

    elif p1 == 3 and p2 == 2:
        print("Block Beats Light")
        time.sleep(.5)
        print(f"{p.name} blocked {c.name}'s attack.")
        input("Press enter to continue...")
        fight()

    elif p1 == 2 and p2 == 3:
        print("Block Beats Light")
        time.sleep(.5)
        print(f"{c.name} blocked {p.name}'s attack.")
        input("Press enter to continue...")
        fight()

    elif p1 == 2 and p2 == 2:
        print("You both attacked. Both figters suffer 4 damage.")
        c.health -= 4
        p.health -= 4
        time.sleep(.5)
        input("Press enter to continue...")
        fight()

    elif p1 == 2 and p2 == 4:
        print("You both attacked. Both figters suffer 5 damage.")
        c.health -= 5
        p.health -= 5
        time.sleep(.5)
        input("Press enter to continue...")
        fight()

    elif p1 == 4 and p2 == 2:
        print("You both attacked. Both figters suffer 5 damage.")
        c.health -= 5
        p.health -= 5
        time.sleep(.5)
        input("Press enter to continue...")
        fight()

    elif p1 == 4 and p2 == 4:
        print("You Both Dodged")
        print("Neither Fighter Takes Damage")
        c.health -= 7
        p.health -= 7
        time.sleep(.5)
        input("Press enter to continue...")
        fight()

    elif p1 == 3 and p2 == 3:
        print("You both Blocked")
        print("Neither Fighter Takes Damage")
        time.sleep(.5)
        input("Press enter to continue...")
        fight()

    elif p1 == 2 and p2 == 1:
        c.health -= 8
        print("Light Beats Heavy")
        print(f"{c.name} suffered 8 damage.")
        time.sleep(.5)
        input("Press enter to continue...")
        fight()

    elif p1 == 1 and p2 == 2:
        p.health -= 8
        print("Light Beats Heavy")
        print(f"{p.name} suffered 8 damage.")
        time.sleep(.5)
        input("Press enter to continue...")
        fight()

    elif p1 == 3 and p2 == 4:
        print("Block and Dodge")
        print("Neither Fighter Takes Damage")
        time.sleep(.5)
        input("Press enter to continue...")
        fight()

    elif p1 == 4 and p2 == 3:
        print("Block and Dodge")
        print("Neither Fighter Takes Damage")
        time.sleep(.5)
        input("Press enter to continue...")
        fight()


def player():
    print("Heavy(1)/ Light(2)/ Block(3)/ Dodge(4)/ ")
    x = int(input())

    if x == 1:
        print(f"{p.name}: Heavy Attack")
        return 1
    elif x == 2:
        print(f"{p.name}: Light Attack")
        return 2
    elif x == 3:
        print(f"{p.name}: Block")
        return 3
    elif x == 4:
        print(f"{p.name}: Dodge")
        return 4


def cpu():
    x = random.randint(1, 4)
    if x == 1:
        print(f"{c.name}: Heavy Attack")
        return 1
    elif x == 2:
        print(f"{c.name}: Light Attack")
        return 2
    elif x == 3:
        print(f"{c.name}: Block")
        return 3
    elif x == 4:
        print(f"{c.name}: Dodge")
        return 4


def start():
    print("Welcome to Tekken! Choose your player.")
    time.sleep(1)
    print("Devil Jin(1)/ Yoshimitsu(2)/ King(3)/ Heihachi(4)")
    x = int(input())

    if x == 1:
        p.name = "Devil Jin"
        avail_char.remove("Devil Jin")
        print("DEVIL JIN")
    elif x == 2:
        p.name = "Yoshimitsu"
        avail_char.remove("Yoshimitsu")
        print("YOSHITMITSU")
    elif x == 3:
        p.name = "King"
        avail_char.remove("King")
        print("KING")
    elif x == 4:
        p.name = "Heihachi"
        avail_char.remove("Heihachi")
        print("HEIHACHI")

    print("Your opponent will be...")

    y = random.randint(1, 3)
    if y == 1:
        c.name = avail_char[0]
        z = (avail_char[0]).upper()
        print(z)
        fight()
    elif y == 2:
        c.name = avail_char[1]
        z = (avail_char[1]).upper()
        print(z)
        fight()
    elif y == 3:
        c.name = avail_char[2]
        z = (avail_char[2]).upper()
        print(z)
        fight()


start()
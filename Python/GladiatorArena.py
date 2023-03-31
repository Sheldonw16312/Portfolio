import random
import time

# Finish rewards roll / maybe add more

rewards = ["HP10(10)", "HP30(30)", "HP50(50)"]
pullfrmhere = ["HP10(10)", "HP30(30)", "HP50(50)"]
inv = []


class Player:
    def __init__(self, name, health, speed, points, victories):
        self.name = name
        self.health = health
        self.speed = speed
        self.points = points
        self.victories = victories


class Beasts:
    def __init__(self, name, health):
        self.name = name
        self.health = health


############################################################# ATTACKS ###############################################################
def cattack():
    x = random.randint(1, 10)
    return x


def oattack():
    x = random.randint(1, 11)
    return x


def tattack():
    x = random.randint(1, 12)
    return x


def pattack():
    x = random.randint(1, 12)
    return x


###################################################### CHARACTERS ######################################################################

c = Beasts("Chimera", 80)
o = Beasts("Ogre", 100)
t = Beasts("Titan", 120)
p = Player("PH", 100, 10, 0, 0)


def opponent():
    x = random.randint(1, 3)
    if x == 1:
        chimera()
    elif x == 2:
        ogre()
    elif x == 3:
        titan()


###################################################### ARENA 2 ######################################################################
def cont_arena():
    print("Welcome back " + p.name + "!!!")
    x = input("Are you ready to fight again?!?! (Y/N) ").lower()

    if x == "y":
        print("Let's get to it then!")
        time.sleep(1)
        print("Today you'll be fighting...")
        time.sleep(1)
        opponent()
    elif x == "n":
        print("So sad...Come back whenver you're ready.")
    else:
        print("That's not an option. Let me start over...")
        cont_arena()


###################################################### INTERMISSION ######################################################################
def limbo():
    fspeed = 30
    healthcap = 100
    print("You have " + str(p.health) + " remainng.")
    print("Healing...")
    time.sleep(1)
    while p.health < healthcap:
        if p.health < 95:
            p.health += 1
            time.sleep(.1)
            print(p.health)
        elif p.health >= 95:
            p.health += 1
            time.sleep(.5)
            print(p.health)


    time.sleep(1.5)
    print("All healed up.")
    time.sleep(1.5)
    if p.points > 0:
        print("You have (" + str(p.points) + ") Attribute points.")
        time.sleep(1.5)
        x = input("Would you like to use it? If not now, you won't be able to use it until your next rest. (Y/N)").lower()
        if x == "y":
            print("What would you like to increase?")
            time.sleep(1.5)
            x = input(f"""Health: {p.health} - +5 (H)
or 
Speed: {fspeed} - +5 (S) """).lower()

            if x == "h":
                p.health += 5
                healthcap += 5

                print(f"Your max health is now {p.health}")
                print("Continue on to the arena when you're ready.")
                input("Press enter to continue...")
                cont_arena()

            elif x == "s":
                fspeed += 5
                p.speed -= 1

                print(f"Your speed is now {fspeed}")
                print("Continue on to the arena when you're ready.")
                input("Press enter to continue...")
                cont_arena()

        else:
            print("Alright, continue on to the arena when you're ready.")
            input("Press enter to continue...")
            cont_arena()

def reward_roll():
    x  = random.randint(0,2)
    y = rewards[x]
    inv.append(pullfrmhere[x])
    print(f"You won a {y}!!!")

def hp10():
    p.health += 10
    return p.health

def hp30():
    p.health += 30
    return p.health

def hp50():
    p.health += 50
    return p.health

############################################################### FIGHTS #############################################################
############################################################## CHIMERA  ##############################################################
def chimera():
    print("The Chimera!!!")

    def fight():
        while p.health and c.health > 0:
            pa = pattack()
            ca = cattack()
            miss = random.randint(1, p.speed)
            crit = random.randint(1, 8)
            if miss == 1:
                print("The Chimera lunged and missed.")
                if crit == 1:
                    chit = pa * 2
                    c.health -= chit
                    print("The player CRITICALLY hit for: " + str(chit))
                    print(p.name + " Health: " + str(p.health))
                    print(c.name + " Health: " + str(c.health))
                else:
                    c.health -= pa
                    print("The player hit for: " + str(pa))
                    print(p.name + " Health: " + str(p.health))
                    print(c.name + " Health: " + str(c.health))

            elif crit == 1:
                chit = pa * 2
                p.health -= ca
                c.health -= chit

                print("The player CRITCALLY hit for: " + str(chit))
                print("The Chimera hit for: " + str(ca))

                print(p.name + " Health: " + str(p.health))
                print(c.name + " Health: " + str(c.health))
            elif crit == 2:
                bhit = ca * 2
                p.health -= bhit
                c.health -= pa

                print("The player hit for: " + str(pa))
                print("The Chimera CRITICALLY hit for: " + str(bhit))

                print(p.name + " Health: " + str(p.health))
                print(c.name + " Health: " + str(c.health))
            else:
                p.health -= ca
                c.health -= pa

                print("The player hit for: " + str(pa))
                print("The Chimera hit for: " + str(ca))

                print(p.name + " Health: " + str(p.health))
                print(c.name + " Health: " + str(c.health))

            if p.health <= 0:
                print("You died.")
                print(f"You had ({p.victories}) victories!")
            elif c.health <= 0:
                print("You managed to kill THe Chimera!!!")
                time.sleep(1.5)
                p.victories += 1
                p.points += 1
                print("You've obtained 1 Attribute point!!!")
                reward_roll()
                time.sleep(1.5)
                print("")
                print("Return to the provided quarters for rest, and food until your next match.")
                time.sleep(1.5)
                c.health = 80
                limbo()

            a = input("Forfeit(F), Continue(C), or Use Item(I) ? ").lower()
            if a == "f":
                print("So you've accepted death?")
                time.sleep(1)
                print("You died")
                print(f"You had ({p.victories}) victories!")
                break
            elif a == "c":
                continue

    fight()


########################################################### OGRE  #################################################################
def ogre():
    print("The Ogre!!!")

    def fight():
        while p.health and o.health > 0:
            pa = pattack()
            oa = oattack()
            miss = random.randint(1, p.speed)
            crit = random.randint(1, 8)
            if miss == 1:
                print("The Ogre lunged and missed.")
                if crit == 1:
                    chit = pa * 2
                    o.health -= chit
                    print("The player CRITICALLY hit for: " + str(chit))
                    print(p.name + " Health: " + str(p.health))
                    print(o.name + " Health: " + str(o.health))
                else:
                    o.health -= pa
                    print("The player hit for: " + str(pa))
                    print(p.name + " Health: " + str(p.health))
                    print(o.name + " Health: " + str(o.health))
            elif crit == 1:
                chit = pa * 2
                p.health -= oa
                o.health -= chit

                print("The player CRITCALLY hit for: " + str(chit))
                print("The Ogre hit for: " + str(oa))

                print(p.name + " Health: " + str(p.health))
                print(o.name + " Health: " + str(o.health))
            elif crit == 2:
                bhit = oa * 2
                p.health -= bhit
                o.health -= pa

                print("The player hit for: " + str(pa))
                print("The Ogre CRITICALLY hit for: " + str(bhit))

                print(p.name + " Health: " + str(p.health))
                print(o.name + " Health: " + str(o.health))
            else:
                p.health -= oa
                o.health -= pa

                print("The player hit for: " + str(pa))
                print("The Ogre hit for: " + str(oa))

                print(p.name + " Health: " + str(p.health))
                print(o.name + " Health: " + str(o.health))

            if p.health <= 0:
                print("You died.")
                print(f"You had ({p.victories}) victories!")
            elif o.health <= 0:
                print("You managed to kill THe Ogre!!!")
                time.sleep(1.5)
                p.victories += 1
                p.points += 1
                print("You've obtained 1 Attribute point!!!")
                reward_roll()
                time.sleep(1.5)
                print("Return to the provided quarters for rest, and food until your next match.")
                time.sleep(1.5)
                o.health = 100
                limbo()

            a = input("Forfeit(F), Continue(C), or Use Item(I) ? ").lower()
            if a == "f":
                print("So you've accepted death?")
                time.sleep(1)
                print("You died")
                print(f"You had ({p.victories}) victories!")
                break
            elif a == "c":
                continue

    fight()


######################################################  TITAN ######################################################################
def titan():
    print("The Titan!!!")

    def fight():
        while p.health and t.health > 0:
            pa = pattack()
            ta = tattack()
            miss = random.randint(1, p.speed)
            crit = random.randint(1, 8)
            if miss == 1:
                print("The Titan lunged and missed.")
                if crit == 1:
                    chit = pa * 2
                    t.health -= chit
                    print("The player CRITICALLY hit for: " + str(chit))
                    print(p.name + " Health: " + str(p.health))
                    print(t.name + " Health: " + str(t.health))
                else:
                    t.health -= pa
                    print("The player hit for: " + str(pa))
                    print(p.name + " Health: " + str(p.health))
                    print(t.name + " Health: " + str(t.health))
            elif crit == 1:
                chit = pa * 2
                p.health -= ta
                t.health -= chit

                print("The player CRITCALLY hit for: " + str(chit))
                print("The Titan hit for: " + str(ta))

                print(p.name + " Health: " + str(p.health))
                print(t.name + " Health: " + str(t.health))
            elif crit == 2:
                bhit = ta * 2
                p.health -= bhit
                t.health -= pa

                print("The player hit for: " + str(pa))
                print("The Titan CRITICALLY hit for: " + str(bhit))

                print(p.name + " Health: " + str(p.health))
                print(t.name + " Health: " + str(t.health))
            else:
                p.health -= ta
                t.health -= pa

                print("The player hit for: " + str(pa))
                print("The Titan hit for: " + str(ta))

                print(p.name + " Health: " + str(p.health))
                print(t.name + " Health: " + str(t.health))

            if p.health <= 0:
                print("You died.")
                print(f"You had ({p.victories}) victories!")
            elif t.health <= 0:
                print("You managed to kill THe Titan!!!")
                time.sleep(1.5)
                p.victories += 1
                p.points += 1
                print("You've obtained 1 Attribute point!!!")
                reward_roll()
                time.sleep(1.5)
                print("Return to the provided quarters for rest, and food until your next match.")
                time.sleep(1.5)
                t.health = 120
                limbo()

            a = input("Forfeit(F), Continue(C), or Use Item(I) ? ").lower()
            if a == "f":
                print("So you've accepted death?")
                time.sleep(1)
                print("You died")
                print(f"You had ({p.victories}) victories!")
                break
            elif a == "c":
                continue


    fight()


########################################################  ARENA ####################################################################
def arena():
    p.name = input("What do you go by Warrior? ")
    print("Welcome to the Arena " + p.name + "!!!")
    time.sleep(1)
    print("The more you fight; the more you gain.")
    x = input("Are you ready (Y/N) ?!?!?").lower()

    if x == "y":
        print("Great!")
        time.sleep(1)
        print("Today you'll be fighting...")
        time.sleep(1)
        opponent()
    elif x == "n":
        print("What a waste, come back when you are then.")
    else:
        print("That's not an option. Let me start from the beginning...")
        arena()

arena()
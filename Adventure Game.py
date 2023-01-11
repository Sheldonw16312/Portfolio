import random
import time


class Monster:
    def __init__(self, name, attack, health):
        self.name = name
        self.attack = attack
        self.health = health


class Player:
    def __init__(self, attack):
        self.attack = attack


g = Monster("Ghoul", random.randint(1, 3), 8)
s = Monster("Slime", random.randint(1, 3), 10)
o = Monster("Orc", random.randint(1, 3), 12)
p1 = Player(random.randint(1, 4))


def result1():
    if "p3" in check:
        result2()
    else:
        game2()


def result2():
    game4()


def result3():
    pass


def result4():
    pass


def result5():
    pass


def run():
    chance = random.randint(0, 1)
    if chance == 0:
        print("You got away!")
        input("Press enter to continue...")
    else:
        # health -= chance
        print("You couldn't get away and died...Game Over!")
        input("Press enter to continue...")
        game2()


def run2():
    chance = random.randint(0, 1)
    if chance == 0:
        print("You got away!")
        input("Press enter to continue...")
    else:
        # health -= chance
        print("You couldn't get away and died...Game Over!")
        input("Press enter to continue...")
        game3()


def run3():
    chance = random.randint(0, 1)
    if chance == 0:
        print("You got away!")
        input("Press enter to continue...")
    else:
        # health -= chance
        print("You couldn't get away and died...Game Over!")
        input("Press enter to continue...")


# It would be cool to have a chance of obtaining an item depending on what monster you fight. Add later.)


def gob():
    health = 10
    a = input("You encounter a Goblin!!! Fight?(Y/N)").lower()
    if a == "y":
        while a == "y":
            health -= g.attack
            g.health -= p1.attack

            print("Player attacked Goblin for: " + str(p1.attack) + " points. The Goblin now has: " + str(
                g.health) + " health points!")
            print("Goblin attacked Player for: " + str(g.attack) + " points. The Goblin now has: " + str(
                health) + " health points!")

            if health > 0 and g.health > 0:
                a = input("Continue on Run?: (Y/N)").lower()

            if health <= 0 or g.health <= 0:
                if health <= 0:
                    print("You died...Game Over!")
                    input("Press enter to continue...")
                    intro()
                elif g.health <= 0:
                    print("You killed the Goblin")
                    input("Press enter to continue...")
                    result1()


def slime():
    health = 10
    a = input("You encounter a Slime!!! Fight?(Y/N)").lower()
    if a == "y":
        while a == "y":

            health -= s.attack
            s.health -= p1.attack

            print("Player attacked Slime for: " + str(p1.attack) + " points. The Slime now has: " + str(
                s.health) + " health points!")
            print("Slime attacked Player for: " + str(s.attack) + " points. The Slime now has: " + str(
                health) + " health points!")
            if health > 0 and s.health > 0:
                a = input("Continue?: (Y/N)").lower()

            if health <= 0 or s.health <= 0:
                if health <= 0:
                    print("You died...Game over!")
                    input("Press enter to continue...")
                    intro()
                elif s.health <= 0:
                    print("You killed the Slime")
                    input("Press enter to continue...")
                    result1()


def orc():
    health = 10

    a = input("You encounter an Orc!!! Fight?(Y/N)").lower()
    if a == "y":
        while a == "y":
            health -= o.attack
            o.health -= p1.attack

            print("Player attacked Orc for: " + str(p1.attack) + " points. The Orc now has: " + str(
                o.health) + " health points!")
            print("Orc attacked Player for: " + str(o.attack) + " points. The Orc now has: " + str(
                health) + " health points!")
            if health > 0 and o.health > 0:
                a = input("Continue?: (Y/N)").lower()
                if a == "n":
                    run()

            if health <= 0 or o.health <= 0:
                if health <= 0:
                    print("You died...Game Over!")
                    input("Press enter to continue...")
                    intro()
                elif o.health <= 0:
                    print("You killed the Orc")
                    input("Press enter to continue...")
                    result1()


def mon_chc():
    chance = random.randint(1, 3)
    if chance == 1:
        return gob()
    elif chance == 2:
        return slime()
    elif chance == 3:
        return orc()


def intro():
    a = input("This is a game of chance would you like to play?(Y/N)").lower()
    acc = ["y", "n"]

    if a == "y":
        print("Then continue forward...")
        game()
    elif a == "n":
        print("Well we'll be here when you're ready!")


items = []
check = []


def game():
    a = input(
        "You walk into this dungeon so grand, and resplendent. There are only two ways you can go; Left, or Right? (L/R)").lower()
    if a == "l":
        mon_chc()
    elif a == "r":
        print("You found a treasure chest..you open it, and find a broken sword!!!")
        input("Press enter to continue")
        items.append("Broken Sword")
        print("Invenory: " + str(items))
        game2()


def game2():
    a = input(
        "You venture forward, and notice a statue who's gaze seems to follow you. Do you confront the statue, or run? (Confront/Run)").lower()
    if a == "confront":
        print("You confront the statue, and ask why does it pretend to not be sentient?")
        input("Press enter to continue...")
        print(
            "The statue says he's just wary of exposing himself as he's often attacked when he addresses explorers directly, and expresses his gratitude for you did not do the same.")
        input("Press enter to continue...")
        if "Broken Sword" in items:
            items.remove("Broken Sword")
            a = input(
                "I notice you have the Sword of Royalty. It's imbued with the exact magic needed to free me from this prison. Will you please free me?!?! I'll be greatly indebted to you if so. (Free/ Leave) ").lower()
            if a == "free":
                print("You pull out the Sword, and hold it to the statue.")
                input("Press enter to continue...")
                print(
                    "It begans glow brighter, and brighter, as the statue begans to crack. In one final burst of light the Sword crumbles to pieces, as the man that was once a statue is freed")
                input("Press enter to continue...")
                print(
                    "The man states his name is Draco, and that while imprisoned he has gained great power due to only being able to focus mentally on increasing his magic capibilities.")
                input("Press enter to continue...")
                print(
                    "As stated before, he pledges his life to you, and says you only need to say his name if his service is needed after which he vanishes...")
                items.append("Draco's Pledge of Service")
                print(
                    "You notice the wall where the statue once stood is a little feinter than the others appearing to hint that it's an illusion.")
                input("Press enter to continue...")
                print(
                    "You successfully put your hand through the wall confirming it's an illusion, and proceed to the space waiting on the other side.")
                game4()
            elif a == "leave":
                print("You turn your back to leave, and the statue states that you'll deeply regret your decision.")
                input("Press enter to continue...")
        elif "Broken Sword" not in items:
            print(
                "The statue states that magic is capable of freeing him from his prison, but you unfrotunately don't appear to have the amount necessary. He then states as a token of his appreciate for just a normal conversation, you can take the shorcut hidden just behind him by an illusuinary wall.")
            input("Press enter to continue...")
            print("You thank the statue, and wave goodbye as you walk through the aforementioned wall behind him.")
            input("Press enter to continue...")
            game4()
    elif a == "run":
        print("You run into a small space tucked away to the left that opens up more, and more the deeper you go.")
        input("Press enter to continue...")
        game3()


def game3():
    print("As you head further into the room")
    check.append("p3")
    a = input("You come to a space that has mmultiple doors; 4 in total. Which door do you enter? (1/2/3/4)")
    if a == "1":
        print("You head though Door 1...")
        input("Press enter to continue...")
        mon_chc()
    elif a == "2":
        print("You head though Door 2...")
        input("Press enter to continue...")
        mon_chc()
    elif a == "3":
        print("You head though Door 3...")
        input("Press enter to continue...")
        mon_chc()
    elif a == "4":
        print("You head though Door 4...")
        input("Press enter to continue...")
        mon_chc()


def game4():
    print(
        "As you continue on your journey. You notice the sound of running water. Do you follow the sound? (Y/N)").lower()
    if a == "y":
        print("You follow the sound for hours, but it never seems to get closer.")
        input("Press enter to continue...")
        print(
            "As you continue walking, you feel like little progress has been made if any at all. Do you turn around? (Y/N)").lower()
        if a == "y":
            print("You head back...")
            input("Press enter to continue...")
            print("1 hour goes by...")
            input("Press enter to continue...")
            print("2 hours go by...")
            input("Press enter to continue...")
            print("4 hours go by...")
            input("Press enter to continue...")
            print("You setup to rest for the night as you don't seem to be making any progress...")
            game5()
        elif a == "n":
            print("You keep walking...")
            input("Press enter to continue...")
            print("1 hour goes by...")
            input("Press enter to continue...")
            print("2 hours go by...")
            input("Press enter to continue...")
            print("4 hours go by...")
            input("Press enter to continue...")
            print("Finally, it seems as if the sound is getting louder. You push on...")
            input("Press enter to continue...")
            print("You finally come to a set of stairs that heads down further into this mysterious dungeon...")
            input("Press enter to continue...")
            print("Since you've come this far, you head in step by step...")
            input("Press enter to continue...")
            print("Finally you come to an iron door")
            input("Press enter to continue...")
            print("You finally come to a set of stairs that heads down further into this mysterious dungeon...")
            input("Press enter to continue...")


    elif a == "n":
        print("")


def game5():
    if a == "":
        pass
    elif a == "run":
        pass


intro()
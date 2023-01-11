import random
import time

# GAMBLING GAME
win1 = [7, 7, 7]
win2 = [5, 5, 5]
win3 = [7, 7, 5]
win4 = [5, 5, 7]
win5 = [7, 5, 7]
win6 = [5, 7, 5]

roll = []


def spin():
    money = 100
    while money > 0:
        del roll[:]
        print("$" + str(money))
        time.sleep(1)
        money -= 5
        print("$" + str(money))

        r1 = random.randint(0, 10)
        roll.append(r1)
        print(roll)
        time.sleep(1)
        r2 = random.randint(0, 10)
        roll.append(r2)
        print(roll)
        time.sleep(.75)
        r3 = random.randint(0, 10)
        roll.append(r3)
        print(roll)
        time.sleep(.50)

        if roll == win1:
            money += 500
            print("You won $500")
            print("You now have " + str(money) + " dollars!")
            x = input("Spin again? (Y/N)").lower()
            if x == "y":
                spin()
            elif x == "n":
                print("We'll be here when you're ready for more.")
        elif roll == win2:
            money += 250
            print("You won $500")
            print("You now have " + str(money) + " dollars!")
            x = input("Spin again? (Y/N)").lower()
            if x == "y":
                spin()
            elif x == "n":
                print("We'll be here when you're ready for more.")
        elif roll == win3:
            money += 50
            print("You won $500")
            print("You now have " + str(money) + " dollars!")
            x = input("Spin again? (Y/N)").lower()
            if x == "y":
                spin()
            elif x == "n":
                print("We'll be here when you're ready for more.")
        elif roll == win4:
            money += 50
            print("You won $500")
            print("You now have " + str(money) + " dollars!")
            x = input("Spin again? (Y/N)").lower()
            if x == "y":
                spin()
            elif x == "n":
                print("We'll be here when you're ready for more.")
        elif roll == win5:
            money += 50
            print("You won $500")
            print("You now have " + str(money) + " dollars!")
            x = input("Spin again? (Y/N)").lower()
            if x == "y":
                spin()
            elif x == "n":
                print("We'll be here when you're ready for more.")
        elif roll == win6:
            money += 50
            print("You won $500")
            print("You now have " + str(money) + " dollars!")
            roll.clear()
            x = input("Spin again? (Y/N)").lower()
            if x == "y":
                spin()
            elif x == "n":
                print("We'll be here when you're ready for more.")
        else:
            print("No Win")
            x = input("Spin again?")
            if x == "y":
                spin()
            elif x == "n":
                print("We'll be here when you're ready for more.")

    if money <= 0:
        print("You're out of money...")


print("Welcome to a Gambling Game!")
x = input("This game cost $5; would you like to play? (Y/N)").lower()
if x == "y":
    print("Alright! Just spin when you're ready.")
    time.sleep(1)
    input("Press enter to Spin!")
    spin()
elif x == "n":
    print("Ok, we'll be here when you're ready.")
else:
    print("That's not an option.")
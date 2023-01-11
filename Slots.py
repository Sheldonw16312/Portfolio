import random
import time

win1 = [7, 7, 7, 7]
win2 = [5, 5, 5, 5]
win3 = [7, 7, 5, 5]
win4 = [5, 5, 7, 7]

money = 100
while money > 0:
    money -= 5


    def slot1():
        x = random.randint(2, 7)
        return x


    def slot2():
        x = random.randint(2, 7)
        return x


    def slot3():
        x = random.randint(2, 7)
        return x


    def slot4():
        x = random.randint(2, 7)
        return x


    roll = [slot1(), slot2(), slot3(), slot4()]

    print(roll)
    print("************")

    if roll == win1:
        print("*********************")
        print("Jackpot! You won $100")
        print("*********************")
        time.sleep(.50)
        money += 100
        print(f"You have {money} dollars.")
        input("Spin...")
    elif roll == win2:
        print("*********************")
        print("Jackpot! You won $100")
        print("*********************")
        time.sleep(.50)
        money += 100
        print(f"You have {money} dollars.")
        input("Spin...")
    elif roll == win3:
        print("*********************")
        print("Jackpot! You won $50")
        print("*********************")
        time.sleep(.50)
        money += 50
        print(f"You have {money} dollars.")
        input("Spin...")
    elif roll == win4:
        print("*********************")
        print("Jackpot! You won $50")
        print("*********************")
        time.sleep(.50)
        money += 50
        print(f"You have {money} dollars.")
        input("Spin...")
    elif roll.count(7) == 3:
        print("*********************")
        print("Jackpot! You won $25")
        print("*********************")
        time.sleep(.50)
        money += 25
        print(f"You have {money} dollars.")
        input("Spin...")
    elif roll.count(5) == 3:
        print("*********************")
        print("Jackpot! You won $25")
        print("*********************")
        time.sleep(.50)
        money += 25
        print(f"You have {money} dollars.")
        input("Spin...")
    else:
        print(f"You have {money} dollars.")
        print("No win.")
        input("Spin...")

if money <= 0:
    print("You're out of money...")

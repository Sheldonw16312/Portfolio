import random

word = "hangman"
win = []
result = []


# Figure out how to clear list before each check

def win():
    for i in word:
        win.append(i)

    if win == result:
        print("You won!")
    else:
        guess()


def guess():
    lives = 7
    while lives > 0:
        g = input("Guess: ")
        if g in word:
            i = word.index(g)
            result[i] = g
            print(result)
            win()
        else:
            lives -= 1
            print("Incorrect")
            print(str(lives) + " remaining.")

    if lives == 0:
        print("You lose.")


def start():
    for i in word:
        result.append("-")

    print(result)
    guess()


start()
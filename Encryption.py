import random
import time

# Encrytion
name = input("What if your last name?").lower()


def encrypt():
    pw = input("Password: ")
    opt1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"]
    opt2 = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "+", "=", "<", ">", "?", ]
    opt3 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", ]
    scramble = []
    rescram1 = []
    rescram2 = []

    def scramp1():
        for i in pw:
            x = random.randint(0, 25)
            y = random.randint(0, 14)
            z = random.randint(0, 14)
            scramble.append(i)
            scramble.append(opt1[x])
            scramble.append(opt2[y])
            scramble.append(opt3[z])

    ##############################################
    scramp1()

    ##############################################
    def scramp2():
        x = int(len(scramble) / 2)
        for i in scramble:
            y = scramble.index(i)
            if y <= x:
                rescram1.append(i)
            else:
                rescram2.append(i)
        print("SCRAMBLED")
        z = (rescram2 + rescram1)
        y = *z

        print(y)

    ##############################################
    scramp2()
    ##############################################


encrypt()


###################################################
def decrypt(x):
    pass

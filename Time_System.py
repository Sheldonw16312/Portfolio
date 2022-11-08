import random
import time
from datetime import datetime

#
# Finish setting up ability to reset password
#
sec_answ = {}  # {id: security answer}
sec_question = {}  # {id: security question}
dir = {}  # {id: full name}
clocked_in = {}  # {id : time_in}
clocked_out = {}  # {id : time_out}
passwd = {}  # {id: password}


#
#
def forgot_pw():
    x = input("Enter your CID: ")
    print(sec_question[x])
    a = input("Enter the answer to your security question: ")

    def edit_pw():
        if a == sec_answ[x]:
            p = input("Set new password: ")
            cp = input("Confirm new password: ")
            if cp != p:
                print("Passwords do not match.")
                edit_pw()
            elif len(p) <= 7:
                print("Password does not meet length expectations.")
                edit_pw()
            elif cp.islower():
                print("Password does not contain an upppercase charcter.")
                edit_pw()
            elif cp == p:
                passwd[x] = cp
                print("Password is set. You can now login with new password.")
                login()
            else:
                print("Something went wrong...")
                edit_pw()

    edit_pw()


#
#
def login():
    x = input("Enter your CID: ")
    print("Forgot password? Enter 'fpwd' ")
    pswd = input("Enter your password: ")
    if pswd == "fpwd":
        forgot_pw()
    elif pswd != passwd[x]:
        print("Password Incorrect.")
        login()
    elif pswd == passwd[x]:
        print("Password Correct.")
        time.sleep(1.5)
        print("Welcome to the Earth System!")
        menu()


#
#
def new_user():
    first = input("What's your First name: ")
    last = input("What's your Last name: ")
    full_name = (last + ", " + first)
    print("Welcome to Earth " + full_name + "!")
    #
    #
    id = random.randint(100000, 999999)
    cid = last.lower() + str(id)
    dir[cid] = full_name
    print("Your Company ID is: " + str(cid))
    time.sleep(1.5)
    print("Please note this down for future reference.")
    time.sleep(1.5)
    input("Press enter to continue...")

    def pwd():
        print("***********************")
        print("Password Requirements: ")
        print("***********************")
        print("Must contain more than 7 characters.")
        print("Must contain at least one uppercase letter.")
        print("***********************")
        password = input("Set your password: ")
        #
        cpassword = input("Confirm your password: ")
        if cpassword != password:
            print("Passwords do not match.")
            pwd()
        elif len(password) <= 7:
            print("Password does not meet length expectations.")
            pwd()
        elif cpassword.islower():
            print("Password does not contain an upppercase charcter.")
            pwd()
        elif cpassword == password:
            passwd[cid] = cpassword
            print("Password is set.")
            security_question()
        else:
            print("Something went wrong...")
            pwd()

    def security_answer():
        x = input("Enter the answer to your security question: ")
        print(x)
        y = input("Does your answer appear correctly?(Y/N)").lower()
        if y == "y":
            sec_answ[cid] = x
            login()
        elif y == "n":
            print("Returning...")
            time.sleep(1)
            security_answer()

    def security_question():
        x = input("Enter your security question: ")
        print(x)
        y = input("Does your question appear correctly?(Y/N)").lower()
        if y == "y":
            sec_question[cid] = x
            security_answer()
        elif y == "n":
            print("Returning...")
            time.sleep(1)
            security_question()

    pwd()


#
#
def clock_in():
    clock = datetime.now()
    x = input("Please enter your Company ID: ")
    if x not in dir:
        print("Does not exist in company directory.")
        clock_in()
    else:
        if x in dir:
            if x in clocked_in:
                print("You're already clocked in.")
                print(clocked_in[x])
                input("Press enter to return to menu.")
                menu()
            else:
                clocked_in[x] = clock
                print("Welcome back " + dir[x])
                print("You clocked in at: " + str(clocked_in[x]))
                input("Press enter to return to menu.")
                menu()


#
#
def clock_out():
    clock = datetime.now()
    x = input("Please enter your Company ID: ")
    if x not in dir:
        print("Does not exist in company directory.")
        clock_out()
    else:
        if x in dir:
            if x in clocked_out:
                print("You're already clocked out.")
                print(clocked_out[x])
                input("Press enter to return to menu.")
                menu()
            else:
                clocked_in.pop(x)
                clocked_out[x] = clock
                print("Take Care " + dir[x])
                print("You clocked out at: " + str(clock))
                input("Press enter to return to menu.")

                menu()


#
#
def menu():
    x = input("Clocking In(in) / Clocking Out(out) / New User(new) / Administrator(admin) / Forgot Password?(fpwd) ").lower()
    if x == "in":
        clock_in()
    elif x == "out":
        clock_out()
    elif x == "new":
        new_user()
    elif x == "admin":
        ad_password()
    elif x == "fpwd":
        forgot_pw()
    else:
        print("That option doesn't exist.")
        menu()


#
#
def ad_password():
    admin_password = "123456"

    x = input("Admin Password: ")
    if x != admin_password:
        print("Password Incorrect.")
        ad_password()
    elif x == admin_password:
        print("Password Correct.")
        admin()
    else:
        print("That option doesn't exist.")
        ad_password()


def admin():
    print("What would you like to view: ")
    time.sleep(1.5)
    a = input("Clocked In Users(in) / Clocked Out Users(out) / All Users(all)").lower()

    if a == "in":
        print("Showing all users currently clocked in.")
        for i in clocked_in:
            print("**************************************")
            print(str(dir[i]) + " / " + str(clocked_in[i]))
            print("**************************************")
        input("Press enter to return to menu.")
        menu()
    if a == "out":
        print("Showing all users currently clocked out.")
        for i in clocked_out:
            print("**************************************")
            print(str(dir[i]) + " / " + str(clocked_out[i]))
            print("**************************************")
        input("Press enter to return to menu.")
        menu()
    if a == "all":
        print("Showing all users.")
        for i in dir:
            print("**************************************")
            print(dir[i])
            print("**************************************")
            input("Press enter to return to menu.")
            menu()
    else:
        print("That option doesn't exist.")
        admin()


#
#
menu()
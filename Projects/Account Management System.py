import random
import time
options = ["new", "returning", "Edit Account", "Forgot Password", "Forgot Email"]

def start():
  x = input("Welcome to Performance Tech. Are you new, or returning? (New/Returning)").lower()
  if x == "new":
    acc_setup()
  elif x == "returning":
    print("Welcome Back! How can I help you today?")
    time.sleep(1.5)
    x = input("Edit Account / Forgot Password / Forgot Email").lower()
    if x == "edit account":
      edit_acc()
    elif x == "forgot password":
      fpass()
    elif x == "forgot email":
      femail()
#email dict
emails = {}
#unique identifier dict
ui = {}
#passwords dict
passwords = {}

def acc_setup():
  first = input("What is your first name? ").lower()
  last = input("What is your last name? ").lower()
  birth_date = input("What is your birth date? (DD/MM/YYYY) ")
  question = input("Enter your preferred security question: ")
  answer = input("Enter the answer to your security question")
#
#
  def unique_id():
    x = str(random.randint(0,1000))
    y = str(random.randint(0,1000))
    z = x + y + last
    return z
#
#  {'unique id' : 'birthdate'}
  id = unique_id()
  ui[id] = birth_date
#
#
  def pw():
    password = input("Enter your password: ")
    cpass = input("Please confirm your password")
    if password != cpass:
      pw()
    else:
      return password
#
#
  x = pw()
  passwords.update({id:x})
  print(passwords)
#
#
  def email():
    workem = first + "." + last + "@mericah.com"
    return workem
#
#
  y = email()
  emails.update({id:y})
  print(emails)




start()
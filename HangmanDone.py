import random

def again():
  options = ["y", "yes", "n", "no"]
  a = input("Would you like to play again? ").lower()

  if a == "y" or "yes":
    game()
  elif a == "n" or "n":
    print("Come back anytime!")
    exit

def game():
  dict = dict = ["naruto", 
  "ichigo",
  "rukia",
  "sasuke",
  "saitama",
  "grimjow",
  "luffy",
  "zoro",
  "sanji",
  "chopper",
  "goku",
  "gogeta",
  "gon",
  "killua",
  "inuyasha",
  "sakura",
  "jiraiya",
  "mikasa",
  "eren",
  "frieza",
  "vegeta",
  "cell",
  "gohan",
  "piccolo",
  "my hero academia",
  "attack on titan",
  "chainsaw man",
  "dragon ball z",
  "deku",
  "aizen",
  ]
  
  print("***********************")
  print("**Welcome to Hangman!**")
  print("***********************")
  print("If you know the word. Just type it out.")
  
  r = random.randint(0, len(dict)-1)
  word = dict[r]
  g = [] #Code checks here and alters guessed letters to "-"
  dash = [] #Dash list / printed for user's to guess 
  graveyard = [] #used letters
  controlword = [] #list used to check for win
  
  for i in word:
    g.append(i)
    controlword.append(i)
  
  for i in g:
    dash.append("-")
    
  if " " in g:
    while " " in g:
      x = g.index(" ")
      dash[x] = " "
      g[x] = "-"
  
  print(*dash, sep = " ")
  
  guesses = 7
  
  
  while guesses > 0:
    print(f"You have {guesses} guesses.")
    
    if guesses == 7:
      print("""
      |-------|
      |       
      |
      |
      |
      |
      |
      |""")
    elif guesses == 6:
      print("""
      |-------|
      |       o
      |
      |
      |
      |
      |
      |""")
    elif guesses == 5:
      print("""
      |-------|
      |       o
      |
      |
      |
      |
      |
      |""")
    elif guesses == 4:
      print("""
      |-------|
      |       o
      |       |
      |
      |
      |
      |
      |""")
    elif guesses == 3:
      print("""
      |-------|
      |       o
      |       |
      |       |
      |
      |
      |
      |""")
    elif guesses == 2:
      print("""
      |-------|
      |       o
      |      /|\\
      |       |
      |
      |
      |
      |""")
    elif guesses == 1:
      print("""
      |-------|
      |       o
      |      /|\\
      |       |
      |      /
      |
      |
      |""")
    
    guess = input("Guess: ").lower()
    
    if guess in graveyard:
      print("You've said that already")
    elif len(guess) > 1:
      if guess == word:
        print("You Saved Him!!!")
        print("""
        |-------|
        |       
        |   
        |       
        |          O/
        |         /|
        |          |
        |         /\  """)
        print(f"The word was '{word}'!!!")
        again()
      else:
        print("That is not correct.")
        guesses -= 1
    elif guess in g:
      graveyard.append(guess)
      print("Yes!")
      while guess in g:
        x = g.index(guess)
        dash[x] = guess
        g[x] = "-"
    elif guess not in g:
      graveyard.append(guess)
      print(f"Their are no {guess}'s.")
      guesses -= 1
      
    if dash == controlword:
      print(*dash, sep = " ")
      print("You Saved Him!!!")
      print("""
        |-------|
        |       
        |   
        |       
        |          O/
        |         /|
        |          |
        |         /\  """)
      
      again()
    elif guesses <= 0:
      print("You Killed Him!!!")
      print("""
      |-------|
      |       o
      |      /|\\
      |       |
      |      /\\
      |
      |
      |""")
      print(f"The word is '{word}'...")
      again()
        
    print(*dash, sep = " ")
    
game()
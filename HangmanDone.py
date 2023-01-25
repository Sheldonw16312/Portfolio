import random
dict = ["naruto", 
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
]
r = random.randint(0, len(dict)-1)
word = dict[r]
g = [] #Code checks here
dash = [] #Dash list
graveyard = []
controlword = []

for i in word:
  g.append(i)
  controlword.append(i)

for i in g:
  dash.append("-")

print(*dash, sep = " ")

guesses = 7

while guesses > 0:
  print(f"You have {guesses} guesses.")
  
  guess = input("Guess: ").lower()
  
  if guess in graveyard:
    print("You've said that already")
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
    break
  elif guesses <= 0:
    print("You Killed Him!!!")
    print(f"The word is '{word}'...")
      
  print(*dash, sep = " ")
import random
import time

class Player:
  def __init__(self, name, health, attack, speed, victories, diamonds, inventory, difficulty):
    self.name = name
    self.health = health
    self.attack = attack
    self.speed = speed
    self.victories = victories
    self.diamonds = diamonds
    self.inventory = inventory
    self.difficulty = difficulty

class Monsters:
  def __init__(self, name, health, attack, speed):
    self.name = name
    self.health = health
    self.attack = attack
    self.speed = speed

#------------------------------------------------------------- 
#Player
name = input("What is your name?")
time.sleep(.5)
print(f"welcome to Planet Skaar {name}!!!")
p = Player("", 100, "p", 10, 0, 0, " ", "e")
p.name = name
#Set 1  Easy
s = Monsters("Slime", 30, "e", 15)
b = Monsters("Bandit", 35, "e", 15)
d = Monsters("Druid", 40, "e", 14)
l = Monsters("Lycan", 45, "e", 13)
v = Monsters("Vampire", 50, "e", 13)
#-------------------------------------------------------------
#Set 2 Medium
m = Monsters("Minotaur", 60, "m", 12)
t = Monsters("Troll", 65, "m", 12)
o = Monsters("Ogre", 70, "m", 11)
ck = Monsters("Corrupted Knight", 75, "m", 10)
c = Monsters("Cyclops", 80, "m", 11)
#-------------------------------------------------------------
#Set 3 Hard
chi = Monsters("Chimera", 100, "h", 10)
r = Monsters("Reaper", 105, "h", 10)
g = Monsters("Griffin", 110, "h", 9)
champ = Monsters("Champion", 120, "h", 6)
#-------------------------------------------------------------
#Monster Attack
def ma(x):
  if x == "e":
    attack = random.randint(5, 15)
    return attack
  elif x == "m" or "p":
    attack = random.randint(10, 20)
    return attack
  elif x == "h":
    attack = random.randint(15, 25)
    return attack

#-------------------------------------------------------------
#Inventory
p.inventory = []
def inv():
  print(p.inventory)
  time.sleep(.5)
  a = input("Would you like to use an item?").lower()
  
  if a == "y":
    a = input("Choose Item: ").lower()
    if a == "hp":
      p.health += 10
      p.inventory.remove("HP")
      time.sleep(.5)
      print(f"{p.name} healed 10HP!")
      time.sleep(.5)
      return
    elif a == "hp hp":
      p.health += 20
      p.inventory.remove("HP HP")
      time.sleep(.5)
      print(f"{p.name} healed 20HP!")
      time.sleep(.5)
      return
    elif a == "full heal":
      p.health += 100
      p.inventory.remove("Full Heal")
      time.sleep(.5)
      print(f"{p.name} fully recovered!")
      time.sleep(.5)
      return
  elif a == "n":
    return
  
 #-------------------------------------------------------------
#Continue

def cont():
  time.sleep(.5)
  print("Would you like to change the difficulty?")
  a = input("Y/N").lower()
  
  if a == "y":
    main()
  elif a == "n":
    time.sleep(.5)
    print("Your next opponent will be...")
    opponent(p.difficulty)

#-------------------------------------------------------------
#Sets player health back to 100
def recover():
  p.health = 100
  shop()

#-------------------------------------------------------------
#Dodge
def dodged(x):
  chance = random.randint(1, x)
  
  if chance == x:
    return "dodged"
  else:
    return "hit"

#-------------------------------------------------------------
#Currency = Diamonds Easy(10) Medium(15) Hard(45)
#Shop defined below
def shop():
  items = {"HP" : 20, "HP HP" : 30, "Full Heal" : 60}
  print("********************************")
  for i in items:
    print(i, " : ", items[i])
  print("********************************")
  print(f"You have {p.diamonds} diamonds.")
  
  buy = input("What would you like to buy?").lower()
  
  
  if buy == "hp":
    x = items.get("HP")
    y = p.diamonds - x
    if y < 0:
      time.sleep(.5)
      print("You don't have enough diamonds for that.")
      shop()
    else:
      time.sleep(.5)
      p.diamonds -= items["HP"]
      p.inventory.insert(0, "HP")
      print("You bought a HP")
      print(f"Diamonds Remaing: {p.diamonds}")
      cont()
  elif buy == "hp hp":
    x = items.get("HP HP")
    y = p.diamonds - x
    if y < 0:
      time.sleep(.5)
      print("You don't have enough diamonds for that.")
      shop()
    else:
      time.sleep(.5)
      time.sleep(.5)
      p.diamonds -= items["HP HP"]
      p.inventory.insert(0, "HP HP")
      print("You bought a HP HP")
      print(f"Diamonds Remaing: {p.diamonds}")
      cont()
  elif buy == "full heal":
    x = items.get("Full Heal")
    y = p.diamonds - x
    if y < 0:
      time.sleep(.5)
      print("You don't have enough diamonds for that.")
      shop()
    else:
      time.sleep(.5)
      p.diamonds -= items["Full Heal"]
      p.inventory.insert(0, "Full Heal")
      print("You bought a Full Heal")
      print(f"Diamonds Remaing: {p.diamonds}")
      cont()
  elif buy == "n" or "none" or "nothing":
    time.sleep(.5)
    print("No worries, good luck out there!")
    cont()
  else:
    time.sleep(.5)
    print("I'm not sure what you said...")
    shop()

#-------------------------------------------------------------
#Function below ask player for difficulty and choose opponent
def opponent(x):
  
  def easy():
    r = random.randint(1,5)
    
    
    if r == 1:
      #-------------------------------------------------------------
      print("A Slime!")
      while p.health > 0 and s.health > 0:
        patt = ma(p.attack)
        satt = ma(s.attack)
        dodge(p.speed)
        dodge(s.speed)
        
        if dodge(s.speed) == "dodged" and dodge(p.speed) == "dodged":
          print("Both fighters dodged!")
        elif pdodge == "dodge":
          print(f"{name} dodged causing the Slime to miss it's attack!")
        elif pdodge == "dodge":
          print(f"The Slime dodged causing {name} to miss his attack!")
        elif dodge(p.speed) == "dodge" and dodge(s.speed) == "hit":
          s.health -= patt
          print(f"{name} dodged and attacked the Slime for {patt} HP.")
          print("********************************************")
          print(f"Player HP: {p.health} | Slime HP: {s.health}")
          print("********************************************")
        elif dodge(p.speed) == "hit" and dodge(s.speed) == "dodged":
          p.health -= satt
          print(f"The Slime dodged and attacked {name} for {satt} HP.")
          print("********************************************")
          print(f"Player HP: {p.health} | Slime HP: {s.health}")
          print("********************************************")
        else:
          
          time.sleep(.5)
          print("********************************************")
          print(f"Player HP: {p.health} | Slime HP: {s.health}")
          print("********************************************")
          p.health -= satt
          s.health -= patt
          time.sleep(.5)
          print(f"{p.name} hit Slime for {patt} HP")
          time.sleep(.5)
          print(f"The Slime hit {p.name} for {satt} HP")
          time.sleep(.5)
          print("********************************************")
          print(f"Player HP: {p.health} | Slime HP: {s.health}")
          print("********************************************")
          
          a = input("continue?(Press Enter) Item?(Type Inv)")
          
          if a == "inv":
            inv()
      
      if p.health <= 0 and s.health <= 0:
        print("It appears they took each other out!!!")
      elif p.health <= 0:
        print("You Lost.")
      elif s.health <= 0:
        print(f"{p.name} Won!")
        p.diamonds += 10
        p.victories += 1
        s.health = 30
        recover()
        
    elif r == 2:
      #-------------------------------------------------------------
      print("A Bandit!")
      while p.health > 0 and b.health > 0:
        patt = ma(p.attack)
        batt = ma(b.attack)
        time.sleep(.5)
        print("********************************************")
        print(f"Player HP: {p.health} | Bandit HP: {b.health}")
        print("********************************************")
        p.health -= batt
        b.health -= batt
        time.sleep(.5)
        print(f"{p.name} hit The Bandit for {patt} HP")
        time.sleep(.5)
        print(f"The Slime hit {p.name} for {batt} HP")
        time.sleep(.5)
        print(f"********************************************")
        print(f"Player HP: {p.health} | Bandit HP: {b.health}")
        print(f"********************************************")
        
        a = input("continue?(Press Enter) Item?(Type Inv)")
        
        if a == "inv":
          inv()
      
      if p.health <= 0 and b.health <= 0:
        print("It appears they took each other out!!!")
      elif p.health <= 0:
        print("You Lost.")
      elif b.health <= 0:
        print(f"{p.name} Won!")
        p.diamonds += 10
        p.victories += 1
        b.health = 35
        recover()
    elif r == 3:
      #-------------------------------------------------------------
      print("A Druid!")
      while p.health > 0 and d.health > 0:
        patt = ma(p.attack)
        datt = ma(d.attack)
        time.sleep(.5)
        print("********************************************")
        print(f"Player HP: {p.health} | Druid HP: {d.health}")
        print("********************************************")
        p.health -= datt
        d.health -= patt
        time.sleep(.5)
        print(f"{p.name} hit Slime for {patt} HP")
        time.sleep(.5)
        print(f"The Druid hit {p.name} for {datt} HP")
        time.sleep(.5)
        print(f"********************************************")
        print(f"Player HP: {p.health} | Druid HP: {d.health}")
        print(f"********************************************")
        
        a = input("continue?(Press Enter) Item?(Type Inv)")
        
        if a == "inv":
          inv()
      
      if p.health <= 0 and d.health <= 0:
        print("It appears they took each other out!!!")
      elif p.health <= 0:
        print("You Lost.")
      elif d.health <= 0:
        print(f"{p.name} Won!")
        p.diamonds += 10
        p.victories += 1
        d.health = 40
        recover()
    elif r == 4:
      #-------------------------------------------------------------
      print("A Lycan!")
      while p.health > 0 and l.health > 0:
        patt = ma(p.attack)
        latt = ma(l.attack)
        time.sleep(.5)
        print(f"********************************************")
        print(f"Player HP: {p.health} | Lycan HP: {l.health}")
        print(f"********************************************")
        p.health -= latt
        l.health -= patt
        time.sleep(.5)
        print(f"{p.name} hit The Lycan for {patt} HP")
        time.sleep(.5)
        print(f"The Lycan hit {p.name} for {latt} HP")
        time.sleep(.5)
        print("********************************************")
        print(f"Player HP: {p.health} | Lycan HP: {l.health}")
        print("********************************************")
        
        a = input("continue?(Press Enter) Item?(Type Inv)")
        
        if a == "inv":
          inv()
      
      if p.health <= 0 and l.health <= 0:
        print("It appears they took each other out!!!")
      elif p.health <= 0:
        print("You Lost.")
      elif l.health <= 0:
        print(f"{p.name} Won!")
        p.diamonds += 10
        p.victories += 1
        l.health = 45
        recover()
    elif r == 5:
      #-------------------------------------------------------------
      print("A Vampire!")
      while p.health > 0 and v.health > 0:
        patt = ma(p.attack)
        vatt = ma(v.attack)
        time.sleep(.5)
        print("********************************************")
        print(f"Player HP: {p.health} | Vampire HP: {v.health}")
        print("********************************************")
        p.health -= vatt
        v.health -= patt
        time.sleep(.5)
        print(f"{p.name} hit The Vampire for {patt} HP")
        time.sleep(.5)
        print(f"The Vampire hit {p.name} for {vatt} HP")
        time.sleep(.5)
        print(f"********************************************")
        print(f"Player HP: {p.health} | Vampire HP: {v.health}")
        print(f"********************************************")
        
        a = input("continue?(Press Enter) Item?(Type Inv)")
        
        if a == "inv":
          inv()
      
      if p.health <= 0 and v.health <= 0:
        print("It appears they took each other out!!!")
      elif p.health <= 0:
        print("You Lost.")
      elif v.health <= 0:
        print(f"{p.name} Won!")
        p.diamonds += 10
        p.victories += 1
        v.health = 50
        recover()
  
  def medium():
    r = random.randint(1,5)
    
    if r == 1:
      #-------------------------------------------------------------
      print("A Minotaur!")
      while p.health > 0 and m.health > 0:
        patt = ma(p.attack)
        matt = ma(m.attack)
        time.sleep(.5)
        print("********************************************")
        print(f"Player HP: {p.health} | Minotaur HP: {m.health}")
        print("********************************************")
        p.health -= matt
        m.health -= patt
        time.sleep(.5)
        print(f"{p.name} hit The Minotaur for {patt} HP")
        time.sleep(.5)
        print(f"The Minotaur hit {p.name} for {matt} HP")
        time.sleep(.5)
        print("********************************************")
        print(f"Player HP: {p.health} |Minotaur HP: {m.health}")
        print("********************************************")
        
        a = input("continue?(Press Enter) Item?(Type Inv)")
        
        if a == "inv":
          inv()
      
      if p.health <= 0 and m.health <= 0:
        print("It appears they took each other out!!!")
      elif p.health <= 0:
        print("You Lost.")
      elif m.health <= 0:
        print(f"{p.name} Won!")
        p.diamonds += 15
        p.victories += 1
        m.health = 60
        recover()
    elif r == 2:
      #-------------------------------------------------------------
      print("A Troll!")
      while p.health > 0 and t.health > 0:
        patt = ma(p.attack)
        tatt = ma(t.attack)
        time.sleep(.5)
        print("********************************************")
        print(f"Player HP: {p.health} | Troll HP: {t.health}")
        print("********************************************")
        p.health -= satt
        s.health -= patt
        time.sleep(.5)
        print(f"{p.name} hit The Troll for {patt} HP")
        time.sleep(.5)
        print(f"The Troll hit {p.name} for {tatt} HP")
        time.sleep(.5)
        print("********************************************")
        print(f"Player HP: {p.health} | Troll HP: {t.health}")
        print("********************************************")
        
        a = input("continue?(Press Enter) Item?(Type Inv)")
        
        if a == "inv":
          inv()
      
      if p.health <= 0 and t.health <= 0:
        print("It appears they took each other out!!!")
      elif p.health <= 0:
        print("You Lost.")
      elif t.health <= 0:
        print(f"{p.name} Won!")
        p.diamonds += 15
        p.victories += 1
        t.health = 65
        recover()
    elif r == 3:
      #-------------------------------------------------------------
      print("An Ogre!")
      while p.health > 0 and s.health > 0:
        patt = ma(p.attack)
        oatt = ma(o.attack)
        time.sleep(.5)
        print("********************************************")
        print(f"Player HP: {p.health} | Ogre HP: {o.health}")
        print("********************************************")
        p.health -= oatt
        o.health -= patt
        time.sleep(.5)
        print(f"{p.name} hit The Ogre for {patt} HP")
        time.sleep(.5)
        print(f"The Ogre hit {p.name} for {oatt} HP")
        time.sleep(.5)
        print("********************************************")
        print(f"Player HP: {p.health} | Ogre HP: {o.health}")
        print("********************************************")
        
        a = input("continue?(Press Enter) Item?(Type Inv)")
        
        if a == "inv":
          inv()
      
      if p.health <= 0 and o.health <= 0:
        print("It appears they took each other out!!!")
      elif p.health <= 0:
        print("You Lost.")
      elif o.health <= 0:
        print(f"{p.name} Won!")
        p.diamonds += 15
        p.victories += 1
        o.health = 70
        recover()
    elif r == 4:
      #-------------------------------------------------------------
      print("A Corrupted Knight!")
      while p.health > 0 and ck.health > 0:
        patt = ma(p.attack)
        ckatt = ma(ck.attack)
        time.sleep(.5)
        print("********************************************")
        print(f"Player HP: {p.health} | Corrupted Knight HP: {ck.health}")
        print("********************************************")
        p.health -= ckatt
        ck.health -= patt
        time.sleep(.5)
        print(f"{p.name} hit The Corrupted Knight for {patt} HP")
        time.sleep(.5)
        print(f"The Corrupted Knight hit {p.name} for {satt} HP")
        time.sleep(.5)
        print("********************************************")
        print(f"Player HP: {p.health} | The Corrupted Knight HP: {o.health}")
        print("********************************************")
        
        a = input("continue?(Press Enter) Item?(Type Inv)")
        
        if a == "inv":
          inv()
      
      if p.health <= 0 and ck.health <= 0:
        print("It appears they took each other out!!!")
      elif p.health <= 0:
        print("You Lost.")
      elif ck.health <= 0:
        print(f"{p.name} Won!")
        p.diamonds += 10
        ck.health = 75
        recover()
    elif r == 5:
      #-------------------------------------------------------------
      print("A Cyclops!")
      while p.health > 0 and c.health > 0:
        patt = ma(p.attack)
        catt = ma(c.attack)
        time.sleep(.5)
        print("********************************************")
        print(f"Player HP: {p.health} | Cyclops HP: {c.health}")
        print("********************************************")
        p.health -= catt
        c.health -= patt
        time.sleep(.5)
        print(f"{p.name} hit The Cyclops for {patt} HP")
        time.sleep(.5)
        print(f"The Cyclops hit {p.name} for {catt} HP")
        time.sleep(.5)
        print("********************************************")
        print(f"Player HP: {p.health} | Cyclops HP: {c.health}")
        print("********************************************")
        
        a = input("continue?(Press Enter) Item?(Type Inv)")
        
        if a == "inv":
          inv()
      
      if p.health <= 0 and c.health <= 0:
        print("It appears they took each other out!!!")
      elif p.health <= 0:
        print("You Lost.")
      elif c.health <= 0:
        print(f"{p.name} Won!")
        p.diamonds += 15
        p.victories += 1
        c.health = 80
        recover()
  
  def hard():
    r = random.randint(1,4)
    
    if r == 1:
      #-------------------------------------------------------------
      print("A Chimera!")
      while p.health > 0 and chi.health > 0:
        patt = ma(p.attack)
        chiatt = ma(chi.attack)
        time.sleep(.5)
        print("********************************************")
        print(f"Player HP: {p.health} | Chimera HP: {chi.health}")
        print("********************************************")
        p.health -= chiatt
        chi.health -= patt
        time.sleep(.5)
        print(f"{p.name} hit The Chimera for {patt} HP")
        time.sleep(.5)
        print(f"The Chimera hit {p.name} for {chiatt} HP")
        time.sleep(.5)
        print("********************************************")
        print(f"Player HP: {p.health} | Chimera HP: {chi.health}")
        print("********************************************")
        
        a = input("continue?(Press Enter) Item?(Type Inv)")
        
        if a == "inv":
          inv()
      
      if p.health <= 0 and chi.health <= 0:
        print("It appears they took each other out!!!")
      elif p.health <= 0:
        print("You Lost.")
      elif chi.health <= 0:
        print(f"{p.name} Won!")
        p.diamonds += 20
        p.victories += 1
        chi.health = 100
        recover()
    elif r == 2:
      #-------------------------------------------------------------
      print("A Reaper!")
      while p.health > 0 and r.health > 0:
        patt = ma(p.attack)
        ratt = ma(r.attack)
        time.sleep(.5)
        print("********************************************")
        print(f"Player HP: {p.health} | Reaper HP: {r.health}")
        print("********************************************")
        p.health -= satt
        s.health -= patt
        time.sleep(.5)
        print(f"{p.name} hit The Reaper for {patt} HP")
        time.sleep(.5)
        print(f"The Reaper hit {p.name} for {ratt} HP")
        time.sleep(.5)
        print("********************************************")
        print(f"Player HP: {p.health} | Reaper HP: {r.health}")
        print("********************************************")
        
        a = input("continue?(Press Enter) Item?(Type Inv)")
        
        if a == "inv":
          inv()
      
      if p.health <= 0 and r.health <= 0:
        print("It appears they took each other out!!!")
      elif p.health <= 0:
        print("You Lost.")
      elif r.health <= 0:
        print(f"{p.name} Won!")
        p.diamonds += 20
        p.victories += 1
        r.health = 105
        recover()
    elif r == 3:
      #-------------------------------------------------------------
      print("A Griffin!")
      while p.health > 0 and g.health > 0:
        patt = ma(p.attack)
        gatt = ma(g.attack)
        time.sleep(.5)
        print("********************************************")
        print(f"Player HP: {p.health} | Griffin HP: {g.health}")
        print("********************************************")
        p.health -= gatt
        g.health -= patt
        time.sleep(.5)
        print(f"{p.name} hit The Griffin for {patt} HP")
        time.sleep(.5)
        print(f"The Griffin hit {p.name} for {gatt} HP")
        time.sleep(.5)
        print("********************************************")
        print(f"Player HP: {p.health} | Griffin HP: {g.health}")
        print("********************************************")
        
        a = input("continue?(Press Enter) Item?(Type Inv)")
        
        if a == "inv":
          inv()
      
      if p.health <= 0 and g.health <= 0:
        print("It appears they took each other out!!!")
      elif p.health <= 0:
        print("You Lost.")
      elif g.health <= 0:
        print(f"{p.name} Won!")
        p.diamonds += 20
        p.victories += 1
        g.health = 110
        recover()
    elif r == 4:
      #-------------------------------------------------------------
      print("The Champion!")
      while p.health > 0 and champ.health > 0:
        patt = ma(p.attack)
        champatt = ma(champ.attack)
        time.sleep(.5)
        print("********************************************")
        print(f"Player HP: {p.health} | Champion HP: {champ.health}")
        print("********************************************")
        p.health -= champatt
        champ.health -= patt
        time.sleep(.5)
        print(f"{p.name} hit The Champion for {patt} HP")
        time.sleep(.5)
        print(f"The Champion hit {p.name} for {champatt} HP")
        time.sleep(.5)
        print("********************************************")
        print(f"Player HP: {p.health} | Champion HP: {champ.health}")
        print("********************************************")
        
        a = input("continue?(Press Enter) Item?(Type Inv)")
        
        if a == "inv":
          inv()
      
      if p.health <= 0 and champ.health <= 0:
        print("It appears they took each other out!!!")
      elif p.health <= 0:
        print("You Lost.")
      elif champ.health <= 0:
        print(f"{p.name} Won!")
        p.diamonds += 25
        p.victories += 1
        champ.health = 120
        recover()
  
  if x == "e":
    easy()
  elif x == "m":
    medium()
  elif x == "h":
    hard()

def main():
  time.sleep(.5)
  print("Difficulty?")
  p.difficulty = input("E/M/H").lower()
  time.sleep(.5)
  print("Are you ready?")
  a = input("Y/N").lower()
  
  if a == "y":
    time.sleep(.5)
    print("Your opponent will be...")
    time.sleep(.5)
    opponent(p.difficulty)
    
  elif a == "n":
    time.sleep(.5)
    print("Well come back when you're ready. We'll be here.")

main()

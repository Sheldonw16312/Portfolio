import time
from datetime import datetime

#DataLogger

print("Press 'q' anytime to quit. Press 'd' to display log.")

def display():
  f = open("BloodPressureLogs.txt", "r")
  print(f.read())
  log()

def log():
  date = ""
  bp = ""
  dictbp = {}
  dicthr = {}
  hr = 0
  
  while True:
    t = datetime.now()
    
    bp = input("Blood Pressure: ").lower()
    if bp == "q":
      break
    elif bp == "d":
      display()
    else:
      if hr == "q":
        break
      elif hr == "d":
        display()
      else:
        hr = input("Heart Rate: ").lower()
  
    dictbp[t] = "Blood Pressure: " + str(bp)
    dicthr[t] = "Heart Rate: " + str(hr)
    
    f = open("BloodPressureLogs.txt", "a")
    f.write("******************** \nDate: " + str(t))
    f.write(" \nBlood Pressure: " + str(bp) + "\nHeart Rate: " + str(hr) + "\n********************")
    f.close()
    
log()

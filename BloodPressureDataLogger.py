#DataLogger

print("Press 'q' anytime to quit.")

date = ""
bp = ""
dictbp = {}
dicthr = {}
hr = 0

while date != "q" and bp != "q":
  
  date = input("Date: ")
  if date == "q":
    break
  else:
    bp = input("Blood Pressure: ")
    if bp == "q":
      break
    else:
      if hr == "q":
        break
      else:
        hr = input("Heart Rate: ")

  dictbp[date] = "Blood Pressure: " + str(bp)
  dicthr[date] = "Heart Rate: " + str(hr)
  
  f = open("BloodPressureLogs.txt", "a")
  f.write("\nDate: " + date)
  f.write(" \nBlood Pressure: " + str(bp) + "\nHeart Rate: " + str(hr))
  f.close()
  
f = open("BloodPressureLogs.txt", "r")
print(f.read())

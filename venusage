#this program takes your current age and converts it into your venus age.
import datetime

name = input("What is your name?")
dob = int(input("What year were you born?"))
today = datetime.datetime.now().year
age = today - dob
venusage = int(age // 0.62) #divided with floor, because humans don't generally say their age as a decimal number.

if age > 0:
  print(name + ", your current age on earth is " + str(age) + " years old.")
  print(name + ", your current age on venus is " + str(venusage) + " years old.")

else:
  print("You haven't been born yet!")

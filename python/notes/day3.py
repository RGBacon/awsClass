############################################################
# Rock Paper Scissors
# Random choose a random choice
# Ask user to input choice
# Conditional statements
# Jeremy
############################################################

import random

win = "You WIN!"
lose = "You lose :( try again"
choice = ["Rock", "Paper", "Scissors"]
# AI first, player 2nd
score = [0, 0]

while True:
  print("Current Score")
  print("AI: " + str(score[0]) + " | Player: " + str(score[1]))
  player = input("Rock, Paper or Scissors?: ").capitalize()
  ai = random.choice(choice)

  # Conditions of RPS game

  # If Tie
  if player == ai:
    print("Tie!")
  # If Rock
  elif player == "Rock":
    if ai == "Scissors":
      print(win)
      score[1] += 1
    else:
      print(lose)
      score[0] += 1
  # If Paper
  elif player == "Paper":
    if ai == "Rock":
      print(win)
      score[1] += 1
    else:
      print(lose)
      score[0] += 1
  # If Scissors
  elif player == "Scissors":
    if ai == "Paper":
      print(win)
      score[1] += 1
    else:
      print(lose)
      score[0] += 1

############################################################
#back from break 11am
#accepts input, prints it back untill "stop" is said then it breaks the loop
############################################################
while True:
  reply = input("Enter Text: ")
  if reply == "stop": break
  else:
    print(reply)

############################################################
# Inputs
############################################################
response = input("What is your name? :")

print("Thank you " + response)

###############################################################
# Dict
###############################################################
carDict = {"Brand": "Mercedes", "Model": "S-Class", "Year": 2025}

print(carDict["Brand"])

############################################################
#creating a list of numbers
#loop through list
#square list and update
############################################################
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

count = 0
for i in numbers:
  #print(i**2)
  numbers[count] = i**2
  count += 1
print(numbers)
############################################################
#creating a list
############################################################
hospitalRobert = ["Robert", "Doe", "5ft5in", 170, "O Neg", False]
print(hospitalRobert)
print(hospitalRobert[1])

############################################################
#testing if you can multiply 0
############################################################
print(0 * 2)
#wow it works prints out 0

############################################################
#more while loop stuff
############################################################
counter = 0

#loops 4 times because starts at 0
while counter <= 3:
  print("I love learning Python!")
  counter += 1

#voting example of a loop

hasVoted = False

while hasVoted == False:
  print("Who do you vote for?")
  hasVoted = True

############################################################
#print statment for every score range
############################################################
score = int(input("Enter Score: "))

if score > 100:
  print("Woah! You probably cheated")
  print(score)
elif score > 90:
  print("Great job! You did excellent on the exam!")
  print(score)
elif score > 80:
  print("Great job! You did excellent on the exam!")
  print(score)
elif score > 70:
  print("Great job! You did excellent on the exam!")
  print(score)
elif score > 60:
  print("Great job! You did excellent on the exam!")
  print(score)
elif score > 50:
  print("Great job! You did excellent on the exam!")
  print(score)
elif score > 40:
  print("Wow a real talent! You chose all of the wrong answers!")
  print(score)
else:
  print("You really blew this one huh")
  print(score)

print("Goodbye")

#starting off the day with IF and ELIF and ELSE
age = 23


# IS AGE >= 18 IF THAT IS TRUE:
if age >= 18:
  print("adult")
  print("ray")

#
elif age >= 13:
  print("teen")
else:
  print("child")





if age < 13:
  print("child")
elif age < 17:
  print("teen")
else:
  print("adult")
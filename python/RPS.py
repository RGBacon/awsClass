############################################################
# Rock Paper Scissors
# Random choose a random choice
# Ask user to input choice
# Conditional statements
# If same print lie, else print winner
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
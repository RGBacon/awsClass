# Rock Paper Scissors
# Jeremy

import random

choice = ["Rock", "Paper", "Scissors"]
# AI first, player 2nd
score = [0, 0]

while True:
  print(f"Current Score\nAI: {score[0]} | Player: {score[1]}")
  player = input("Rock, Paper or Scissors?: ").capitalize()
  ai = random.choice(choice)

  # Conditions of RPS game
  winners = {"Rock": "Scissors", 
             "Paper": "Rock", 
             "Scissors": "Paper"}

  # If Tie
  if player == ai:
    print("Tie!")
  # If Rock
  elif winners[player] == ai:
    print("You WIN!")
    score[1] += 1
  else:
    print("You lose :( try again")
    score[0] += 1
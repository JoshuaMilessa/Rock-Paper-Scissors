import random

user_wins = 0 
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
  user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
  if user_input == "q":
    quit()

  if user_input not in ["rock", "paper", "scissors"]:
    continue

  randon_number = random.randint(0, 2)
  # rock: 0, paper: 1, scissors: 2
  
  computer_pick = options[randon_number]
  print("Computer picked", computer_pick + ".")

  if (user_input == "rock" and computer_pick == "scissors") or (user_input == "paper" and computer_pick == "rock"):
    print("You won!")
    user_wins += 1
    continue 

  else: 
    print("You lost!")
    computer_wins += 1
  
  print("You won", user_wins, "times.")
  print("The computer won", computer_wins, "times.")
  print("Goodbye!")

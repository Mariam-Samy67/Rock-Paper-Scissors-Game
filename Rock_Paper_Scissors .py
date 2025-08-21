import random
rock = """
    -------
---'    _____)
       (_____)
       (_____)
       (____)
---.__ (___)
"""
paper = """
    _______
---'   ____)____
          ______)
          _______)
          ______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       _________)
      (____)
---.__(___)
"""
print("welcome to the rock, paper, scissors game: ")
rules = input("press enter to continue or type (help) for the rules ").lower()
if rules == "help":
    print("""********Rules******* 
             1) you choose and the computer chooses 
             2) rock smashes scissors -> rock wins 
             3) scissors cut paper -> scissors win 
             4) paper covers rock -> paper wins""")
user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
if user_choice not in ["rock", "paper", "scissors"]:
    print("invalid choice. Please run the program again and choose rock, paper, or scissors.")
    if user_choice == "rock":
        print(f"\nYou chose:\n{rock}")
    elif user_choice == "paper":
        print(f"\nYou chose:\n{paper}")
    else:
        print(f"\nYou chose:\n{scissors}")
computer_choice = random.choice(["rock", "paper", "scissors"])
if computer_choice == "rock":
    print(f"\ncomputer chose:\n{rock}")
elif computer_choice == "paper":
    print(f"\ncomputer choice:\n{paper}")
else:
    print(f"computer choice:\n{scissors}")

if computer_choice == user_choice:
    print("It`s a tie!")
elif (
     (user_choice == "rock" and computer_choice == "scissors")
     or
     (user_choice == "paper" and computer_choice == "rock")
     or
     (user_choice == "scissors" and computer_choice == "paper")):
    print(f"You win! {user_choice} beats {computer_choice}.")
else:
    print(f"You lose! {computer_choice} beats {user_choice}.")



    

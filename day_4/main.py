import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

moves = [rock, paper, scissors]

print("Welcome to Rock, Paper, Scissors")
player_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)
if player_choice >= 3 or player_choice < 0:
    print("You typed an invalid number, You loose")
else:
    print(f'Player: {moves[player_choice]}')
    print(f'Computer: {moves[computer_choice]}')

    if player_choice == 0 and computer_choice == 2:
        print("You Win!")
    elif computer_choice == 0 and player_choice == 2:
        print("You Lose!")
    elif player_choice == 2 and computer_choice == 1:
        print("You Win!")
    elif player_choice == 1 and computer_choice == 0:
        print("You Win!")
    elif computer_choice > player_choice:
        print("You Lose!")
    elif player_choice == computer_choice:
        print("It's a Draw!")

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

#Write your code below this line 👇
options_list = [rock, paper, scissors]
user_chose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))


if user_chose > 2 or user_chose < 0:
  print("You typed an invalid number, you loose!")
else:
  print(options_list[user_chose])
  
  computer_chose = random.randint(0, len(options_list) - 1)
  print("Computer chose:\n" + options_list[computer_chose])
  if user_chose == computer_chose:
    print("It's a draw, nobody wins")
  elif (user_chose == 0 and computer_chose == 2) or (user_chose == 1 and computer_chose == 0) or (user_chose == 2 and computer_chose == 1):
    print("You win!")
  else:
    print("You loose!")

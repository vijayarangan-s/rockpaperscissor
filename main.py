import random

rock = '''   
 _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''

user_choice = int(input('Enter your choice 0 for rock , 1 for paper, 2 for scissor ?'))

hand = [rock, paper, scissor]

computer_choice = random.randint(0,2)

print(len(hand) > user_choice)

if len(hand) > user_choice: 
  print('-------------User Choice------------\n')
  print(f'{hand[user_choice]}\n')
  print('---------Computer Choice------------\n')
  print(f'{hand[computer_choice]}\n')
else : 
  print('Please Enter the valid input')

if len(hand) > user_choice:
  if computer_choice > user_choice:
    print('Computer wins!....')
  elif user_choice > computer_choice:
    print('User wins....!')
  elif user_choice == 0 and computer_choice == 2:
    print('You Win....!')
  elif computer_choice == 0 and user_choice == 2:
    print('You lose....!')
  elif user_choice == computer_choice:
    print('you Draw....Keep Try....!')
  else:
    print('you Lose.....!')
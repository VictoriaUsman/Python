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

hands_list = [rock, paper, scissors]
hands = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
if hands == '0':
    print("You chose Rock")
    print(rock)
    computer = random.choice(hands_list)
    if computer == hands_list[0]:
        print("Computer chose Rock")
        print(rock)
        print("It's a tie!")
    if computer == hands_list[1]:
        print("Computer chose Paper")
        print(paper)
        print("You Lose!")
    if computer == hands_list[2]:
        print("Computer chose Scissors")
        print(scissors)
        print("You Win!")

elif hands == '1':
    print("You chose Paper")
    print(paper)
    computer = random.choice(hands_list)
    if computer == hands_list[0]:
        print("Computer chose Rock")
        print(rock)
        print("You Win!")
    if computer == hands_list[1]:
        print("Computer chose Paper")
        print(paper)
        print("It's a tie!")
    if computer == hands_list[2]:
        print("Computer chose Scissors")
        print(scissors)
        print("You Lose!")

elif hands == '2':
    print("You chose Scissors")
    print(scissors)
    computer = random.choice(hands_list)
    if computer == hands_list[0]:
        print("Computer chose Rock")
        print(rock)
        print("You Lose!")
    if computer == hands_list[1]:
        print("Computer chose Paper")
        print(paper)
        print("You Win!")
    if computer == hands_list[2]:
        print("Computer chose Scissors")
        print(scissors)
        print("It's a tie!")

else:
    print("Invalid input")



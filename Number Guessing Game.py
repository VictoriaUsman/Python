logo = r"""
 _______               ___.                    ________                            .__                 
 \      \  __ __  _____\_ |__   ___________   /  _____/ __ __   ____   ______ _____|__| ____    ____   
 /   |   \|  |  \/     \| __ \_/ __ \_  __ \ /   \  ___|  |  \_/ __ \ /  ___//  ___/  |/    \  / ___\  
/    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/ \    \_\  \  |  /\  ___/ \___ \ \___ \|  |   |  \/ /_/  > 
\____|__  /____/|__|_|  /___  /\___  >__|     \______  /____/  \___  >____  >____  >__|___|  /\___  /  
        \/            \/    \/     \/                \/            \/     \/     \/        \//_____/   
                             ________    _____      _____  ___________                                 
                            /  _____/   /  _  \    /     \ \_   _____/                                 
                           /   \  ___  /  /_\  \  /  \ /  \ |    __)_                                  
                           \    \_\  \/    |    \/    Y    \|        \                                 
                            \______  /\____|__  /\____|__  /_______  /                                 
                                   \/         \/         \/        \/                                  
"""
import random

print(logo)
print("Welcome to Number Guessing Project!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty: Type 'easy' or 'hard'\n")


attempts = 0
if difficulty == "easy":
    attempts += 10
    print(f"You have {attempts} attempts left")

if difficulty == "hard":
    attempts += 5
    print(f"You have {attempts} attempts left")

random_number = random.randint(1, 101)
print(f"Your number is {random_number}")

Continue = True
while Continue:
    guess = int(input("Make a guess: "))
    if guess == random_number:
        print("You got it!")
        Continue = False
    if guess != random_number:
        attempts -= 1
        print(f"You have {attempts} attempts left")
        if attempts < 1:
            print("You lose :(")
            Continue = False
        if  attempts > 1:
            Continue = True
            if guess > random_number:
                print("Lower!")
                Continue = True
            if guess < random_number:
                print("Higher")
                Continue = True






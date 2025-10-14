import random
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
print("Welcome to Poging Hangman Game")
word_list = ["aardvark", "baboon", "camel"]
blank = "_"
word = ""
Word_In_List = []
Word_To_Guess = random.choice(word_list)
for X in range(len(Word_To_Guess)):
    word += blank
for letter in range(len(Word_To_Guess)):
    Word_In_List += [Word_To_Guess[letter]]

print(Word_To_Guess)
print(word)
HangOver = False
New_Word_In_List = []
lives = 6
while HangOver == False:
    guess = input("Guess the word:\n")
    Display_Word = ""
    for letter in Word_To_Guess:
        if guess == letter:
            Display_Word += letter
            New_Word_In_List.append(guess)
        elif letter in New_Word_In_List:
            Display_Word += letter
        else:
            Display_Word += blank

    print(Display_Word)

    if guess not in Word_To_Guess:
        lives -= 1
    print(stages[lives])

    if "_" not in Display_Word:
        HangOver = True
        print("You guessed the word!")
    if lives < 1:
        HangOver = True
        print("Game Over!")
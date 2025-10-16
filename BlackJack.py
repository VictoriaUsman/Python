logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
import random
print(logo)

Cards = {
    "A": int,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,

}

# 1st Pick for Your Card
y_card1 = random.choice(list(Cards.keys()))
y_card2 = random.choice(list(Cards.keys()))



if y_card1 in Cards:
    number_1 = Cards[y_card1]
    if y_card1 == "A":
        print("Your Card #2 is: [" + y_card2 + "]")
        y1_choice = int(input("You got ACE card 1! Would it be 1 or 11\n"))
        if y1_choice == 1:
            number_1 = 1
        if y1_choice == 11:
            number_1 = 11

if y_card2 in Cards:
    number_2 = Cards[y_card2]
    if y_card2 == "A":
        print("Your Card #1 is: "+ y_card1)
        y2_choice = int(input("You got ACE for card 2! Would it be 1 or 11\n"))
        if y2_choice == 1:
            number_2 = 1
        if y2_choice == 11:
            number_2 = 11

count = number_1 + number_2

print("Your Card is: [" + str(y_card1) + " and " + str(y_card2) + "]")
print(count)



comp_card1 = random.choice(list(Cards.keys()))
comp_card2 = random.choice(list(Cards.keys()))



if comp_card1 in Cards:
    number_3 = Cards[comp_card1]
    if comp_card1 == "A":
        print("Computer Card #2 is: [" + comp_card2 + "]")
        C1_choice = int(input("Computer got ACE for card 1! Would it be 1 or 11\n"))
        if C1_choice == 1:
            number_3 = 1
        if C1_choice == 11:
            number_3 = 11

if comp_card2 in Cards:
    number_4 = Cards[comp_card2]
    if comp_card2 == "A":
        print("Computer Card #1 is: "+ comp_card1)
        y2_choice = int(input("Computer got ACE for card 2! Would it be 1 or 11\n"))
        if y2_choice == 1:
            number_4 = 1
        if y2_choice == 11:
            number_4 = 11


count2 = number_3 + number_4

print("Commputer Card is: [" + str(comp_card1) + " and " + str(comp_card2) + "]")
print(count2)
print(" ")

more_card = input("Would you like to get 1 more card? y/n\n")
if more_card == "n":
    test1 = 21 - count
    test2 = 21 - count2
    if test1 > test2:
        print("You Lose!")
    if test1 < test2:
        print("You Win!")
    else:
        print("It's a tie!")

if more_card == "y":
    y_card3 = random.choice(list(Cards.keys()))
    number_5 = Cards[y_card3]
    if y_card3 in Cards:
        if y_card3 == "A":
            print("Your New Card is: [" + str(y_card3) + "]")
            y3_choice = int(input("You got ACE card 3! Would it be 1 or 11\n"))
            if y3_choice == 1:
                number_5 = 1
                print("Your Cards Counts are: [" + str(number_1) + " ," + str(number_2) + ", and " + str(number_5) + "]")
                count1 = number_1 + number_2 + number_5
                print(count1)
                if count1 > 21:
                    print("You Lose!")
                else:
                    test1 = 21 - count
                    test2 = 21 - count2
                    if test1 > test2:
                        print("You Lose!")
                    if test1 < test2:
                        print("You Win!")
                    else:
                        print("It's a tie!")

        if y3_choice == 11:
                print("Your Cards Counts are: ["+ str(number_1) + " ," + str(number_2) + ", and " + str(number_5) +"]")
                count1 = number_1 + number_2 + number_5
                print(count1)
                if count1 > 21:
                    print("You Lose! You got more than 21")
                else:
                    test1 = 21 - count1
                    test2 = 21 - count2
                    if test1 > test2:
                        print("You Lose!")
                    if test1 < test2:
                        print("You Win!")
                    else:
                        print("It's a tie!")




        else:
            print("Your Cards Counts are: ["+ str(number_1) + " ," + str(number_2) + ", and " + str(number_5) + "]")
            count1 = number_1 + number_2 + number_5
            print(count1)
            if count1 > 21:
                print("You Lose! You got more than 21")
            else:
                test1 = 21 - count1
                test2 = 21 - count2
                if test1 > test2:
                    print("You Lose!")
                if test1 < test2:
                    print("You Win!")
                else:
                    print("It's a tie!")



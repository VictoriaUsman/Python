print("This is love calculator")

Name_of_Male = (input("What is the male's name?"))
Name_of_Female = (input("What is the female's name?"))

NAME = []
Comb_List = Name_of_Male + Name_of_Female
for letter in Comb_List:
    NAME.append(letter.upper())
print("T = " + str(NAME.count("T")))
print("R = " + str(NAME.count("R")))
print("U = " + str(NAME.count("U")))
print("E = " + str(NAME.count("E")))

print("L = " + str(NAME.count("L")))
print("O = " + str(NAME.count("O")))
print("V = " + str(NAME.count("V")))
print("E = " + str(NAME.count("E")))

true_counter = NAME.count("T") + NAME.count("R") + NAME.count("U") + NAME.count("E")
love_counter = NAME.count("L") + NAME.count("O") + NAME.count("V") + NAME.count("E")
love_score = true_counter + love_counter
print("Love Score = " + str(true_counter) + str(love_score))

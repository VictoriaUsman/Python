print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

Tip_for_each_Person = (bill/people) * tip/100
print(f"Each person should pay: ${Tip_for_each_Person}")
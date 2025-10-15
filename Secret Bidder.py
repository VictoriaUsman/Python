logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
print("Welcome to the Secret Highest Auction Application!")
high_bid = {}
morebid = True

while morebid:
    name = input("What is your name?\n")
    bid = int(input("What is your bid?\n"))
    high_bid[name] = bid

    more = input("Is there another person who would like to bid - yes or no?")
    if more == "yes":
        morebid = True
    if more == "no":
        morebid = False
    print("\n" *100)

highest_bid = 0
highest_bidder = name
for name in high_bid:
    if high_bid[name] > highest_bid:
        highest_bid = high_bid[name]
        highest_bidder = name
print("The Highest Bidder Is: " + highest_bidder)
print("Bid: " + str(highest_bid))
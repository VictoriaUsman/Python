logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)
print("           Welcome to Python Calculator\n               by Ian Tristan ")

n1 = float(input("Please enter a number: \n"))
n2 = input("Enter the operation: \n")
n3 = float(input("Enter the number: \n"))

def add(n1, n3):
    return n1 + n3
def sub(n1, n3):
    return n1 - n3
def multiply(n1, n3):
    return n1 * n3
def divide(n1, n3):
    return n1 / n3

Operation = {
    "+": add,
    "-": sub,
    "*": multiply,
    "/": divide
}

result = 0

if n2 in Operation:
    answer = Operation[n2](n1, n3)
    result = answer
    print(f"Answer = {result}")

Addmore = True
while Addmore:
    again = input(f"Do you want to perform another operation for - {result}? (y/n)")
    if again == "y":
        n2 = input("Enter the operation: \n")
        n3 = float(input("Enter the number: \n"))
        if n2 in Operation:
            answer = Operation[n2](result, n3)
            result = answer
            print(f"Answer = {answer}")
        Addmore = True
    else:
        Addmore = False

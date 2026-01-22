import random
def guess():
    return random.randint(15 , 30)
userName = input("What is your name?")
correct = False
while not correct:
    currentGuess = guess()
    response = input(f"are you {currentGuess} years old? (y/n)" )
    if response == "y":
        correct = True
    else:
        print("Rats")
print(userName + " is " + str(currentGuess) + " years old")

import random
def guess(x = 15, y = 30):
    return random.randint(x, y)
userName = input("What is your name?")
correct = False
currentGuess = guess()
while not correct:
    response = input(f"are you {currentGuess} years old? (older/younger/correct)" )
    if response == "older":
        currentGuess = guess(currentGuess, 30)
    elif response == "younger":
        currentGuess = guess(15, currentGuess)
    elif response == "correct":
        correct = True
print(userName + " is " + str(currentGuess) + " years old")

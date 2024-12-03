import random as r

# input
def userInput():
    getInput = input("Enter name:")

    # true loop for number of adjectives user wants
    while True:
        try:
            numAdjectives = int(input("Enter the number of adjectives to include: "))
            if 1 <= numAdjectives <= 3:
                break
            else:
                print("Please enter a number between 1 and 3.")
        except ValueError:
            print("Please enter a number between 1 and 3.")

    # true loop for number of insults to generate
    while True: 
        try: 
            numInsults = int(input("Enter the number of insults you would like to generate: ")) 
            if numInsults > 0: 
                break 
            else: print("Please enter a positive number.")
        except ValueError: print("Please enter a positive number.")

    return getInput, numAdjectives, numInsults

# pass number of adjectives into insult function
def insult(numAdjectives):
    # list
    adjective = ["abhorrent", "babbling", "disapointing", "annoying", "facetious", "loathsome", "myopic", "querulous", "petulant", "vacuous"]
    noun = ["idiot", "dummy", "slob", "loser", "wimp", "weakling"]


    # pulls random sample from list with user specified number of adjectives
    selectedAdjective = r.sample(adjective, numAdjectives)
    # choses random noun
    selectedNoun = r.choice(noun)

    return selectedAdjective, selectedNoun

def generateInsult():
    # take users input
    Name, numAdjectives, numInsults = userInput()

    # loop runs based of user inputted number of insults
    for x in range(numInsults):
        # call the genertaed insults with the user inputted number
        selectedAdjective, selectedNoun = insult(numAdjectives)

        # start empty string loop
        allInsults = ""
        for n in range(len(selectedAdjective)):
            allInsults += (f"{selectedAdjective[n]} ")
        allInsults += selectedNoun

        # print result
        print(f"{Name} is a {allInsults}!")
        
def main():
    # play again loop
    # set a value for loop
    again = "y"
    # loop will run as long as input is "y"
    while again.lower() == "y":
        generateInsult()
        # inner loop gets the "y" or "n" input
        while True:
            again = input("Do you want to generate another insult? (y/n): ").lower()
            # if "n" program breaks and ends
            if again in ("y", "n"):
                break
            # if not y or n error check
            else: 
                print("Please enter 'y' to play again or 'n' to quit.")
main()
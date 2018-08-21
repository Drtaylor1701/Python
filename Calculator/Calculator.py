print("What type of math are you doing?")
print("Press 1 for arithmetic. Examples include addition, subtraction, multiplication, and division problems.")

mathType = input()

def selectMath(mathType):
    numbersToWorkWith = []
    if mathType == 1:
        print("You have selected arithmetic.")
        mathType == "arithmetic"
        print("Excellent. Give me the numbers you are working with, please.")
        keepGettingNumbers = True
        while keepGettingNumbers == True:
            number = input()
            numbersToWorkWith.append(number)
            print("Is that the last number I need to know about? y/n")
            response = input()
            if response == y or response == Y:
                keepGettingNumbers = False
            elif response == n or response == N:
                keepGettingNumbers = True
            else:
                print("That didn't make any sense, so I'm not sure what to do here.")
                print("Please try again. More numbers? y/n")
                if response == y or response == Y:
                    keepGettingNumbers = False
                elif response == n or response == N:
                    keepGettingNumbers = True
        else:
            print("I'm sorry, I don't know what you want me to do with that.")

selectMath(mathType)

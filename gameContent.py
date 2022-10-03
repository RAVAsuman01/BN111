import random


# the main game class:
class MasterMind:

    # constants for the class
    MAXIMUM_NUMBER_GUESSES = 10
    NUMBER_OF_DIGITS = 3

    # constructor
    def __init__(self):
        self.disp()
        self.totalGameGuesses = 0
        self.totalGamesPlayed = 0
        self.newGame()

    # function to display the welcome message
    def disp(self):
        print("\n\t ~~~ Welcome to Mastermind Game ~~~")
        print("Hi gamer, welcome to the Mastermind game")
        name = input("What is your name ? ")
        print("Hello, " + name +
              ", Please follow the instructions to play the game.\n")
        print("\t ~~~ GAME INSTRUCTION ~~~ \n ")
        print(" I am thinking of a 3-digit number. Try to guess what it is.\n")
        print("Here are some clues:")
        print("When I say:   That means:\n")
        print("Yellow        One digit is correct but in the wrong position.")
        print("Green         One digit is correct and in the right position.")
        print("Red           No digit is correct.\n")
        print(
            "For example, if the secret number was 346 and your guess was 843, the clues would be Green Yellow.\n"
        )

    # function to generate random numbers
    def guessCode(self):
        # Generate three unique random numbers in [0,9]
        randNums = random.sample(range(0, 10), MasterMind.NUMBER_OF_DIGITS)
        # Shuffle the random numbers into random order
        random.shuffle(randNums)
        # Join them to make a string and return it
        randNumstr = ''.join(str(x) for x in randNums)
        return randNumstr

    # function that holds the game logic and returns appropriate result
    def guessFlagColor(self, userInNum):
        # check user input
        if (len(userInNum) != 3):
            return "Invalid Input"

        # check if correct input is given
        if (userInNum == self.gameCode):
            self.gameEnd = True
            self.numberOfGuessesMade += 1
            self.totalGameGuesses += 1
            return "You got it!"

        # if there are moves left
        if (self.hasMoreMoves() and (not self.gameEnd)):
            self.numberOfGuessesMade += 1
            self.totalGameGuesses += 1
            allWrongPos = True
            corDigWrongPlac = 0
            corDigCorPlac = 0

            # loop through both string numbers to determine required output
            for i in range(self.NUMBER_OF_DIGITS):
                for j in range(self.NUMBER_OF_DIGITS):
                    # if the digits match
                    if userInNum[i] == self.gameCode[j]:
                        allWrongPos = False
                        # if the positions match as well
                        if i == j:
                            corDigCorPlac += 1
                        else:
                            corDigWrongPlac += 1

            # if no digit match
            if allWrongPos:
                return "Red"
            else:
                # build relevant return string
                returnString = ""
                for i in range(corDigCorPlac):
                    returnString += "Green "
                for i in range(corDigWrongPlac):
                    returnString += "Yellow "
            return returnString
        else:
            return "No More Moves"

    # function that checks if the user has more moves
    def hasMoreMoves(self):
        return self.numberOfGuessesMade < self.MAXIMUM_NUMBER_GUESSES

    # function to start a new game
    def newGame(self):
        self.gameCode = self.guessCode()
        self.totalGamesPlayed += 1
        self.numberOfGuessesMade = 0
        self.gameEnd = False
        print("I have thought up a number.")
        print(" You have " + str(self.MAXIMUM_NUMBER_GUESSES) +
              " guesses to get it.")

    # function that displays the results of the game
    def dispResult(self):
        print("Thank you for playing")
        print("Overall results: Total games = " + str(self.totalGamesPlayed))
        print("Total guesses = " + str(self.totalGameGuesses))
        print("Average guesses/game = " +
              str(self.totalGameGuesses / self.totalGamesPlayed))

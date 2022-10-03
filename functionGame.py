from gameContent import MasterMind


# main program
def main():
    # creating the object of the game
    myGame = MasterMind()

    play = True
    # loop until the user wants to exit
    while play == True:
        userInput = ""
        # loop until there are valid moves and game not end
        while (myGame.hasMoreMoves() and (not myGame.gameEnd)):
            print("Guess #" + str(myGame.numberOfGuessesMade + 1) + ":")
            userInput = input("> ")
            print(myGame.guessFlagColor(userInput))

        # asking if the user wants to start a new game
        answer = input("Do you want to play again? (Yes/No) ")
        if (len(answer) != 0) and (answer.lower()[0] == 'y'):
            play = True
            myGame.newGame()
        else:
            play = False
            myGame.dispResult()


# running the game
main()

# -----------------------------------------------------------
# Game of TicTacToe
#
# (C) 2020 Pieke Heijmans
# -----------------------------------------------------------

# Function to display the TicTacToeBoard
def displayBoard(list):
    # Copy board list, to not directly change the boardlist values.
    copyBoard = []
    for i in list:
        if (i == 0):
            copyBoard.append(' ')
        if (i == 1):
            copyBoard.append('x')
        if (i == 2):
            copyBoard.append('o')
    print(copyBoard[0] + '|' + copyBoard[1] + '|' + copyBoard[2])
    print('-+-+-')
    print(copyBoard[3] + '|' + copyBoard[4] + '|'+ copyBoard[5])
    print('-+-+-')
    print(copyBoard[6] + '|' + copyBoard[7] + '|' + copyBoard[8])
    

# Player 1's turn.
def makeAMove1():
    print("Het is de beurt aan Speler 1! Waar wil je een kruisje zetten?")
    while True:
      try:
        turn = int(input("Speler 1 voert een getal in van 1 tot 9: "))
        if (turn > 0 and turn < 10) and newBoard[turn-1] == 0: 
            # If statement to check whether the values are between 0-9 and whether the given value is occupied or not.
            break
        print("Voer een geldige zet in op een vrije plek van 1 tot 9!") # The number is not valid or place is occupied.
      except Exception as e:
        print('Weet je niet wat een getal is?') #User typed in string or float value.
    for i in range(len(newBoard)):
        newBoard[turn-1] = 1 # Success, the given value is changed in '1', the x.
               
#S Spaler 2's turn
def makeAMove2():
    print("Het is de beurt aan Speler 2! Waar wil je een rondje zetten?")
    while True:
      try:
        turn = int(input("Speler 2 voert een getal in van 1 tot 9: "))
        if (turn > 0 and turn < 10) and newBoard[turn-1] == 0:
             # If statement to check whether the values are between 0-9 and whether the given value is occupied or not.
            break
        print("Voer een geldige zet in op een vrije plek van 1 tot 9!")
      except Exception as e:
        print('Weet je niet wat een getal is?')
    for i in range(len(newBoard)):
        newBoard[turn-1] = 2 # Success, the given value is changed in '2', the o.
        
def boardEvaluate():
    if (newBoard[0] == newBoard[1] == newBoard[2] == 1 # First horizontal row = 'x'
        or newBoard[3] == newBoard[4] == newBoard[5] == 1 # Second horizontal row = 'x'
        or newBoard[6] == newBoard[7] == newBoard[8] == 1
        or newBoard[0] == newBoard[3] == newBoard[6] == 1 # First vertical row = 'x'
        or newBoard[1] == newBoard[4] == newBoard[7] == 1 #etc etc.
        or newBoard[2] == newBoard[5] == newBoard[8] == 1
        or newBoard[0] == newBoard[4] == newBoard[8] == 1
        or newBoard[6] == newBoard[4] == newBoard[2] == 1):
        return 0 # Return 0 in case that Player 1 has 3 in a row and wins the game.
    if (newBoard[0] == newBoard[1] == newBoard[2] == 2 # First horizontal row = 'o'
        or newBoard[3] == newBoard[4] == newBoard[5] == 2
        or newBoard[6] == newBoard[7] == newBoard[8] == 2
        or newBoard[0] == newBoard[3] == newBoard[6] == 2
        or newBoard[1] == newBoard[4] == newBoard[7] == 2
        or newBoard[2] == newBoard[5] == newBoard[8] == 2
        or newBoard[0] == newBoard[4] == newBoard[8] == 2
        or newBoard[6] == newBoard[4] == newBoard[2] == 2):
        return 1 # Return 1 in case that Player 2 has 3 in a row and wins the game.
    if (newBoard[0] != 0
        and newBoard[1] != 0
        and newBoard[2] != 0     
        and newBoard[3] != 0
        and newBoard[4] != 0
        and newBoard[5] != 0
        and newBoard[6] != 0
        and newBoard[7] != 0  
        and newBoard[8] != 0):
        return 2 # Return 2: it's a tie and all spaces on the board are occupied.
    else: 
        return 3 # There is no winner yet and spots are available: keep playing.


def startGame():
    gameOn = True
    while (gameOn): # Keep making moves untill the game has finished.
        displayBoard(newBoard)
        makeAMove1()
        print("\n") # To add more spacing between rounds, visually more appealing.
        if (boardEvaluate() == 0):
            print('Speler 1 wint het spel!')
            gameOn = False # End game, Player 1 wins.
            break
        if (boardEvaluate() == 1):
            print('Speler 2 wint het spel!')
            gameOn == False # End game, Player 2 wins.
            break
        if (boardEvaluate() == 2):
            print('Oh oh! Gelijkspel.') #It's a Tie
            gameOn == False
            break
        if (boardEvaluate() == 3):
            print('Er kunnen nog zetten gedaan worden.') # Keep playing.
        displayBoard(newBoard)
        makeAMove2()
        print("\n")
        if (boardEvaluate() == 0):
            print('Speler 1 wint het spel!')
            gameOn = False
            break
        if (boardEvaluate() == 1):
            print('Speler 2 wint het spel!')
            gameOn == False
            break
        if (boardEvaluate() == 2):
            print('Oh oh! Gelijkspel.')
            gameOn == False
            break
        if (boardEvaluate() == 3):
            print('Er kunnen nog zetten gedaan worden.')
    displayBoard(newBoard)
    gameOn = False


while True:
    newBoard = [0, 0, 0, 0, 0, 0, 0, 0, 0] # Start a new, empty board.            
    startGame()# Starts game.
    restart = input('Wil je nog een keer spelen? y/n') # Restart the game.
    print("\n")
    if restart == 'n':
        print('Boo!')
        print("\n")
        print('Spel verlaten.')
        break
    elif restart == 'y':
        continue
    else:
        print('Spel verlaten.')
        break

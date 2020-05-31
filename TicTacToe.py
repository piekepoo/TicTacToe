# -----------------------------------------------------------
# Game of TicTacToe
#
# (C) 2020 Pieke Heijmans
# -----------------------------------------------------------
"""Hi Karim,
I have created a game of TicTacToe and it's working fine, except for the part of PlayAgain at the bottom of the code. 
Basically what I want is that the user has the option to start over if they type 'y'.
Problem is that within the loop I cannot call the variable newBoard as it is defined outside of the loop and I can't find a way to reset the global variable within the loop.
I have to change things around  but I'm not sure how. Thanks for looking at it <3"""

#Functie om het board als TicTacToe te weergeven
def displayBoard(list):
    #Maak een kopie om bij de weergave de waarden van het booard niet direct aan te spreken
    copyBoard = []
    for i in list:
        if (i == 0):
            copyBoard.append(' ')
        if (i == 1):
            copyBoard.append('x')
        if (i == 2):
            copyBoard.append('o')
    print(copyBoard[0], '|', copyBoard[1], '|', copyBoard[2])
    print('---------')
    print(copyBoard[3], '|', copyBoard[4], '|', copyBoard[5])
    print('---------')
    print(copyBoard[6], '|', copyBoard[7], '|', copyBoard[8])
    

#Speler 1 is aan zet
def makeAMove1():
    print("Het is de beurt aan Speler 1! Waar wil je een kruisje zetten?")
    while True:
      try:
        zet = int(input("Speler 1 voert een getal in van 1 tot 9: "))
        if (zet > 0 and zet < 10) and newBoard[zet-1] == 0: 
            #Controleert of waarde tussen 0-9 is en of de ingegeven plaats vrij is
            break
        print("Voer een geldige zet in op een vrije plek van 1 tot 9!") #Het getal is niet tussen 1-9 of niet vrij
      except Exception as e:
        print('Weet je niet wat een getal is?') #String ingegeven of float
    for i in range(len(newBoard)):
        newBoard[zet-1] = 1 #Succes dus vakje wordt veranderd in een '1'
               
#Speler 2 is aan zet
def makeAMove2():
    print("Het is de beurt aan Speler 2! Waar wil je een rondje zetten?")
    while True:
      try:
        zet = int(input("Speler 2 voert een getal in van 1 tot 9: "))
        if (zet > 0 and zet < 10) and newBoard[zet-1] == 0:
            #Controleert of waarde tussen 0-9 is en of de ingegeven plaats vrij is
            break
        print("Voer een geldige zet in op een vrije plek van 1 tot 9!")
      except Exception as e:
        print('Weet je niet wat een getal is?')
    for i in range(len(newBoard)):
        newBoard[zet-1] = 2 #Succes dus vakje wordt verandert in een '2'
        
def boardEvaluate():
    if (newBoard[0] == newBoard[1] == newBoard[2] == 1 # eerste rij horizontaal = 'x'
        or newBoard[3] == newBoard[4] == newBoard[5] == 1 # tweede rij horizontaal = 'x'
        or newBoard[6] == newBoard[7] == newBoard[8] == 1
        or newBoard[0] == newBoard[3] == newBoard[6] == 1 #eerste rij verticaal = 'x'
        or newBoard[1] == newBoard[4] == newBoard[7] == 1 #etc etc.
        or newBoard[2] == newBoard[5] == newBoard[8] == 1
        or newBoard[0] == newBoard[4] == newBoard[8] == 1
        or newBoard[6] == newBoard[4] == newBoard[2] == 1):
        return 0 #Return 0 in geval dat speler 1 3 op rij heeft en dus wint.
    if (newBoard[0] == newBoard[1] == newBoard[2] == 2
        or newBoard[3] == newBoard[4] == newBoard[5] == 2
        or newBoard[6] == newBoard[7] == newBoard[8] == 2
        or newBoard[0] == newBoard[3] == newBoard[6] == 2
        or newBoard[1] == newBoard[4] == newBoard[7] == 2
        or newBoard[2] == newBoard[5] == newBoard[8] == 2
        or newBoard[0] == newBoard[4] == newBoard[8] == 2
        or newBoard[6] == newBoard[4] == newBoard[2] == 2):
        return 1 #Return 1 in geval dat speler 2 3 op rij heef en dus wint.
    if (newBoard[0] != 0
        and newBoard[1] != 0
        and newBoard[2] != 0     
        and newBoard[3] != 0
        and newBoard[4] != 0
        and newBoard[5] != 0
        and newBoard[6] != 0
        and newBoard[7] != 0  
        and newBoard[8] != 0):
        return 2 #Return 2 als alle zetten niet 0 zijn, en dus allemaal ingevuld zijn maar geen winnaar er uit komt: gelijkspel.
    else: 
        return 3 #Nog geen winnaar en nog steeds vakjes vrij: speel door.


def startGame():
    gameOn = True
    while (gameOn): #Blijf dit doen tot spel afgelopen.
        displayBoard(newBoard)
        makeAMove1()
        print("\n") #Netter format met meer spacing tussen rondes.
        if (boardEvaluate() == 0):
            print('Speler 1 wint het spel!')
            gameOn = False #Einde spel als Speler 1 wint.
            break
        if (boardEvaluate() == 1):
            print('Speler 2 wint het spel!')
            gameOn == False #Einde spel als Speler 2 wint.
            break
        if (boardEvaluate() == 2):
            print('Oh oh! Gelijkspel.')
            gameOn == False
            break
        if (boardEvaluate() == 3):
            print('Er kunnen nog zetten gedaan worden.') #Geen break, want spel speelt door.
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
    playAgain = int(input("Nog een keer spelen? y/n"))
    if (playAgain == 'y'):
        #newBoard = [0, 0, 0, 0, 0, 0, 0, 0, 0]
       # startGame()
        gameOn = True
    else:
        print('Boo!')

newBoard = [0, 0, 0, 0, 0, 0, 0, 0, 0] #Begint nieuw bord met lege vakjes.            
startGame()#Begin spel.



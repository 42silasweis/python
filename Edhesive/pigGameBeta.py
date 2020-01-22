import random
import time

guess = 0
c = 0
correct = random.randint(1, 100)

pScore = 0
pRoll = " "
pRollScore = 0
pRollCount = 0
pRollNumber = 0

cScore = 0
cRoll = " "
cRollScore = 0
cRollCount = 0
cRollNumber = 0
cChanceToRoll = 0

isPlayerTurn = 1
isComputerTurn = 0
print("\nWelcome to Silas's PigGame! to win you must reach 100 before the computer. \nYou can roll as many times as you want with every roll number being added to a total turn score \nthat will go into your Game Total score when you end your turn (stop rolling by saying no). \nIf you land a 1 on any roll your turn instantly ends and you lose all your turn points. \nHope you enjoy the game!")
def PlayerTurn():
    global isPlayerTurn
    global isComputerTurn
    global pRollScore
    global pScore
    global pRollCount
    global pRollNumber
    global pRoll

    while (isPlayerTurn == 1):

        if(pRollCount >= 1):
            pRoll = str(input("\nRoll Again? (y=Yes n=No): "))
            time.sleep(1)
        else:
            pRoll = str(input("\nPlayer turn. roll? (y=Yes n=No): "))
            time.sleep(1)

        if(pRoll != "y" and pRoll != "Y" and pRoll != "n" and pRoll != "N"):
            while(pRoll != "y" and pRoll != "Y" and pRoll != "n" and pRoll != "N"):
                #print("Debug. If WhileLoop 1 " + str(pRoll))
				#print(type(pRoll))
                pRoll = str(input("\nInvalid input. roll? (y=Yes n=No): "))
				
        if(pRollCount < 1 and pRoll == "n" or pRollCount < 1 and pRoll == "N"):
            while(pRoll == "n" or pRoll == "N"):
                pRoll = str(input("\nMust roll at least once. roll? (y=Yes n=No): "))

        elif(pRoll == "n" or pRoll == "N"):
            isPlayerTurn = 0
            isComputerTurn = 1
            pScore += pRollScore
            print("\nYou ended your turn with " + str(pRollScore) + ". and a total score of " + str(pScore))
            pRollCount = 0
            pRollScore = 0
            time.sleep(1)
            if(pScore >= 100):
                print("\nCongratulations you reached 100 or more points before the computer, you win! Total Score: " + str(pScore))
                time.sleep(10)
                exit()

            MainLoop()


        if (pRoll == "y" or pRoll == "Y"):
            pRollNumber = random.randint(1, 6)
            pRollCount += 1

        time.sleep(1)

        if(pRollNumber == 1):
            print("\nYou landed a " + str(pRollNumber) + " your turn is now over.")
            isPlayerTurn = 0
            isComputerTurn = 1
            pRollCount = 0
            pRollScore = 0
            print("\nTotal Score: " + str(pScore))
            time.sleep(1)
            MainLoop()

        if(pRollNumber > 1):
            pRollScore += pRollNumber
            print("\nYou rolled " + str(pRollNumber) + ". With a total turn score of " + str(pRollScore))
            time.sleep(1)




def ComputerTurn():
    global isPlayerTurn
    global isComputerTurn
    global cRollScore
    global cScore
    global cRollCount
    global cRollNumber
    global cChanceToRoll

    while (isComputerTurn == 1):

        if(cRollCount >= 1 and cRollCount <= 2):
            cChanceToRoll = random.randint(1, 3)

        if(cRollCount >= 4):
            cChanceToRoll = random.randint(1, 4)

        if(cRollCount < 1):
            cChanceToRoll = 1

        if (cChanceToRoll == 1 or cChanceToRoll == 3):
            cRollNumber = random.randint(1, 6)
            cRollCount += 1

        elif(cChanceToRoll != 1 or cChanceToRoll != 3):
            isComputerTurn = 0
            isPlayerTurn = 1
            cScore += cRollScore
            print("\nComputer ended their turn with " + str(cRollScore) + ". and a total score of " + str(cScore))
            cRollCount = 0
            cRollScore = 0
            time.sleep(2)
            if(cScore >= 100):
                print("\nSorry, the computer obtained 100 or more points before you, you lost. Computers points: " + str(cScore) + ". Your score: " + str(pScore))
                time.sleep(10)
                exit()
            MainLoop()


        if(cRollNumber == 1):
            print("\nComputer landed a " + str(cRollNumber) + " computer turn is now over. \n\nComputer Total Score: " + str(cScore))
            isComputerTurn = 0
            isPlayerTurn = 1
            cRollCount = 0
            cRollScore = 0
            time.sleep(2)
            MainLoop()

        if(cRollCount >= 2 and cRollNumber > 1):
            cRollScore += cRollNumber
            print("\nComputer rolled again and rolled a " + str(cRollNumber) +". With a total turn score of " + str(cRollScore))
            time.sleep(2)
        else:
            cRollScore += cRollNumber
            print("\nComputer rolled a " + str(cRollNumber) + ". With a total turn score of " + str(cRollScore))
            time.sleep(2)



def MainLoop():
    global pScore
    global cScore
    global isPlayerTurn
    global isComputerTurn

    while (pScore <= 100 or cScore <= 100):
        if(isPlayerTurn == 1):
            PlayerTurn()
        else:
            ComputerTurn()

MainLoop()

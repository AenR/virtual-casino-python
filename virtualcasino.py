#<----------imports---------->
import random # Choosing random number
import time # For sleep command
import os # For clear console
from openpyxl import Workbook,load_workbook # For save balance
#<----------/imports---------->

#<----------variables---------->
def clear(): # Clear console screen
    os.system('cls' if os.name=='nt' else 'clear')

def moneyDecrase():
    casinoBalance.value -= betAmount
    ws["A1"]=casinoBalance.value
    wb.save("casinobalance.xlsx")

def moneySave():
    ws["A1"]=casinoBalance.value
    wb.save("casinobalance.xlsx")

wb = load_workbook("casinobalance.xlsx")
ws = wb.active
casinoBalance= ws["A1"] # Balance = A1 cell in excel
wb.close()
#<----------/variables---------->

#<----------Main Menu---------->
while True:
    mainMenuChoose = int(input("Welcome!\nYour Wallet: {:.0f}\n1-) Heads or Tails\n2-) Aviator\n3-) Guess\n4-) Same Dice\n0-) Exit\n".format(casinoBalance.value)))

    if(mainMenuChoose == 0 or mainMenuChoose > 4): # Exit
        print("Bye!")
        break
#<----------/Main Menu---------->

#<----------Heads or Tails---------->
    elif(mainMenuChoose == 1):
        sonuc = random.randint(1,2)
        print("Welcome to Heads or Tails Game your wallet: {:.0f}".format(casinoBalance.value))
        while True: # Play until exit
            betAmount = int(input("Please enter your bet: \n0-) Exit\n"))
            if(betAmount>casinoBalance.value):
                print("Invalid value.")
                break
            if(betAmount==0): # Exit
                print("Bye!")
                break
            moneyDecrase()

            playerChoose = input("Heads or Tails?\n")
            if(playerChoose=="heads"):
                hort = 1
            if(playerChoose=="tails"):
                hort = 2
            if(sonuc==hort):
                betAmount *= 2
                casinoBalance.value += betAmount
                print("You won. Your new balance: {:.0f}".format(casinoBalance.value))
                moneySave()
            else:
                print("You lose. Your new balance: {:.0f}".format(casinoBalance.value))
#<----------/Heads or Tails---------->

#<----------Aviator---------->
    elif(mainMenuChoose == 2):
        value = 0.0
        min_range = 0
        max_range = random.uniform(0,50)
        increment = 0.1

        betAmount = int(input("Wallet: {:.0f}\nWelcome to Aviator Game enter your bet please: ".format(casinoBalance.value)))
        if(betAmount > casinoBalance.value or betAmount < 1):
            print("Invalid value.")
        else:
            moneyDecrase()
            while True:
                try:
                    if(value < max_range):
                        value += increment
                        time.sleep(0.2)
                        print("{:0.1f}".format(value))
                    else:
                        print("Wallet: {:.0f}".format(casinoBalance.value))
                        break
                except KeyboardInterrupt:
                        exitMoney = betAmount*value
                        casinoBalance.value += exitMoney
                        print("Your exit money: {:.0f}, your wallet: {:.0f}".format(exitMoney, casinoBalance.value))
                        ws["A1"]=casinoBalance.value
                        wb.save("casinobalance.xlsx")
                        break
#<----------/Aviator--------->

#<----------Guess---------->
    elif(mainMenuChoose == 3):
        betAmount = int(input("Wallet: {:.0f}\nWelcome to Guess Game enter your bet please: ".format(casinoBalance.value)))
        if(betAmount > casinoBalance.value or betAmount < 1):
            print("Invalid value.")
        else:
            moneyDecrase()
            number = random.randint(1,10)
            playerChoose = int(input("Choose a number between 1-10: "))
            if(number == playerChoose):
                betAmount *= 2
                casinoBalance.value += betAmount
                print("You won. Your new balance: {:.0f}".format(casinoBalance.value))
                moneySave()
            else:
                print("You lose. Your new balance: {:.0f}".format(casinoBalance.value))
#<----------/Guess---------->

#<----------Same Dice---------->
    elif(mainMenuChoose == 4):
        while True:
            betAmount = int(input("Wallet: {:.0f}\nWelcome to Guess Game enter your bet please\n0-) Exit:\n".format(casinoBalance.value)))
            if(betAmount > casinoBalance.value or betAmount < 0):
                print("Invalid value.")
            elif(betAmount == 0):
                print("Bye!")
                break
            else:
                moneyDecrase()
                firstDice = random.randint(1,6)
                secondDice = random.randint(1,6)
                if(firstDice == secondDice):
                    betAmount *= 2
                    casinoBalance.value += betAmount
                    print("First dice is {}, second dice is {}. You won.\nYour new balance: {:.0f}".format(firstDice,secondDice,casinoBalance.value))
                    moneySave()
                else:
                    print("First dice is {}, second dice is {}. You lose.\nYour new balance: {:.0f}".format(firstDice,secondDice,casinoBalance.value))
#<----------/Same Dice---------->
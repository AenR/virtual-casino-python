#<----------imports---------->
import sqlite3
from datetime import datetime
import random # Choosing random number
import time # For sleep command
from openpyxl import Workbook,load_workbook # For save balance
#<----------/imports---------->

#<----------variables---------->
db = sqlite3.connect('database.db')
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS casino(id, balance, daily)")
db.commit()
command = """SELECT * FROM casino"""
cursor.execute(command)
variable = cursor.fetchone()
casinoBalance = int(variable[1])

def moneySave():
    command = "UPDATE casino SET balance = ? WHERE id = ?"
    cursor.execute(command,(casinoBalance,'1'))
    db.commit()
#<----------/variables---------->

#<----------Main Menu---------->
while True:
    date = datetime.today() # Get today's info for daily reward
    today = date.day
    command = """SELECT * FROM casino"""
    cursor.execute(command)
    variable = cursor.fetchone()
    daily = int(variable[2])
    if (today < daily):
        print("Daily reward is not ready.")
    elif (today == daily):
        print("You have collected your daily reward.")
        command = "UPDATE casino SET balance = ? WHERE id = ?"
        x = casinoBalance + 200
        cursor.execute(command,(x,'1'))
        command = "UPDATE casino SET daily = ? WHERE id = ?"
        cursor.execute(command,(today+1,'1'))
    else:
        command = "UPDATE casino SET daily = ? WHERE id = ?"
        cursor.execute(command,(today+1,'1'))

    db.commit()
    mainMenuChoose = int(input("Welcome!\nYour Wallet: {:.0f}\n1-) Heads or Tails\n2-) Aviator\n3-) Guess\n4-) Same Dice\n5-) Slot\n6-) Roulette\n0-) Exit\n".format(casinoBalance)))

    if(mainMenuChoose == 0 or mainMenuChoose > 6): # Exit
        print("Bye!")
        break
#<----------/Main Menu---------->

#<----------Heads or Tails---------->
    elif(mainMenuChoose == 1):
        sonuc = random.randint(1,2)
        print("Welcome to Heads or Tails Game your wallet: {:.0f}".format(casinoBalance))
        while True: # Play until exit
            betAmount = int(input("Please enter your bet: \n0-) Exit\n"))
            if(betAmount>casinoBalance):
                print("Invalid value.")
                break
            if(betAmount==0): # Exit
                print("Bye!")
                break
            casinoBalance -= betAmount

            playerChoose = input("Heads or Tails?\n")
            if(playerChoose=="heads"):
                hort = 1
            if(playerChoose=="tails"):
                hort = 2
            if(sonuc==hort):
                betAmount *= 2
                casinoBalance += betAmount
                print("You won. Your new balance: {:.0f}".format(casinoBalance))
                moneySave()
            else:
                print("You lose. Your new balance: {:.0f}".format(casinoBalance))
#<----------/Heads or Tails---------->

#<----------Aviator---------->
    elif(mainMenuChoose == 2):
        value = 0.0
        min_range = 0
        max_range = random.uniform(0,50)
        increment = 0.1

        betAmount = int(input("Wallet: {:.0f}\nWelcome to Aviator Game enter your bet please: ".format(casinoBalance)))
        if(betAmount > casinoBalance or betAmount < 1):
            print("Invalid value.")
        else:
            casinoBalance -= betAmount
            while True:
                try:
                    if(value < max_range):
                        value += increment
                        time.sleep(0.2)
                        print("{:0.1f}".format(value))
                    else:
                        print("Wallet: {:.0f}".format(casinoBalance))
                        break
                except KeyboardInterrupt:
                        exitMoney = betAmount*value
                        casinoBalance += exitMoney
                        print("Your exit money: {:.0f}, your wallet: {:.0f}".format(exitMoney, casinoBalance))
                        command = "UPDATE casino SET balance = ? WHERE id = ?"
                        cursor.execute(command,(casinoBalance,'1'))
                        db.commit()
                        break
#<----------/Aviator--------->

#<----------Guess---------->
    elif(mainMenuChoose == 3):
        betAmount = int(input("Wallet: {:.0f}\nWelcome to Guess Game enter your bet please: ".format(casinoBalance)))
        if(betAmount > casinoBalance or betAmount < 1):
            print("Invalid value.")
        else:
            casinoBalance -= betAmount
            number = random.randint(1,10)
            playerChoose = int(input("Choose a number between 1-10: "))
            if(number == playerChoose):
                betAmount *= 2
                casinoBalance += betAmount
                print("You won. Your new balance: {:.0f}".format(casinoBalance))
                moneySave()
            else:
                print("You lose. Your new balance: {:.0f}".format(casinoBalance))
#<----------/Guess---------->

#<----------Same Dice---------->
    elif(mainMenuChoose == 4):
        while True:
            betAmount = int(input("Wallet: {:.0f}\nWelcome to Guess Game enter your bet please\n0-) Exit:\n".format(casinoBalance)))
            if(betAmount > casinoBalance or betAmount < 0):
                print("Invalid value.")
            elif(betAmount == 0):
                print("Bye!")
                break
            else:
                casinoBalance -= betAmount
                firstDice = random.randint(1,6)
                secondDice = random.randint(1,6)
                if(firstDice == secondDice):
                    betAmount *= 2
                    casinoBalance += betAmount
                    print("First dice is {}, second dice is {}. You won.\nYour new balance: {:.0f}".format(firstDice,secondDice,casinoBalance))
                    moneySave()
                    break
                else:
                    print("First dice is {}, second dice is {}. You lose.\nYour new balance: {:.0f}".format(firstDice,secondDice,casinoBalance))
                    break
#<----------/Same Dice---------->

#<----------Slot---------->
    elif(mainMenuChoose == 5):
        slotItems = ["🍒", "🍋", "🍉", "🍇", "💎", "🍀"]
        while True:
            betAmount = int(input("Wallet: {:.0f}\nWelcome to Slot Game enter your bet please\n0-) Exit:\n".format(casinoBalance)))
            if(betAmount > casinoBalance or betAmount < 0):
                print("Invalid value.")
            elif(betAmount == 0):
                print("Bye!")
                break
            else:
                casinoBalance -= betAmount
                slotMachine = [random.choice(slotItems) for i in range(3)]
                print(" ".join(slotMachine))
                if(slotMachine[0] == slotMachine[1] == slotMachine[2]):
                    betAmount *= 2
                    casinoBalance += betAmount
                    print("You won.\nYour new balance: {:.0f}".format(casinoBalance))
                    moneySave()
                else:
                    print("You lose. Your new balance: {:.0f}".format(casinoBalance))
#<----------/Slot---------->

#<----------Roulette---------->
    elif(mainMenuChoose == 6):
        while True:
            betAmount = int(input("Wallet: {:.0f}\nWelcome to Roulette Game enter your bet please\n0-) Exit:\n".format(casinoBalance)))
            if(betAmount > casinoBalance or betAmount < 0):
                print("Invalid value.")
            elif(betAmount == 0):
                print("Bye!")
                break
            else:
                wheelResult = random.randint(1,36)
                casinoBalance -= betAmount
                choose = int(input("Choose a number between 1-36: "))
                if(wheelResult == choose):
                    betAmount *= 36
                    casinoBalance += betAmount
                    print("You won.\nYour new balance: {:.0f}".format(casinoBalance))
                    moneySave()
                else:
                    print("Number is: {}\nYou lose. Your new balance: {:.0f}".format(wheelResult, casinoBalance))
#<----------/Roulette---------->
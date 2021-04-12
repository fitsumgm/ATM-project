
#***********ATM Authentication and basic bank operarion*****************

import random
import datetime, time

database = {}

def init():
    isvalidOptionSelected = False
    print("Welcome to BankPHP")

    while isvalidOptionSelected == False:

        haveAccount = int(input("Do you have an account with us? 1 (yes), 2 (no) \n"))

        if (haveAccount == 1):
            isvalidOptionSelected = True
            login()
        elif (haveAccount == 2):
            isvalidOptionSelected = True
            print(register())
        else:
            print("You have selected invalid option")

    
def login():
    print("*******Login*******")
    accountNumberFromUser = int(input("what is your accountNumber? \n"))
    password = input("What is your password? \n")
        
    for accountNumber,userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            
            if(userDetails[3] == password):
                print('Welcome ' + userDetails[0])
                print(time.strftime("%a, %d %b %Y %H:%M:%S \n"))
                
        else:
                print("Invalid account or password")
                login()

    bankOperation()


def register():
    print("*******Registeration*******")
    
    first_name = input("What is your name? \n")
    last_name = input("What is your last name? \n")
    email = input("What is your email address? \n")
    password = input("Create a password \n")
     
    accountNumber = generatingAccountNumber()
    database[accountNumber] = [first_name, last_name, email, password]
    #userDetails = database
    print("Account setup successful")
    print("Your account number is %d \n" %accountNumber)
    login()


def withdraw(currentBalance):

    print('Your balance is %d' % currentBalance)
    withdrawal = int(input('How much would you like to withdraw: \n'))

    if(withdrawal > currentBalance):
        print('You do not have enough balance \n')
        withdraw(currentBalance)


    elif(withdrawal <= currentBalance):
        print('Please take your cash \n')
        bankOperation()
    else:
        print('wrong input')
        withdraw()
            

def Deposit(currentBalance):
    print('How much would you like to deposit?')
    deposit = int(input(''))
    currentBalance += deposit
    print('Your currenct balance is %d \n' %currentBalance)
    bankOperation()

def logout():
    print('Logged out. \n')
    init()


def bankOperation():
    print('What would you like to do? \n')
    print('1. Withdraw \n''2. Deposit \n''3. logout \n' '4. Exit \n')
    selectedOption = int(input(''))
    balance = 1000
   

    if(selectedOption == 1):
        withdraw(balance)

    elif(selectedOption == 2):
        Deposit(balance)


    elif(selectedOption == 3):
        logout()

    elif(selectedOption == 4):
        print("Thank you for visiting us! \n")
        exit

    else:
        print('Invalid selection, please try again')
        bankOperation()

    
def generatingAccountNumber():
    return random.randrange(1111111111,9999999999)

init()

#***********ATM Authentication and basic bank operarion*****************

import os
import random
import datetime, time
import database
import validation

currentBalance = 1000
logout = 0

#Program initialization

def generatingAccountNumber():
    return random.randrange(1111111111,9999999999)

accountNumber = generatingAccountNumber()

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
    accountNumberFromUser = input("what is your accountNumber? \n")

    is_valid_account_number = validation.account_number_validation(accountNumberFromUser)

    if is_valid_account_number:
        
        password = input("What is your password? \n")
  
        
        user = database.authenticated_user(accountNumberFromUser, password);

        if user:
            print('Welcome %s, %s' % (user[0],user[1]))
            print(time.strftime("%a, %d %b %Y %H:%M:%S \n"))
            f = open('Data/auth_session/' + str(accountNumberFromUser) + ".txt", "x")
            f.write("User logged: " + str(time.strftime("%a, %d %b %Y %H:%M:%S")));
            f.close()

            bankOperation(currentBalance)

        print('Invalid account or password')
        login()
        
                    
    else:
        print("Invalid account number, please try again")
        login()


def register():
    print("*******Registeration*******")
    
    first_name = input("What is your name? \n")
    last_name = input("What is your last name? \n")
    email = input("What is your email address? \n")
    password = input("Create a password \n")
     
    #accountNumber = generatingAccountNumber()

    is_user_created = database.creat(accountNumber,first_name, last_name, email, password, currentBalance)


    if is_user_created:

        print("Account setup successful")
        print("Your account number is %d \n" %accountNumber)
        login()

    else:
        print("Please try again")
        register()


def withdraw(currentBalance):

    print('Your available balance is %d' % currentBalance)
    withdrawal = int(input('How much would you like to withdraw: \n \n'))

    if(withdrawal > currentBalance):
        print('You do not have enough balance \n')
        withdraw(currentBalance)


    elif(withdrawal <= currentBalance):
        currentBalance -= withdrawal
        print('Please take your cash, remaining balance is %d. \n' %currentBalance)
        bankOperation(currentBalance)
    else:
        print('wrong input')
        withdraw(currentBalance)
            

def Deposit(currentBalance):
    print('How much would you like to deposit?')
    deposit = int(input(''))
    currentBalance += deposit
    print('Your currenct balance is %d. \n' %currentBalance)
    bankOperation(currentBalance)

def logout():
    print('Logged out. \n')
    init()


def bankOperation(currentBalance):
    print('What would you like to do? \n')
    print('1. Withdraw \n''2. Deposit \n''3. logout \n' '4. Exit \n')
    selectedOption = int(input(''))


    if(selectedOption == 1):
        withdraw(currentBalance)

    elif(selectedOption == 2):
        Deposit(currentBalance)


    elif(selectedOption == 3):
        database.delete(accountNumber)
        logout()

    elif(selectedOption == 4):
        print("Thank you for visiting us! \n")
        database.delete(accountNumber)
        exit()

    else:
        print('Invalid selection, please try again')
        bankOperation(currentBalance)

    
def generatingAccountNumber():
    return random.randrange(1111111111,9999999999)

init()
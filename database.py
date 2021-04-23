# program to managing user data

import os
import validation

user_db_path = 'Data/user_record/'
user_db_path1 = 'Data/auth_session/'

def creat(accountNumber,first_name, last_name, email, password, currentBalance):

    completion_state = False
   
    user_data = first_name + "," + last_name + "," + email + "," + password + "," + str(1000)

    if does_account_number_exist(accountNumber):

        return False

    if does_email_exist(email):
        print("User already exists")
        return False

    completion_state = False

    try:

        f = open(user_db_path + str(accountNumber) + ".txt", "x")

    except FileExistsError:

        does_file_contain_data = read(user_db_path + str(accountNumber) + ".txt")
        if not does_file_contain_data:
            delete(accountNumber)

    else:

        f.write(str(user_data));
        completion_state = True

    finally:

        f.close();
        return completion_state

def read(accountNumber):

    # find user with account number
    # fetch content of the file
    is_valid_account_number = validation.account_number_validation(accountNumber)

    try:

        if is_valid_account_number:
            f = open(user_db_path + str(accountNumber) + ".txt", "r")

        else:
            f = open(user_db_path + accountNumber, "r")

    except FileNotFoundError:

        print("User not found")

    except FileExistsError:

        print("User doesn't exist")

    except TypeError:

        print("Invalid account number format")

    else:

        return f.readline()

    return False


def update(accountNumber):
    print("update user record")
    # find user with account number
    # fetch the content of the file
    # update the content of the file
    # save the file
    # return true


def delete(accountNumber):

    # find user with account number
    # delete the user record (file)
    # return true

    is_delete_successful = False

    if os.path.exists(user_db_path1+ str(accountNumber) + ".txt"):

        try:

            os.remove(user_db_path1 + str(accountNumber) + ".txt")
            is_delete_successful = True

        except FileNotFoundError:

            print("User not found")

        finally:

            return is_delete_successful


def does_email_exist(email):

    all_users = os.listdir(user_db_path)

    for user in all_users:
        user_list = str.split(read(user), ',')
        if email in user_list:
            return True
    return False


def does_account_number_exist(accountNumber):

    all_users = os.listdir(user_db_path)

    for user in all_users:

        if user == str(accountNumber) + ".txt":

            return True

    return False


def authenticated_user(accountNumber, password):

    if does_account_number_exist(accountNumber):

        user = str.split(read(accountNumber), ',')

        if password == user[3]:
            return user

    return False

#print(creat(accountNumber))
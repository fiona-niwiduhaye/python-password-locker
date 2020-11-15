#!/usr/bin/env python3.6
'''

This is the file that runs the application
Import User Class from User Module and Credential Class from Credential Module
'''

from user import User
from credential import Credential

def create_user(name, password):
    '''
    Function to create a user account
    Args:
        name :  name the user wants for their account
        password :  password the user want for their account
    '''
      new_user = User(name,password)

    return new_user

def save_users(user):
    '''
    Function to save a user account
    Args:
        user : the user account to be saved
    '''
    user.save_user()

def check_existing_users(name):
    '''
    Function that checks if a user account name already exists
    Args:
        name : the user account name
    '''
     return User.user_exist(name)

def user_log_in(name, password):
    '''
    Function that allows a user to log into their credential account
    Args:
        name : the name the user used to create their  account
        password : the password the user used to create their  account
    '''
    log_in = User.log_in(name, password)
    if log_in != False:
        return User.log_in(name, password)

def display_users():
    '''
    Function that returns all the saved users 
    '''

    return User.display_user()
def create_credentail(user_password, name, password):
    '''
    Function to create a credential 
    Args:
        user_password : the password for Password Locker
        name : the name of the account 
        password : the password for the account
    '''

    new_credentail = Credential(user_password,name,password)

    return new_credentail

def save_credentials(credential):
    '''
    Function to save a credential
    Args:
        credential : the credential to be saved
    '''

    credential.save_credential()
def check_existing_credentials(name):
    '''
    Function that checks if a user credential name already exists
    Args:
        name : the credential name
    '''

    return Credential.credential_exist(name)

def display_credentials(password):
    '''
    Function that returns all the saved credentials
    '''

    return Credential.display_credential(password)

    def main():
    '''
    Function running the Password Locker app
    '''

    print("Welcome to Password Locker \n Use these short codes to get around")

    while True:
        '''
        Loop that is running the entire application
        '''

        print('''   Short codes:
        cu - create a Password Locker account \n
        du - display names of current Password Locker users \n
        lg - log into your Password Locker account \n
        ex - exit the Password Locker account''')
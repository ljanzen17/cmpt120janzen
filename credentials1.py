# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions 
# Author: Lucas Janzen
# Created: 2018-09-25
# This is the second part of the lab

def name():
    first = input("Enter your first name: ").lower()
    last = input("Enter your last name: ").lower()
    name = (first+"."+last)
    name.split(".")
    return(name)

def username(name):
    uname = (name+"@marist.edu")
    return(uname)

def passwdlength():
    password = input("Create a new password: ")
    if passwordCase(password):
        print("Valid password")
    while len(password) < 8:
        print("Fool of a Took! That password is feeble!")
        password = input("Create a new password: ")
    print("The force is strong in this one…")
    
    return(password)

def finish(user):
    print("Account configured. Your new email address is",
    user + "@marist.edu")

def passwordCase (password):
    letters = set(password)

    lower = any(letter.islower() for letter in letters)
    upper = any(letter.isupper() for letter in letters)

    if not upper:
        print("This password is invalid. Add upper case letters.")
        return(False)
    if not lower:
        print("This password is invalid. Add lower case letters.")
        return(False)
    return(True)



def main():
    # get user's first and last names and
    #modify this to generate a Marist-style username
    user = username(name())
    # ask user to create a new password
    pwd = passwdlength()
    # tell user their final info
    info = finish(user)
   
main()

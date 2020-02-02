# Winson Gin
# CPSC 332; 5:30-6:45pm
# Professor Reed
# Assignment 5
import mysql.connector
import sys

print("Welcome to Winson's MySQL Program! Please type the number that corresponds to the task that you would like to complete")
userInput = input("Please enter the database that you want to access: ")

myDb = mysql.connector.connect(host = "localhost", user = "root", passwd = "ForSchoolUse", database = userInput)

def menu():
    print("Please type \'Q\' to quit")
    print("1. Print records from the database")
    print("2. Access a record based on an attribute value")
    print("3. Sort a report")
    choice = input()

    if choice == "1":
        myCursor = myDb.cursor()
        userInput = input("Which table records would you like to print? ")
        query = "SELECT * FROM {}"
        myCursor.execute(query.format(userInput))
        myResult = myCursor.fetchall()
        for x in myResult:
            print(x)
        print("\n")
        menu()

    if choice == "2":
        myCursor = myDb.cursor()
        userInput = input("Which table records would you like to access? ")
        userInput2 = input("Please enter the attribute: ")
        userInput3 = input("Please enter the attribute value: ")
        query = "SELECT * FROM {} WHERE {} = '{}'"
        myCursor.execute(query.format(userInput, userInput2, userInput3))
        myResult = myCursor.fetchall()
        for x in myResult:
            print(x)
        print("\n")
        menu()

    if choice == "3":
        myCursor = myDb.cursor()
        userInput = input("Which table records would you like to access? ")
        userInput2 = input("Please enter the attribute you would like to sort: ")
        print("Please enter which order you would like to sort it in (A = Ascending/D = Descending): ")
        sortDecision = input()
        if sortDecision == "A":
            query = "SELECT * FROM {} ORDER BY {}"
            myCursor.execute(query.format(userInput, userInput2))
            myResult = myCursor.fetchall()
            for x in myResult:
                print(x)
            print("\n")
            menu()
        else:
            query = "SELECT * FROM {} ORDER BY {} DESC"
            myCursor.execute(query.format(userInput, userInput2))
            myResult = myCursor.fetchall()
            for x in myResult:
                print(x)
            print("\n")
            menu()
    if choice == "Q":
        sys.exit()
menu()

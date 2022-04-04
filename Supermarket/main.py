from cProfile import run
from database import *
from login import *
from stores import *

'''def start():
    Role = input("Please Enter Your Role ")

    if Role == "Till operator" or Role == "till operator":
        starting.TO()

    if Role == "Store Manager" or Role == "store manager":
        starting.SM()

    if Role == "Stock controller" or Role == "stock controller":
        starting.SC()

    if Role == "Financial consultant" or Role == "financial consultant":
        starting.TC()'''


class starting():
    def TO():

        menu = input("Choose from the following options: Search stock, Logout ")

        if menu == "Search stock" or menu == "search stock":
            one = input("Do you want to search all stock or one item? ")

            if one == "All stock" or one == "all stock":
                store.Searchstockall()
                starting.TO()

            elif one == "One item" or one == "one item":
                store.Searchstock()
                starting.TO()

            else:
                print("Invalid Choice. Please check and try again")
                starting.TO()

        elif menu == "Logout" or menu == "logout":
            starting.TO()

        elif menu == "Test" or menu == "test":
            employee.account()
            starting.TO()

        elif menu == "Test1" or menu == "test1":
            employee.login()

        else:
            print("Invalid Choice. Please check and try again")
            starting.TO()

    def SM():

        menu = input("Hello:"  "Choose from the following options: Store(Add item, Remove item) Staff(Add staff, Remove staff, View all staff, Update staff) Logout ")
        if menu == "Add item" or menu == "add item":
            store.AddItem()
            starting.SM()
        elif menu == "Remove item" or menu == "remove item":
            store.Removeitem()
            starting.SM()
        elif menu == "Add staff" or menu == "add staff":
            employee.addstaff()
            starting.SM()
        elif menu == "View all staff" or menu == "view all staff":
            employee.findallstaff()
            starting.SM()
        elif menu == "Remove staff" or menu == "remove staff":
            employee.removestaff()
            starting.SM()
        elif menu == "Update staff" or menu == "update staff":
            updatestaffs = input("Would you like to: Update staff role, Update staff salary ")
            if updatestaffs == "Update staff role" or updatestaffs == "update staff role":
                employee.updatestaffrole()
                starting.SM()
            elif updatestaffs == "Update staff salary" or updatestaffs == "update staff salary":
                employee.updatestaffsalary()
                starting.SM()
            else:
                print("No valid option chosen")
                starting.SM()
        elif menu == "Logout" or menu == "logout":
            starting.TO()

    def SC():
        menu = input("Hello:" "User" "Choose from the following options: Update stock, Logout ")
        if menu == "Update stock" or menu == "update stock":
            store.Updatestock()
            starting.SC()
        elif menu == "Logout" or menu == "logout":
            starting.TO()
        else:
            print("No valid option chosen")
            starting.SC()

    def TC():
        menu = input("Hello:" "User" "Choose from the following options: Update cost, Logout ")
        if menu == "Update cost" or menu == "update cost":
            store.Updatecost()
            starting.TC()
        elif menu == "Logout" or menu == "logout":
            starting.TO()
        else:
            print("No valid option chosen")
            starting.TC()



starting.TO()
'''====================================(Initilize Ports/Database)===================================='''
from pymongo import MongoClient

host = "localhost"
port = 27017
client = MongoClient(host, port)
tesgo = client["Store"]
item_collection = tesgo["Stock"]
staff_collection = tesgo["Staff"]
#client.close()





'''================================================(Store functions)================================================'''
class store():
    '''====================================(Remove Item From Database)===================================='''
    def Removeitem():
        remove = input("What item do you want to remove ")
        results = item_collection.collection.delete_many({"Name": remove })
        print("\nDeleted %d items" %(results.deleted_count))
    '''====================================(Search One Item)===================================='''
    def Searchstock():
        Search = input("Please Enter The Item Name")
        myquery = {"Name": Search }

        doc = item_collection.collection.find_one(myquery)

        if doc is not None:
            print(doc)
        else:
            print("Item not found: " )
    '''====================================(Search All Stock)===================================='''
    def Searchstockall():
        search = item_collection.collection.find()
        for document in search:
            print(document)
    '''====================================(Add Item)===================================='''    
    def AddItem():
        item1 = input("Please Enter Your First Item Name ")
        
        myquery = {"Name": item1 }
        doc = item_collection.collection.find_one(myquery)

        if doc is not None:
            print("Item already exists")

        else:
            item2 = int(input("Please Enter Your First Item Price "))
            item3 = int(input("Please Enter Your First Item Stock "))

            Item = {"Name": item1, "Price": item2, "Stock left": item3}
            new_id = item_collection.collection.insert_one(Item)
            print("Inserted item with id %s" % new_id.inserted_id)
    '''====================================(Update Stock)===================================='''
    def Updatestock():
        
        input2 = input("What item do you want to update ")
        itemname = {"Name": input2}

        
        addstock = input("How much stock is left for this item ")
        newvalue = {"$set": {"Stock left" : addstock}}

        result1 = item_collection.collection.update_one(itemname, newvalue)
        print("%d Items matched, %d Item prices updated"%(result1.matched_count, result1.modified_count))

    def Updatecost():
        input1 = input("What item do you want to update")
        itemname = {"Name": input1}

        cost = input("What would you like the cost to be? ")
        costvalue = {"$set": {"Price": cost}}

        result = item_collection.collection.update_one(itemname, costvalue)
        print("%d Items matched, %d Item prices updated"%(result.matched_count, result.modified_count))

class employee():
    '''===================================(Creating new accounts)======================================='''
    def account():
        newlogin = input("Please Enter a username ")
        newpassword = input("Please Enter a password")
        newloginquery = {"Login": newlogin }
        newpasswordquery = {"Password": newpassword}
        doc = staff_collection.collection.find_one(newloginquery)

        if doc is not None:
            print("Username already exists please enter a new username")
        else:
            loginitem = {"Login": newlogin}
            passitem = {"Password": newpassword}
            logitem = {"Login": newlogin, "Password": newpassword}

            new_id = staff_collection.collection.insert_one(logitem)
            print("Inserted item with id %s" % new_id.inserted_id)

    '''==============================(Adding logins for employee protection)============================'''
    def login():
        login = input("Please Enter your username ")
        password = input("Please Enter your password ")
        lquery = {"Login": login}
        pquery = {"Password": password}
        login1 = staff_collection.collection.find_one(lquery)
        if login1 is not None:
            print("User successfully logged in")
            login2 = staff_collection.collection.find_one(pquery)
            if login2 is not None:
                start()
            else:
                print("Wrong password")
        else:
            print("No User Found")

    '''====================================(Add Staff Into Database)===================================='''
    def addstaff():
        Staff = input("Please Enter Your Full Name ")
        
        myquery = {"Full Name": Staff }
        doc = staff_collection.collection.find_one(myquery)

        if doc is not None:
            print("Item already exists")

        else:
            Jobrole = input("Please Enter Your Job Role  ")
            Salary = input("Please Enter Your Salary ")

            Item = {"Full Name": Staff, "Job_Role": Jobrole, "Salary": Salary}

            new_id = staff_collection.collection.insert_one(Item)
            print("Inserted item with id %s" % new_id.inserted_id)
    '''====================================(Remove Staff From Database)===================================='''
    def removestaff():
        remove = input("What staff member do you want to remove ")
        results = staff_collection.collection.delete_many({"Full Name": remove })
        print("\nDeleted %d items" %(results.deleted_count))
    '''====================================(Update a current staff member)===================================='''
    def updatestaff():
        input1 = input("What staff name do you want to update? ")
        itemname = {"Full Name": input1}

        
        input2 = input("What full name do you want to update to? ")
        newvalue = {"$set": {"Full Name" : input2}}

        result1 = staff_collection.collection.update_one(itemname, newvalue)
        print("%d Staff members matched, %d Staff members updated"%(result1.matched_count, result1.modified_count))
    '''====================================(Find All Staff In Database)===================================='''
    def findallstaff():
        search = staff_collection.collection.find()
        for staff in search:
            print(staff)
    '''====================================(Update current Staff role)===================================='''
    def updatestaffrole():
        input1 = input("What staff name would you like to update? ")
        itemname = {"Full Name": input1}

        
        role = input("What role would you like to update to? ")
        newvalue = {"$set": {"Job_Role" : role}}

        result1 = staff_collection.collection.update_one(itemname, newvalue)
        print("%d Staff members matched, %d Staff roles updated"%(result1.matched_count, result1.modified_count))
    '''====================================(Update Current Staff Salary)===================================='''
    def updatestaffsalary():
        input1 = input("What staff name would you like to update? ")
        itemname = {"Full Name": input1}

        
        sal = input("What salary would you like to update him to?  ")
        newvalue = {"$set": {"Salary" : sal}}

        result1 = staff_collection.collection.update_one(itemname, newvalue)
        print("%d Staff members matched, %d Staff salarys updated"%(result1.matched_count, result1.modified_count))

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
            start()

        elif menu == "Test" or menu == "test":
            employee.account()

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
            start()

    def SC():
        menu = input("Hello:" "User" "Choose from the following options: Update stock, Logout ")
        if menu == "Update stock" or menu == "update stock":
            store.Updatestock()
            starting.SC()
        elif menu == "Logout" or menu == "logout":
            start()
        else:
            print("No valid option chosen")
            starting.SC()

    def TC():
        menu = input("Hello:" "User" "Choose from the following options: Update cost, Logout ")
        if menu == "Update cost" or menu == "update cost":
            store.Updatecost()
            starting.TC()
        elif menu == "Logout" or menu == "logout":
            start()
        else:
            print("No valid option chosen")
            starting.TC()

def start():
    Role = input("Please Enter Your Role ")

    if Role == "Till operator" or Role == "till operator":
        starting.TO()

    if Role == "Store Manager" or Role == "store manager":
        starting.SM()

    if Role == "Stock controller" or Role == "stock controller":
        starting.SC()

    if Role == "Financial consultant" or Role == "financial consultant":
        starting.TC()


#start()

employee.login()
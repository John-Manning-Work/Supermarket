from database import *

'''(Creating employee)'''
class employee():
    
    
    '''====(Creating new accounts)===='''
    def account():
        newlogin = input("Please Enter a username ")
        newpassword = input("Please Enter a password ")
        newjob = input("Please enter job role ")

        newloginquery = {"Login": newlogin }

        doc = staff_collection.collection.find_one(newloginquery)

        if doc is not None:
            print("Username already exists please enter a new username")
        else:
            logitem = {"Login": newlogin, "Password": newpassword, "Job_Role": newjob}

            new_id = staff_collection.collection.insert_one(logitem)
            print("Inserted item with id %s" % new_id.inserted_id)

    
    '''====(Adding logins for employee protection)===='''
    def login():
        from main import starting
        login = input("Please Enter your username ")
        password = input("Please Enter your password ")
        lquery = {"Login": login}
        pquery = {"Password": password}
        jquery = {"Job_Role": "till operator"}
        
        
        login1 = staff_collection.collection.find_one(lquery)
        if login1 is not None:
            print("User successfully logged in")
            login2 = staff_collection.collection.find_one(pquery)
            if login2 is not None:
                print("Success")
                print(pquery)
                
                login3 = staff_collection.collection.find_one(jquery)
                if login3 is not None:
                    print(login3)
                    starting.SM()
                else:
                    print("Not working")
                    print(login3)
            else:
                print("Wrong password")
        else:
            print("No User Found")

    
    '''====(Add Staff Into Database)===='''
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
    
    
    '''====(Remove Staff From Database)===='''
    def removestaff():
        remove = input("What staff member do you want to remove ")
        results = staff_collection.collection.delete_many({"Login": remove })
        print("\nDeleted %d items" %(results.deleted_count))
    
    
    '''====(Update a current staff member)===='''
    def updatestaff():
        input1 = input("What staff name do you want to update? ")
        itemname = {"Full Name": input1}

        
        input2 = input("What full name do you want to update to? ")
        newvalue = {"$set": {"Full Name" : input2}}

        result1 = staff_collection.collection.update_one(itemname, newvalue)
        print("%d Staff members matched, %d Staff members updated"%(result1.matched_count, result1.modified_count))
    
    
    '''====(Find All Staff In Database)===='''
    def findallstaff():
        search = staff_collection.collection.find()
        for staff in search:
            print(staff)
    
    
    '''====(Update current Staff role)===='''
    def updatestaffrole():
        input1 = input("What staff name would you like to update? ")
        itemname = {"Full Name": input1}

        
        role = input("What role would you like to update to? ")
        newvalue = {"$set": {"Job_Role" : role}}

        result1 = staff_collection.collection.update_one(itemname, newvalue)
        print("%d Staff members matched, %d Staff roles updated"%(result1.matched_count, result1.modified_count))
    
    
    '''====(Update Current Staff Salary)===='''
    def updatestaffsalary():
        input1 = input("What staff name would you like to update? ")
        itemname = {"Full Name": input1}

        
        sal = input("What salary would you like to update him to?  ")
        newvalue = {"$set": {"Salary" : sal}}

        result1 = staff_collection.collection.update_one(itemname, newvalue)
        print("%d Staff members matched, %d Staff salarys updated"%(result1.matched_count, result1.modified_count))

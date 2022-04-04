from database import *

'''==(Store functions)=='''
class store():


    '''==(Remove Item From Database)=='''
    def Removeitem():
        remove = input("What item do you want to remove ")
        results = item_collection.collection.delete_many({"Name": remove })
        print("\nDeleted %d items" %(results.deleted_count))


    '''==(Search One Item)=='''
    def Searchstock():
        Search = input("Please Enter The Item Name")
        myquery = {"Name": Search }

        doc = item_collection.collection.find_one(myquery)

        if doc is not None:
            print(doc)
        else:
            print("Item not found: " )


    '''==(Search All Stock)=='''
    def Searchstockall():
        search = item_collection.collection.find()
        for document in search:
            print(document)


    '''==(Add Item)=='''    
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


    '''==(Update Stock)=='''
    def Updatestock():
        
        input2 = input("What item do you want to update ")
        itemname = {"Name": input2}

        
        addstock = input("How much stock is left for this item ")
        newvalue = {"$set": {"Stock left" : addstock}}

        result1 = item_collection.collection.update_one(itemname, newvalue)
        print("%d Items matched, %d Item prices updated"%(result1.matched_count, result1.modified_count))


    '''==(Update Cost)=='''
    def Updatecost():
        input1 = input("What item do you want to update")
        itemname = {"Name": input1}

        cost = input("What would you like the cost to be? ")
        costvalue = {"$set": {"Price": cost}}

        result = item_collection.collection.update_one(itemname, costvalue)
        print("%d Items matched, %d Item prices updated"%(result.matched_count, result.modified_count))
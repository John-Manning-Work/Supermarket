'''==(Initilize Ports/Database)=='''
from pymongo import MongoClient
host = "localhost"
port = 27017
client = MongoClient(host, port)
tesgo = client["Store"]
item_collection = tesgo["Stock"]
staff_collection = tesgo["Staff"]
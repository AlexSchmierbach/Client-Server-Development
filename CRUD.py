from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        # accuser
        # SNHU1234
        USER = username
        PASS = password
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32129
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return False

# Create method to implement the R in CRUD.
    def read(self, query):
        result = self.database.animals.find(query)
        return list(result) if result else []

# Create method to implement the U in CRUD.
    def update(self, query, update_data):
        result = self.database.animals.update_many(query, {'$set': update_data})
        return {'modified_count': result.modified_count}
    
# Create method to implement the D in CRUD.
    def delete(self, query):
        result = self.database.animals.delete_many(query)
        return {'deleted_count': result.deleted_count}


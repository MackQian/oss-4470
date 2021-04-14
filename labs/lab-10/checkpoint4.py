from pymongo import MongoClient
from bson.objectid import ObjectId
import pprint
client = MongoClient()

if __name__ == "__main__":
    db = client.mongo_db_lab

    print('fetch all')
    for definition in db.definitions.find():
        pprint.pprint(definition)

    print('fetch one')
    pprint.pprint(db.definitions.find_one())

    print('fetch a specific record')
    pprint.pprint(db.definitions.find_one({'word': 'Random'}))

    print('fetch using object id')
    pprint.pprint(db.definitions.find_one({'_id': ObjectId('56fe9e22bad6b23cde07b931')}))

    print('insert new')
    db.definitions.insert_one({'word': 'foo', 'definition': 'n. a word used for method and variable names'})
    pprint.pprint(db.definitions.find_one({'word': 'foo'}))
from pymongo import MongoClient
import datetime
import random
import pprint
client = MongoClient()
db = client.mongo_db_lab


def random_word_requester():
    '''
    This function should return a random word and its definition and also
    log in the MongoDB database the timestamp that it was accessed.
    '''
    word=list(db.definitions.aggregate([{ '$sample': { 'size': 1 } }]))[0]
    db.definitions.update_one({'_id': word['_id']}, {'$push': {'dates': datetime.datetime.isoformat(datetime.datetime.utcnow())}})
    return word['word']

if __name__ == '__main__': 
    words=[]
    word=''
    while True:
        word=(random_word_requester())
        if word in words:
            break
        words.append(word)
    pprint.pprint((db.definitions).find_one({'word': word}))

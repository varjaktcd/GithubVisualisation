#here we access our stored data
import pymongo
import pprint

conn ="mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

db = client.classDB

githubuser = db.githubuser.find()

for user in githubuser:
    pprint.pprint(user)
    print()
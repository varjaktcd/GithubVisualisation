import pymongo

conn ="mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

db = client.classDB

db.githubuser.delete_many([])

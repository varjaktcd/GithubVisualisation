import json #for dict to string
import pymongo
from github import Github

input = input("Please login by entering your Github access token:")

token = Github(input)
#have the user enter their access token

#get user from token
user = token.get_user()

#dictionary
dct = {'user': user.login,
       'fullname': user.name,
       'location': user.location,
       'company' : user.company
}


#store dct in mongodb

#remove null fields. shouldnt include null fields in mongo db's

#this should be in a unit test function
for k,v in dict(dct).items():
       if v is None:
              del dct[k]

print ("dictionary: " + json.dumps(dct))

#establish connection
conn ="mongodb://localhost:27017"
#this port matches the one in docker-compose.yml
client = pymongo.MongoClient(conn)

#create database
db = client.classDB

db.githubuser.insert_many([dct])

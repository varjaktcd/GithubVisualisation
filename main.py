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

#number of commits for a repo
for repo in g.get_user().get_repos():
    print(repo.name, repo.get_commits().totalCount)

    # dictionary
    dct2 = {'repo': repo.name,
           'commits': repo.get_commits().totalCount,
           }

#remove null fields here
for i,j in dict(dct).items():
       if j is None:
              del dct2[i]

print ("dictionary2: " + json.dumps(dct2))


#establish connection
conn ="mongodb://localhost:27017"
#this port matches the one in docker-compose.yml
client = pymongo.MongoClient(conn)

#create databases
db = client.classDB

db.githubuser.insert_many([dct])

db2 = client.classDB

db2.githubuser.insert_many([dct2])


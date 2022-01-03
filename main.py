import json #for dict to string
import pymongo
from github import Github

input = input("Please login by entering your Github access token:")

token = Github(input)
#have the user enter their access token

#get user from token
user = token.get_user()


print("Showing data for " + user.login)

#number of commits for a repo
for repo in g.get_user().get_repos():
    print(repo.name, repo.get_commits().totalCount)

# dictionary
dct = {'repo': repo.name,
       'commits': repo.get_commits().totalCount,
       }

#remove null fields here
for i,j in dict(dct).items():
       if j is None:
              del dct[i]

print("dictionary: " + json.dumps(dct))


#establish connection
conn ="mongodb://localhost:27017"
#this port matches the one in docker-compose.yml
client = pymongo.MongoClient(conn)

#create databases
db = client.classDB

db.githubuser.insert_many([dct])




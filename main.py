import json #for dict to string
import pymongo
from github import Github

g = Github()

input = input("Please enter the Github user to view:")

#get user
user = g.get_user(input)

print("Getting public repos...")

#number of commits per repo
print("Creating dictionary...")
repos =[]
commits = []

for repo in user.get_repos('all'):
    repos.append(repo.name)
    commits.append(repo.get_commits().totalCount)

#have it remove null cases

print(repos) #keys
print(commits)  #values

dct = {}

dct = dict(zip(repos, commits))

print("dictionary: " + json.dumps(dct))

print("Establishing connection...")

#establish connection
conn ="mongodb://localhost:27017"
#this port matches the one in docker-compose.yml
client = pymongo.MongoClient(conn)

print("Creating database...")
#create databases
db = client.classDB

db.repos.insert_many([dct])




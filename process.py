#here we access our stored data
import pymongo
import pprint
from matplotlib import pyplot as plt
import numpy as np

conn ="mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

db = client.classDB

repositories = db.repos.find()
#returns a cursor, which we msut iterate to get our dict back

print(repositories) #this is a cursor object

for repo in repositories:
   #pprint.pprint(repo)
   repo.pop('_id') #remove the objectID stuff
   print(repo)  # this is our dict!

# split dict into two lists, keys(repos) and values(commits)
keys = repo.keys()
values = repo.values()

print(keys)
print(values)

# The pie chart visualises the number
# of repos a user has and how many commits
# were made in each repo.

plt.pie(values, labels=keys)
plt.axis('equal')
plt.show()




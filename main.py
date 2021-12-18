import json #for dict to string

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

print ("dictionary: " + json.dumps(dct))


from github import Github

#access token. I'm using a second Github account for
#this module so I don't mind including it
#in source code

token = Github("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")
#have the user enter their access token

#get user from token
user = token.get_user()

#print user info
print("user:  " + user.login)

if user.name is not None:
    print("fullname: " + user.name)

if user.location is not None:
    print("location: " + user.location)

if user.company is not None:
    print("company: " + user.company)
curusers = ["yack", "jack", "smack", "rack", "admin"]
newusers = ["yack", "black", "track", "rack", "admin"]

for user in newusers:
    for users in curusers:
        if user.lower() == users.lower():
            print('You need a new username!')
        else:
            print('Nice username! It\'s avilable btw.')
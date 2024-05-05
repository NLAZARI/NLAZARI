myFriends = []
blocked = []

friendRequest = input("Can you code? > ")
yourName = input("What is your name? > ")

if yourName not in myFriends & yourName not in blocked:
    if friendRequest == "yes" & yourName not in myFriends:
        myFriends.append(yourName)
        print("Your friend request has been sent")
    else:
        blocked.append(yourName)
        print("Sorry, you have been blocked")
elif yourName in myFriends:
    print("You are already my friend :)")
else:
    print("Sorry you are blocked :(")

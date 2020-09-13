 # Get instance 
import instaloader

def getFollowers(today):
    followerList = []

    # Create login
    instaloadera = instaloader.Instaloader()
    instaloadera.login("your_username", "your_password") 

    # Obtain profile metadata
    profile = instaloader.Profile.from_username(instaloadera.context, "to_check_username")

    for follower in profile.get_followers():
        followerList.append(follower.username)

    with open(today, 'w') as f:
        for s in followerList:
            f.write(str(s) + '\n')
    




def getAssholes(yesterday, today):
    assholes = []
    for follower in yesterday:
        if follower not in today:
            assholes.append(follower)
    return assholes

            
def getNewOnes(yesterday, today):
    newOnes = []
    for follower in today:
        if follower not in yesterday:
            newOnes.append(follower)
    return newOnes











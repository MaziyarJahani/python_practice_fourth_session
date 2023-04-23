import instaloader
#instaloader has a github page. it can do so many things in instagram.
import getpass


f = open("python_practice_fourth_session/followers.txt", "r")
old_followers = []
for line in f:
    old_followers.append(line)
f.close()


L = instaloader.Instaloader()
username = input("enter username: ")
password = getpass.getpass("enter password: ")
L.login("maziyarjahani", "sth")
print("connected")


profile = instaloader.Profile.from_username(L.context, "maziyarjahani")
new_followers = []
for follower in profile.get_followers():
    new_followers.append(follower)
    
your_new_followers = []
for new_follower in new_followers:
    if new_follower not in old_followers:
        your_new_followers.append(new_follower)


f = open("python_practice_fourth_session/followers.txt", "w")  
for follower in new_followers:
    f.write(follower + "\n")
f.close

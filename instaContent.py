import instaloader

loader = instaloader.Instaloader()

user = input("Enter the username: ")
print("Downloading.......")

loader.download_profile(user,profile_pic_only = False)
profile = instaloader.Profile.from_username(loader.context, user)

print("Dwnloaded")
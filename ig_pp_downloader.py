import instaloader

def download_ig_pp(username):
    
    loader = instaloader.Instaloader()
    
    try:
        loader.download_profile(username, profile_pic_only=True)
        print(f"{username} profile picture downloaded successfully")
    except instaloader.exceptions.ProfileNotExistsException:
        print(f"User {username} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


username = input('Enter the username of the profile:')
download_ig_pp(username)
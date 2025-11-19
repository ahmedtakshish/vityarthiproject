def write_username(username):
    with open("username.txt","a") as f:
        f.write(username+"/n")


username = input("enter your name: ")

# checks if the user is new or already registered
with open("username.txt","r") as f:
    data = f.readlines()
    if username in data:
        print("user is already registered")
    else:
        print("new user detected.")
        write_username(username)
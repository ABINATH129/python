# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username= input("Enter a username:")

if len(username)>12:
    print("your name can't be more than 12 characters")

elif not username.isdigit() == -1:
    print("your username must not contain digits")

elif not username.find(" ") == -1:
    print("your username can't contain any spaces")

else:
    print(f"welcome {username}")


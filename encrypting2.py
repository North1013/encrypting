import hashlib
import json

def encrypt():
    ...
def compare():
    ...

while True:
    menu = int(input("1 to login\n2 to add a user\n:"))
    if menu == 1:
        while True:
            username = input("Input username to add: ")
            crypt_user = hashlib.sha1(username.encode("utf-8")).hexdigest()
            with open("users.json", "r") as f:
                data = json.load(f)
                for s in data:
                    print(s)
                    if s == crypt_user:
                        print(s['name'])
                        print(s['password'])
                 
    elif menu == 2:
        while True:
            with open("users.json", "a") as f:
                username = input("Input username to add: ")
                password = input("Input password to add: ")
                f.write()

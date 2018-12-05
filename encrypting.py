"""

"""

import hashlib

words = []

while True:
    print("""
            1. To encrypt phrase
            2. To decrypt phrase
            3. To end
            """)
    menu = int(input(""))

    if menu == 1:
        print("""
                1. To overwrite phrase
                2. To append a new phrase
                """)
        menu = int(input(""))
        phrase = input("Input phrase to encrypt")
        if menu == 1:
            words = (hashlib.sha1(phrase.encode("utf-8")).hexdigest())
            print(words)
        elif menu == 2:
            words.append(
                    hashlib.sha1(
                        phrase.encode("utf-8")
                        ).hexdigest()
                        )
            print(words)
        else:
            print("Not a valid choice")
    elif menu == 2:
        ...
    elif menu == 3:
        break
    else:
        print("Not a valid choice")

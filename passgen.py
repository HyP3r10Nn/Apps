import random

numbers = [str(i) for i in range(10)]
Bchars = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
schars = list("abcdefghijklmnopqrstuvwxyz")
symbols = ["_", "-", "§", "'", "/", "*", "\\", " "]

all_chars = numbers + Bchars + schars + symbols

while True:
    try:
        num = int(input("input length of your password: "))
        if num <= 0:
            print("password length must be bigger than 0.")
        else:
            break
    except ValueError:
        print("please input number.")

password = "".join(random.choice(all_chars) for _ in range(num))

print("your generated password: ", password)

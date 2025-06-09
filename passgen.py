import random

numbers = [str(i) for i in range(10)]
Bchars = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
schars = list("abcdefghijklmnopqrstuvwxyz")
symbols = ["_", "-", "§", "'", "/", "*", "\\", " "]

all_chars = numbers + Bchars + schars + symbols

while True:
    try:
        num = int(input("Zadej délku hesla: "))
        if num <= 0:
            print("Délka musí být větší než 0.")
        else:
            break
    except ValueError:
        print("Zadej celé číslo!")

password = "".join(random.choice(all_chars) for _ in range(num))

print("Vygenerované heslo:", password)

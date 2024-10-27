number = int(input("Введіть число:"))
if number % 2 == 0:
    print("Число парне")
else:
    print("Число непарне")


num = int(input("Введіть число:"))
if num > 0:
    print("Число додатне")
elif num == 0:
    print("Число дорівнює нюлю")
else:
    print("Число від'ємне")


age = int(input("Введіть ваш вік:"))
if age >= 18:
     print("Ви повнолітній")
else:
     print("Ви неповнолітній")


number = int(input("Введіть число:"))
if number % 3 == 0 or number % 5 == 0:
    print(f"Число {number} є кратним 3 або 5.")
else:
    print(f"Число {number} не є кратним ні 3, ні 5.")
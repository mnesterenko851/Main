with open("practice.txt", "w") as file:
    file.write("Hi world!//n")
    file.write("This is a file handling practice.")
with open("pactice.txt," "r") as file:
    content = file.read()
    print(content)
    

import shutil
shutil.copy("practice.txt", "copy_of_practice.txt")


import os

if os.path.exists("copy_of_practice.txt"):
    os.remove("copy_of_practice.txt")
    print("Файл видалено.")
else:
    print("Файл не знайдено.")
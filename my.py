name = input("Введіть ваше ім'я:")
age = input("Введіть ваш вік:")
print(f"Привіт, {name}! Тобі {age} років")

def reverse_string(s):
    return s[::-1]
s = 'GitHub'
print(reverse_string(s))

vowels = "аеєиіїоуюяАЕЄИІЇОУЮЯ"
user_string = input("Введіть строку: ")
vowel_count = 0
for char in user_string:
    if char in vowels:
        vowel_count += 1
print(f"Кількість голосних літер у введеній строкі: {vowel_count}")
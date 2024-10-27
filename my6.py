for i in range(1, 21):
    if i % 2 == 0:
        print(i)


n = 10
factorial = 1
while n > 0:
     factorial *= n
     n -= 1
print(f"Факторіал числа: {factorial}")


a, b = 0, 1
while a < 100:
    print(a, end="")
    a, b = b, a + b


text = "hello world"
for char in text:
    if char != "":
        print(char)
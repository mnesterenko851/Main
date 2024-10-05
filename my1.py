numbers = []
for i in range(5):
    num = float(input(f"Введіть число {i+1}: "))
    numbers.append(num)
max_value = max(numbers)
min_value = min(numbers)
print(f"Максимальне число: {max_value}")
print(f"Мінімальне число: {min_value}")

def sum_list(lst):
    return sum(lst)
numders = [12, 10, 3, 20, 1]
print(sum_list(numders))  

my_list = [2, 2, 3, 4, 4, 5, 5, 6, 7, 8, 8, 8]
unique_elemets = list(set(my_list))
print(f"Унікальні елементи списку: {unique_elemets}")
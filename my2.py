my_tuple = (17, "Githab", 8.2, False, (4, 3, 2))
print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[2])
print(my_tuple[3])
print(my_tuple[4])

my_tuple1 = (1, 2, 3, 4, 5)
my_tuple2 = (6, 7, 8, 9, 10)
new_tuplen =  my_tuple1 + my_tuple2
print(new_tuplen)

def min_max(numbers):
     return min(numbers), max(numbers)
result = min_max([10, 60, 2,  90, 20])
print(result)

my_tuple = (1, 2, 3, 4, 2, 5, 2, 6)
element = 2
count_element = my_tuple.count(element)
index_element = my_tuple.index(element)
print(f"Кількість входжень елемента {element}: {count_element}")
print(f"Перший індекс елемента {element}: {index_element}")

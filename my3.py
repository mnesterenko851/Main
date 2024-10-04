my_list = [1, 1, 2, 3, 3, 4, 4, 5]
my_set = set(my_list)
print(my_set)

set1 = {5, 6, 7}
set2 = {7, 8, 9}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))

set1 = {3, 4, 5}
set2 = {4, 5, 6}
print(set1.symmetric_difference(set2))

set1 = {5, 6}
set2 = {5, 6, 7, 8}
print(set1.issubset(set2))
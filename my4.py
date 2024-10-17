students = {
    "student1": {"name": "John", "age": "24", "city": "New York"},
    "student2": {"name": "Alice", "age": "25", "city": "Los Angeles"}
}
print(students["student1"]["city"])


text = "orange orange orange apple apple banana"
word_count = {}
for word in text.split():
    word_count[word] = word_count.get(word, 0 ) + 1
print(word_count)


books = {
    "book1": {"title": "1984", "author": "Gorge Orwell", "year": "1949"},
    "book2": {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960}
}
print(books["book1"]["title"])


text = "hello world"
char_count = {}
for char in text:
    if char != "":
        char_count[char] = char_count.get(char, 0) + 1
print(char_count)

# TODO Найдите количество книг, которое можно разместить на дискете

byte_in_megabyte = 1024*1024  # Количество байт в мегабайте
size_in_mb = 1.44             # Размер дискеты
size_symbol = 4               # Размер одного символа в байтах
count_symbols = 25
count_lines = 50
count_pages = 100

# Размер одной книги в мегабайтах
size_one_book = (count_symbols * size_symbol) * count_lines * count_pages / byte_in_megabyte

count_books = round(size_in_mb/size_one_book)
print("Количество книг, помещающихся на дискету:", count_books)

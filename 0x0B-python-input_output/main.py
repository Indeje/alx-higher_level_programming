#!/usr/bin/python3

# 0-main
""" read_file = __import__('0-read_file').read_file

read_file("my_file_0.txt") """


# 1-main
write_file = __import__('1-write_file').write_file

nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
print(nb_characters)


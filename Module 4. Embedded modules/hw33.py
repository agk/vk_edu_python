""" ДЗ1-1: Практическое задание 33
Написать функцию write_and_read, которая будет записывать в файл текст как параметр функции
и читать текст из этого файла и передавать на выход функции.

Дополните код ниже, дописав свой код в секции “YOUR CODE HERE”.

import os

text = input()

def write_and_read(text):
   # YOUR CODE HERE
"""
import os

text = input()

def write_and_read(text):
    filename_path = os.path.join(os.getcwd(), "filename")
    open(filename_path, "w").write(text)
    return open(filename_path, "r").read()

print(write_and_read(text))
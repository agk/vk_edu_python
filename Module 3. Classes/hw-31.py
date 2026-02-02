""" ДЗ8-1: Практическое задание 31
Перед вам класс ContextDictionary, в котором уже реализованы несколько методов:
__init__: в нем объявлен атрибут self.dictionary, который равен None
put(self, key, value), который кладет значение value по ключу key в self.dictionary,
когда этот атрибут является словарем, то есть в контексте with
get(self, key), который забирает значение по ключу key в self.dictionary,
когда этот атрибут является словарем, то есть в контексте with
Вам нужно дополнить его, реализовав магические методы контекста:
__enter__: здесь во время контекста наш атрибут self.dictionary превращается в словарь
__exit__: в нем атрибут self.dictionary вновь равен None
Таким образом мы хотим смоделировать поведение класса в контексте with.

Дополните код ниже, дописав свой код в секции “YOUR CODE HERE”.
class ContextDictionary:
   def __init__(self):
       self.dictionary = None

   def __enter__(self):
       # YOUR CODE HERE

   def __exit__(self, exc_type, exc_val, exc_tb):
       # YOUR CODE HERE

   def put(self, key, value):
       self.dictionary[key] = value

   def get(self, key):
       return self.dictionary[key]

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)
"""
class ContextDictionary:
    def __init__(self):
        self.dictionary = None

    def __enter__(self):
        self.dictionary = {}

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.dictionary = None

    def put(self, key, value):
        self.dictionary[key] = value

    def get(self, key):
        return self.dictionary[key]

code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
"""
ДЗ13-1: Проект в конце модуля - 24
Необходимо написать генераторную функцию solution, которая будет фильтровать данные из последовательности data
функцией func_filter, к полученным данным применять функцию func_map
и возвращать в качестве значения каждый второй элемент полученной последовательности.

Нужно пользоваться здесь концепцией генератора, то есть обрабатывать не все данные разом, а только те,
что необходимы для возвращения следующего значения.
Дополните также код своей реализацией кэшируещего декоратора из ДЗ 4:

def cache_deco(func):
   # YOUR CODE HERE

def solution(func_map, func_filter, data):
   # YOUR CODE HERE

code = []
while data := input():
  code.append(data)
code = "\n".join(code)
exec(code)
"""
def cache_deco(func):
    # Создаем словарь для хранения кэша
    cache = {}
    def wrapper(*args, **kwargs):
        if args in cache:
            return cache[args]

        result = func(*args, **kwargs)
        cache[args] = result
        return result

    return wrapper

def solution(func_map, func_filter, data):
    filtered_data = filter(func_filter, data)
    mapped_data = map(func_map, filtered_data)
    for i, data in enumerate(mapped_data):
        if i % 2 == 0:
            yield data

code = []
while data := input():
  code.append(data)
code = "\n".join(code)
exec(code)

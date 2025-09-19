"""
ДЗ7-1: Практическое задание 18
Напишите декоратор, который будет кэшировать вызовы функции, которая будет передана на вход.
То есть декоратор должен проверить нет ли в кэше (например, словаре) значения, и если нет,
то вычислить и запомнить результат, если есть, то взять это значение.
Дополните код ниже, дописав свой код в секции “YOUR CODE HERE”.

def cache_deco(func):
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

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)
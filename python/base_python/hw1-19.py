"""
ДЗ8-1: Практическое задание 19
Напишите декоратор, который будет принимать натуральное число n – число повторений –
и будет повторять вызов декорированной функции n раз, а также возвращать значение из последнего вызова.
Дополните код ниже, дописав свой код в секции “YOUR CODE HERE”.

def repeat_deco(n=1):
   # YOUR CODE HERE

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)
"""

def repeat_deco(n=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)

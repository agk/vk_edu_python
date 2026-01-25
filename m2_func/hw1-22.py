"""
ДЗ11-1: Практическое задание 22
Представьте, что у вас есть словарь с ключами и их частотами (то есть насколько часто встречался каждый ключ)
в качестве значений.
Напишите функцию make_most_common_keys, которая принимает словарь частот и выводит отсортированный
(например через функцию sorted) по убыванию частот (то есть значений ключей) список ключей.

Дополните код ниже, дописав свой код в секции “YOUR CODE HERE”.

from typing import List, Dict

def make_most_common_keys(d: Dict[int, int]) -> List[int]:
   # YOUR CODE HERE

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)
"""
from typing import List, Dict

def make_most_common_keys(d: Dict[int, int]) -> List[int]:
    # YOUR CODE HERE
    return sorted(d.keys(), key=lambda k: d[k], reverse=True)

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)
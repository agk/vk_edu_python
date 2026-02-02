"""
ДЗ12-1: Практическое задание 23
Написать функцию get_indexes которая принимает два списка и возвращает список индексов,
в которых элемент из первого списка меньше элемента из второго списка по данному индексу.

Желательно проходиться сразу по двум массивам одновременно (вспомните функцию zip).
Для нахождения индексов можно использовать enumerate вместе с zip.

Дополните код ниже, дописав свой код в секции “YOUR CODE HERE”.

from typing import List

def get_indexes(nums1: List[int], nums2: List[int]) -> List[int]:
   # YOUR CODE HERE

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)

nums1 = [2, 4, 3, 5, 0]
nums2 = [4, 3, 2, 1, 1]
print(get_indexes(nums1, nums2))
"""
from typing import List

def get_indexes(nums1: List[int], nums2: List[int]) -> List[int]:
    r = []
    for i, el in enumerate(zip(nums1, nums2)):
        if el[0] < el[1]:
            r.append(i)
    return r

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)

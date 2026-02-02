"""
ДЗ6-1: Практическое задание 17
В этом задании нужно будет написать свою реализацию filter()
(https://docs.python.org/3/library/functions.html#filter),
то есть генераторную функцию, которая принимает функцию и последовательность и фильтрует
последовательность в зависимости от вердикта переданной функции.
Воспользуйтесь своей реализацией, чтобы применить лямбда функцию, поданную на вход,
к поданной на вход последовательности.

Вам нужно написать свой код в секции “YOUR CODE HERE”, остальной код можно оставить как есть:

def filter(func, seq):
   # YOUR CODE HERE

func_in, seq_in = eval(input()), eval(input())

for x in filter(func_in, seq_in):
   print(x)

"""
def filter(func, seq):
    l_seq = list(seq)
    # print(l_seq)
    for x in l_seq:
        if func(x):
            yield x

func_in, seq_in = eval(input()), eval(input())

for x in filter(func_in, seq_in):
   print(x)

"""
ДЗ4-1: Практическое задание 27
Реализовать метод calculate_period с декоратором classmethod в классе “Pendulum”, в котором написаны два атрибута класса:
g =10
pi = 3.14
Этот метод должен вычислять период математического маятника по формуле:
T=2π√l/g
Дополните код ниже, дописав свой код в секции “YOUR CODE HERE”.
class Pendulum:
   g = 10
   pi = 3.14

   @classmethod
   def calculate_period(cls, length):
       # YOUR CODE HERE

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)
"""
import math

class Pendulum:
   g = 10
   pi = 3.14

   @classmethod
   def calculate_period(cls, length):
       return 2 * cls.pi * math.sqrt(length/cls.g)


code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)
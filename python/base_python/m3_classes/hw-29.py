""" ДЗ6-1: Практическое задание 29
У нас есть такой же класс Circle из предудущего задания,
но теперь появляется класс-примесь CalculateCircleLengthMixin.
Затем от двух классов наследуется класс CircleWithMixin,
реализуя таким образом множественное наследование.
В классе-примеси CalculateCircleLengthMixin реализуйте метод calculate_length,
который вычисляет длину окружности по формуле L=2πr,
чтобы использовать его в итоге в классе CircleWithMixin.
Желательно, чтобы это было сделано через super и проперти класса Circle.

Дополните код ниже, дописав свой код в секции “YOUR CODE HERE”.

class Circle:
   _pi = 3.14

   def __init__(self, radius):
       self._radius = radius

   @property
   def radius(self):
       return self._radius

   @property
   def pi(self):
       return self._pi

   def calculate_area(self):
       return self._pi * self._radius ** 2


class CalculateCircleLengthMixin:
   def calculate_length(self):
       # YOUR CODE HERE


class CircleWithMixin(CalculateCircleLengthMixin, Circle):
   pass

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)
"""
class Circle:
   _pi = 3.14

   def __init__(self, radius):
       self._radius = radius

   @property
   def radius(self):
       return self._radius

   @property
   def pi(self):
       return self._pi

   def calculate_area(self):
       return self._pi * self._radius ** 2

   def calculate_length(self):
       return 2 * self._pi * self._radius

class CalculateCircleLengthMixin:
   def calculate_length(self):
       return super().calculate_length()

class CircleWithMixin(Circle, CalculateCircleLengthMixin):
   pass

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)

import unittest

def factorial(n): 
    '''Возвращает факториал для заданного неотрицательного числа n
    
        Параметр: a (int) : число
    
        Возвращаемое значение: (int) : факториал n

        Пример вызова функции:
            factorial(5) -> 120'''
    if n == 0:
        return 1
    else: 
        return n * factorial(n - 1)

class FactorialTestCase (unittest.TestCase):
    def test_zero(self):
        res = factorial(0)
        self.assertEqual(res, 1)

    def test_one(self):
        res = factorial(1)
        self.assertEqual(res, 1)

    def test_three(self):
        res = factorial(3)
        self.assertEqual(res, 6)

    def test_three(self):
        res = factorial(5)
        self.assertEqual(res, 120)

    def test_thirty_two(self):
        res = factorial(32)
        self.assertEqual(res, 263130836933693530167218012160000000)
import unittest

def fibonacchi(iter):
    # Принимает неотрицательное количество итераций iter подсчёта чисел последовательности Фибоначчи и возвращает последнее полученное число
    a = 0
    b = 1
    for iter in range(iter):
        c = a + b
        a = b
        b = c
    return b

class FibonacchiTestCase (unittest.TestCase):
    def test_zero(self):
        res = fibonacchi(0)
        self.assertEqual(res, 1)

    def test_one(self):
        res = fibonacchi(1)
        self.assertEqual(res, 1)

    def test_three(self):
        res = fibonacchi(3)
        self.assertEqual(res, 3)

    def test_three(self):
        res = fibonacchi(14)
        self.assertEqual(res, 610)

    def test_thirty_two(self):
        res = fibonacchi(17)
        self.assertEqual(res, 2584)
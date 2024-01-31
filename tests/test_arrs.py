import unittest
# Импорт модуля, содержащего функции для тестирования
from utils import arrs


class Test_func(unittest.TestCase):
    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get([1, 2, 3], 1, None), 2)
        self.assertEqual(arrs.get([], 0, "test"), "test")
        self.assertEqual(arrs.get([1, 2, 3], 0, "test"), 1)
        self.assertEqual(arrs.get([1, 2, 3], 2, "test"), 3)
        self.assertEqual(arrs.get([1, 2, 3], -2, "test"), "test")
        self.assertEqual(arrs.get([1, 2, 3], 10, "test"), "test")
        self.assertEqual(arrs.get([], -2, "test"), "test")
        self.assertEqual(arrs.get([], 20, "test"), "test")
        self.assertEqual(arrs.get([], 20, None), None)
        self.assertEqual(arrs.get([], -2, None), None)

    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(arrs.my_slice([], ), [])
        self.assertEqual(arrs.my_slice([], 1), [])
        self.assertEqual(arrs.my_slice([], None), [])
        self.assertEqual(arrs.my_slice([], 1, 3), [])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 0, 10), [1, 2, 3, 4])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4]), [1, 2, 3, 4])


if __name__ == '__main__':
    test_obj = Test_func

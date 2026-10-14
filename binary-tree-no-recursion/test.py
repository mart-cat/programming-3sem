import unittest
from app import gen_bin_tree


class TestGenBinTree(unittest.TestCase):

    def test_height_zero(self) -> None:
        """При height=0 должно возвращаться значение корня"""
        tree = gen_bin_tree(0, 1)
        self.assertEqual(tree, [])

    def test_height_one(self) -> None:
        """При height=1 корень с двумя None-потомками"""
        tree = gen_bin_tree(1, 5)
        self.assertEqual(tree, [5])

    def test_height_three(self) -> None:
        """Проверка структуры дерева высоты 3"""
        tree = gen_bin_tree(3, 1)
        self.assertEqual(tree, [1, 2, 4, 5, 3, 6, 7])


if __name__ == "__main__":
    unittest.main(verbosity=2)
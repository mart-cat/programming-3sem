import unittest
from typing import Any

from app import gen_bin_tree


class TestGenBinTree(unittest.TestCase):
    """Тесты для проверки построения бинарного дерева."""

    def test_root_value(self) -> None:
        """Проверяет, что корень дерева содержит переданное значение."""
        tree= gen_bin_tree(4, 8)
        self.assertEqual(tree["value"], 8)

    def test_left_right(self) -> None:
        """Проверяет значения левого и правого потомков при height=1."""
        tree = gen_bin_tree(1, 8)
        self.assertEqual(tree["left"]["value"], 12)   # 8 + 8/2
        self.assertEqual(tree["right"]["value"], 64)  # 8 * 8

    def test_small(self) -> None:
        """Проверяет, что при height=0 возвращается лист без потомков."""
        tree= gen_bin_tree(0, 8)
        self.assertEqual(tree, {"left": None, "right": None, "value": 8})


if __name__ == "__main__":
    unittest.main(verbosity=2)
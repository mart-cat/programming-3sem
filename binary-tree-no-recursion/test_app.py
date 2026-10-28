"""Тесты для функции gen_bin_tree."""

import unittest

from app import gen_bin_tree


def depth(node: dict | None) -> int:
    """Глубина дерева в рёбрах: у листа (и у None) глубина 0."""
    if node is None or (node["left"] is None and node["right"] is None):
        return 0
    return 1 + max(depth(node["left"]), depth(node["right"]))


class TestGenBinTree(unittest.TestCase):
    """Проверки построения бинарного дерева."""

    def test_height_zero(self) -> None:
        """При height=0 возвращается только корневой лист."""
        tree = gen_bin_tree(0, 8)
        self.assertEqual(tree, {"value": 8, "left": None, "right": None})

    def test_height_one(self) -> None:
        """При height=1 у корня ровно два потомка с ожидаемыми значениями."""
        tree = gen_bin_tree(1, 8)
        self.assertEqual(tree["left"]["value"], 12)   # 8 + 8/2
        self.assertEqual(tree["right"]["value"], 64)  # 8 ** 2

    def test_height_two(self) -> None:
        """Значения на втором уровне вычисляются от значений первого."""
        tree = gen_bin_tree(2, 8)
        self.assertEqual(tree["left"]["left"]["value"], 18)    # 12 + 12/2
        self.assertEqual(tree["left"]["right"]["value"], 144)  # 12 ** 2
        self.assertEqual(tree["right"]["left"]["value"], 96)   # 64 + 64/2
        self.assertEqual(tree["right"]["right"]["value"], 4096)  # 64 ** 2

    def test_custom_leaves(self) -> None:
        """Собственные left_leaf и right_leaf применяются к потомкам."""
        tree = gen_bin_tree(
            1, 10,
            left_leaf=lambda x: x + 1,
            right_leaf=lambda x: x - 1,
        )
        self.assertEqual(tree["left"]["value"], 11)
        self.assertEqual(tree["right"]["value"], 9)

    def test_full_height(self) -> None:
        """Глубина построенного дерева равна параметру height."""
        for h in range(5):
            with self.subTest(height=h):
                self.assertEqual(depth(gen_bin_tree(h, 8)), h)

    def test_default_args(self) -> None:
        """Вызов без аргументов использует значения варианта 8."""
        tree = gen_bin_tree()
        self.assertEqual(tree["value"], 8)  # root по умолчанию
        self.assertEqual(depth(tree), 4)    # height по умолчанию

    def test_negative_height(self) -> None:
        """Отрицательная высота вызывает ValueError."""
        with self.assertRaises(ValueError):
            gen_bin_tree(-1, 8)


if __name__ == "__main__":
    unittest.main(verbosity=2)
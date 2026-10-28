import unittest

from app import gen_bin_tree


class TestGenBinTree(unittest.TestCase):
    """Тесты для проверки построения бинарного дерева."""

    def test_root_value(self) -> None:
        """Корень содержит переданное значение."""
        tree = gen_bin_tree(4, 8)
        self.assertEqual(tree["value"], 8)

    def test_left_right(self) -> None:
        """Значения левого и правого потомков при height=1."""
        tree = gen_bin_tree(1, 8)
        self.assertEqual(tree["left"]["value"], 12)   # 8 + 8/2
        self.assertEqual(tree["right"]["value"], 64)  # 8 * 8

    def test_small(self) -> None:
        """При height=0 возвращается лист без потомков."""
        tree = gen_bin_tree(0, 8)
        self.assertEqual(tree, {"left": None, "right": None, "value": 8})

    def test_custom_leaves(self) -> None:
        """Собственные функции left_leaf и right_leaf."""
        tree = gen_bin_tree(
            1, 10,
            left_leaf=lambda x: x + 1,
            right_leaf=lambda x: x - 1,
        )
        self.assertEqual(tree["left"]["value"], 11)
        self.assertEqual(tree["right"]["value"], 9)

    def test_full_height(self) -> None:
        """Высота всего дерева соответствует параметру height."""
        def depth(node: dict | None) -> int:
            if node is None or (node["left"] is None and node["right"] is None):
                return 0
            return 1 + max(depth(node["left"]), depth(node["right"]))

        for h in range(4):
            with self.subTest(height=h):
                self.assertEqual(depth(gen_bin_tree(h, 8)), h)

    def test_default_args(self) -> None:
        """Вызов без аргументов использует значения варианта 4."""
        def depth(node: dict | None) -> int:
            if node is None or (node["left"] is None and node["right"] is None):
                return 0
            return 1 + max(depth(node["left"]), depth(node["right"]))

        tree = gen_bin_tree()
        self.assertEqual(tree["value"], 8)   # root по умолчанию
        self.assertEqual(depth(tree), 4)     # height по умолчанию

    def test_negative_height(self) -> None:
        """Отрицательная высота вызывает ValueError"""
        with self.assertRaises(ValueError):
            gen_bin_tree(-1, 8)


if __name__ == "__main__":
    unittest.main(verbosity=2)
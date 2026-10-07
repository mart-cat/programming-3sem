"""Генерация бинарного дерева."""

from typing import Callable


def gen_bin_tree(
    height: int,
    root: float,
    left_leaf: Callable[[float], float] = lambda r: r + r / 2,
    right_leaf: Callable[[float], float] = lambda r: r * r,
) -> dict:
    """Рекурсивно строит бинарное дерево высоты height.

    Каждый узел — словарь {"value", "left", "right"}.
    Лист (height == 0) имеет left = right = None.
    """
    if height == 0:
        return {"value": root, "left": None, "right": None}
    return {
        "value": root,
        "left": gen_bin_tree(height - 1, left_leaf(root), left_leaf, right_leaf),
        "right": gen_bin_tree(height - 1, right_leaf(root), left_leaf, right_leaf),
    }


if __name__ == "__main__":
    print(gen_bin_tree(4, 8))
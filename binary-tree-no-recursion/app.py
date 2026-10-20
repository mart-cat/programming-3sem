"""Построение бинарного дерева без рекурсии"""

from collections import deque
from typing import Callable, TypeAlias

TreeNode: TypeAlias = dict[str, object]


def gen_bin_tree(
    height: int = 4,
    root: int | float = 8,
    left_leaf: Callable[[int | float], int | float] = lambda x: x + x / 2,
    right_leaf: Callable[[int | float], int | float] = lambda x: x ** 2,
) -> TreeNode:
    """Создать полное бинарное дерево заданной высоты без рекурсии.

    Высота означает число рёбер от корня до самого глубокого листа.
    При высоте 0 дерево состоит из единственного корневого узла.
    """
    if not isinstance(height, int) or isinstance(height, bool):
        raise TypeError("height должна быть целым числом")
    if height < 0:
        raise ValueError("height не может быть отрицательной")

    tree: TreeNode = {"value": root, "left": None, "right": None}
    queue = deque([(tree, 0)])

    while queue:
        node, level = queue.popleft()
        if level == height:
            continue

        value = node["value"]
        left: TreeNode = {"value": left_leaf(value), "left": None, "right": None}
        right: TreeNode = {"value": right_leaf(value), "left": None, "right": None}
        node["left"] = left
        node["right"] = right

        queue.append((left, level + 1))
        queue.append((right, level + 1))

    return tree


if __name__ == "__main__":
    from pprint import pprint

    pprint(gen_bin_tree(height=2), sort_dicts=False)

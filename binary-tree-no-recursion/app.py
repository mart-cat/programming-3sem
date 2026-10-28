"""Построение полного бинарного дерева без рекурсии.

Вариант 8: значения по умолчанию для параметров:
    height = 4, root = 8.

Реализация использует обход в ширину (BFS) с помощью collections.deque,
поэтому глубокая рекурсия не требуется — дерево строится итеративно.
"""

from collections import deque
from typing import Callable, TypeAlias

Number: TypeAlias = int | float
LeafFunc: TypeAlias = Callable[[Number], Number]
TreeNode: TypeAlias = dict[str, object]


def gen_bin_tree(
    height: int = 4,
    root: Number = 8,
    left_leaf: LeafFunc = lambda x: x + x / 2,
    right_leaf: LeafFunc = lambda x: x ** 2,
) -> TreeNode:
    """Итеративно строит полное бинарное дерево заданной высоты.

    Параметры:
        height: высота дерева — число рёбер от корня до самого глубокого
            листа. При height == 0 дерево состоит из единственного
            корневого узла. Значение по умолчанию — 4 (вариант 4).
        root: значение корневого узла. Значение по умолчанию — 8 (вариант 4).
        left_leaf: функция вычисления значения левого потомка из значения
            родителя. По умолчанию r + r/2.
        right_leaf: функция вычисления значения правого потомка из значения
            родителя. По умолчанию r ** 2.

    Возвращает:
        Словарь вида {"value": ..., "left": ..., "right": ...}.
        У листьев (узлов на уровне height) поля left и right равны None.
    """
    if not isinstance(height, int) or isinstance(height, bool):
        raise TypeError("height должна быть целым числом")
    if height < 0:
        raise ValueError("height не может быть отрицательной")

    tree: TreeNode = {"value": root, "left": None, "right": None}
    queue: deque[tuple[TreeNode, int]] = deque([(tree, 0)])

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
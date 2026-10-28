"""Генерация бинарного дерева.
"""

from typing import Callable


def gen_bin_tree(
    height: int = 4,
    root: float = 8,
    left_leaf: Callable[[float], float] = lambda r: r + r / 2,
    right_leaf: Callable[[float], float] = lambda r: r * r,
) -> dict:
    """Рекурсивно строит бинарное дерево заданной высоты.

    Параметры:
        height: высота дерева (неотрицательное). height == 0 —
            возвращается только корневой лист. Значение по умолчанию — 4
        root: значение корневого узла. Значение по умолчанию — 8
        left_leaf: функция вычисления значения левого из значения
            родителя. По умолчанию r + r/2.
        right_leaf: функция вычисления значения правого из значения
            родителя. По умолчанию r * r.

    Возвращает:
        Словарь вида {"value": ..., "left": ..., "right": ...}.
        У листа (height == 0) поля left и right равны None.

    Исключения:
        ValueError: если height < 0.
    """
    if height < 0:
        raise ValueError(f"height должно быть >= 0, получено {height}")
    if height == 0:
        return {"value": root, "left": None, "right": None}
    return {
        "value": root,
        "left": gen_bin_tree(height - 1, left_leaf(root), left_leaf, right_leaf),
        "right": gen_bin_tree(height - 1, right_leaf(root), left_leaf, right_leaf),
    }


if __name__ == "__main__":
    print(gen_bin_tree(4, 8))
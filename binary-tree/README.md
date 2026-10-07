# Бинарное дерево (Binary Tree)

Решение задачи «Бинарное дерево» на Python.

## Условие

Даны параметры `height`, `root`, `left_leaf` и `right_leaf`.
Нужно описать рекурсивную функцию `gen_bin_tree`, которая строит бинарное дерево.
Базовый вариант решения представляет результат в виде словаря с ключами `value`, `left`, `right`.

## Примеры

При `gen_bin_tree(1, 8)`:

```python
{
  "value": 8,
  "left":  {"value": 12.0, "left": None, "right": None},  # 8 + 8/2
  "right": {"value": 64,   "left": None, "right": None}   # 8 * 8
}
```

При `gen_bin_tree(0, 8)` — один лист без потомков:

```python
{"value": 8, "left": None, "right": None}
```

При gen_bin_tree(4, 8) строится дерево глубины 4 с 31 узлом.

## Решение

Файл app.py содержит функцию gen_bin_tree(height, root, left_leaf, right_leaf).

Пока height > 0, создаём узел со значением root и двумя поддеревьями высоты height - 1. Значения потомков вычисляются лямбдами left_leaf и right_leaf. При height = 0 возвращается лист.

## Запуск тестов

python -m unittest test.py -v

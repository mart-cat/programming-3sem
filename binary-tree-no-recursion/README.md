# Бинарное дерево (Binary Tree)

Решение задачи «Бинарное дерево» на Python без рекурсии.

## Условие

Создать функцию `gen_bin_tree`, которая строит бинарное дерево в виде словаря с ключами `value`, `left`, `right`.

Вариант 8:
- `root = 8`
- `height = 4`
- `left_leaf = lambda x: x + x / 2`
- `right_leaf = lambda x: x ** 2`

## Пример

При `gen_bin_tree(1, 8)`:

```python
{
    'value': 8,
    'left': {'value': 12.0, 'left': None, 'right': None},
    'right': {'value': 64, 'left': None, 'right': None}
}
```

При `height=0` дерево состоит только из корня.

## Решение

Функция находится в `app.py`. Дерево строится в цикле `while` с помощью очереди `deque`. Значения потомков вычисляются lambda-функциями. Рекурсия не используется.

Дерево хранится в `dict`. Для хранения дерева также можно использовать `list`, `tuple` и `collections.namedtuple`.

## Запуск тестов

```bash
python -m unittest test.py -v
```

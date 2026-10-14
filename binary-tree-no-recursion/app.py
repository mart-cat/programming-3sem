"""Генерация бинарного дерева без рекурсии"""

from typing import Callable


def gen_bin_tree(height,root):
    
    """
    Просчет кол-во узлов в полном дереве
    """
    n = 2** height-1 
    tree = [root + i for i in range(n)]
    box=[0]
    result=[]

    while box:
        i = box.pop()
        if i>= len(tree):
            continue
        result.append(tree[i])
        box.append(2*i+2)
        box.append(2*i+1)
    return result


if __name__ == "__main__":
    print(gen_bin_tree(3,1))
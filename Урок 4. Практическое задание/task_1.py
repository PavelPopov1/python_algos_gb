"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""

from timeit import timeit


lst = [1, 2, 3, 4, 5, 6, 7]


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i in range(len(nums)) if not nums[i] % 2]


print(func_1(lst))
print(func_2(lst))

print('func1: ', timeit(stmt='func_1(lst)', setup='from __main__ import func_1, lst', number=10000000))
print('func2: ', timeit(stmt='func_2(lst)', setup='from __main__ import func_2, lst', number=10000000))

"""
Результаты замеров:
func1:  25.046432023
func2:  19.425661488000003

Аналитика: Удалось с помощью использования генератора оптимизировать решение, теперь оно выполняется быстрее, хоть 
и не на много. Оно более оптимально, так как генератор - втроенный в интерпретатор питона механизм, 
который оптимизирован и работает быстрее, чем написанные вручную аналоги
"""
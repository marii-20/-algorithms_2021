"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым!
"""

from timeit import timeit
from collections import Counter

array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


t1 = timeit('func_1', 'from __main__ import func_1')
print(f'Результат замера func_1: {t1} мс.')


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


t2 = timeit('func_2', 'from __main__ import func_2')
print(f'Результат замера func_2: {t2} мс.')


def func_3():
    num = max(array, key=array.count)
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {array.count(num)} раз(а)'


t3 = timeit('func_3', 'from __main__ import func_3')
print(f'Результат замера func_1: {t3} мс.')

print(func_1())
print(func_2())
print(func_3())

# Согласно замерам, func_1 и func_3 работают примерно одинаково, но в первой функции использованы счетчики,
# что убыстряет процесс работы.

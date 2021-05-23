"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Не забудьте указать сложность каждого из двух алгоритмов. Для лучшего закрепления темы
можете определить и указать сложность еще и у каждого выражения этих двух алгоритмов.

Примечание:
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""

# Алгоритм №1

def min_list(lst):
    for i in lst:
        min_num = True
            for n in lst:
                if i > n:
                    min_num = False
            if min_num:
                return i
 # Сложность O(n^2)



# Алгоритм №2

def min_list(lst):
    min_num = lst[0]
    for i in lst:
        if i < min_num:
            min_num = i
    return min_num

# Сложность O(n)

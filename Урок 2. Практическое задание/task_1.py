"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.

Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.

Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ

Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""



def calculator():
    operation = input('Введите операцию (+, -, *, / или 0 для выхода): ')

    if operation == '0':
        return 'выход'
    else:
        if operation in '+-/*':
            try:
                a = int(input('Введите первое число: '))
                b = int(input('Введите второе число: '))

                if operation == '/':
                    try:
                        print(f'Ваш результат: {a/b}')
                        return calculator()
                    except ZeroDivisionError:
                        print('Ошибка! Делить на ноль нельзя!')

                elif operation == '*':
                    print(f'Ваш результат: {a*b}')
                    return calculator()

                elif operation == '+':
                    print(f'Ваш результат: {a+b}')
                    return calculator()

                elif operation == '-':
                    print(f'Ваш результат: {a-b}')
                    return calculator()

            except ValueError:
                print('Неправильный формат данных. Попробуйте ввести число.')
                return calculator()

        else:
            print('Неправильный формат данных. Попробуйте ввести символ.')
            return calculator()

calculator()



"""
Задача 4 (сложно) "Первый после точки":
Напишите в начале программы однострочный комментарий: "4th program".
Дана строка '123.456'.
Вывести на экран первую цифру после запятой - 4.
Начало алгоритма решения:
Преобразуйте в строку в дробное число. ('123.456' -> 123.456)
Умножьте на 10, чтобы сместить 4 в целую часть. (1234.56)
Следующие шаги алгоритма составьте самостоятельно. В них вам понадобится команда int() и остаточное деление на 10.
"""

###    РЕШЕНИЕ:

# "4th program"

text = '123.456'  # Дана строка '123.456'

number = float('123.456') # Преобразуйте строку в дробное число. ('123.456' -> 123.456)
# print(type(number)) # <class 'float'>

intermediate_number = number * 10 # Умножьте на 10, чтобы сместить 4 в целую часть. (1234.56)

# print(intermediate_number) # 1234.56

digit_1 = int(intermediate_number) % 10

print('Первая цифра после запятой =', digit_1) # Вывести на экран первую цифру после запятой - 4

# возможный упрощенный вариант решения по данному условию задачи
print(int(text[4])) # Вывести на экран первую цифру после запятой - индекс 4-го элемента в заданой строке

# решение преподавателя, показывают после проверки преподавателя

print(int(float('123.456') * 10) % 10)



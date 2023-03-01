# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа,
#                      которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества.
# m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

# 1. Ввод данных.
# 2. Пересечение наборов
# 3. Упорядочивание элементов и вывод множеств на экран


def sorts_by_selection(some_list):
    list_x = some_list.copy()
    i = 0
    while i < len(list_x):
        j = i+1
        while j < (len(list_x)):
            if list_x[i] > list_x[j]:
                list_x[j], list_x[i] = list_x[i], list_x[j]
            j += 1
        i += 1
    return list_x


# 1
n = int(input("Введите кол-во элементов множества 'n': "))
m = int(input("Введите кол-во элементов множества 'm': "))

list_n = []
list_m = []

for i in range(n):
    list_n.append(int(input("Введите элемент для множества 'n':")))

for i in range(m):
    list_m.append(int(input("Введите элемент для множества 'm':")))


# 2
set_mn = set(list_n).intersection(set(list_m))

# 3
list_mn = sorts_by_selection(list(set_mn))
print(list_mn)

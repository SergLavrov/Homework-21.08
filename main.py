
# Задача. В одномерном массиве, состоящем из "n" вещественных элементов вычислить:
#
# 1) Номер минимального элемента массива

import random
lenList = int(input('Введите количество элементов : '))

someList = [''] * lenList

for index in range(lenList):
    someList[index] = random.randint(-100, 100)

print(someList)

minNumber = min(someList)
numberMin = someList.index(minNumber) + 1

print(f'Min element: {minNumber}')
print(f'Number of min element: {numberMin}')


# 1) Сумму элементов массива, расположенных между
# первым и вторым отрицательными элементами

import random
lenList = int(input('Введите количество элементов : '))

someList = [''] * lenList

for index in range(lenList):
    someList[index] = random.randint(-25, 25)
    # someList[index] = int(input('Enter number: '))

print(someList)

cnt = 0
i = 0
ind1 = 0

while i < len(someList): # находим индекс первого отрицат. эл-та
    if someList[i] < 0:
        ind1 = i
        cnt += 1
        if cnt > 0:
            break
    i += 1
# print(ind1)

summ = 0
for item in someList[ind1 + 1:]:
    if item < 0:
        break
    summ += item

print('Summa =', summ)


# 3) Преобразовать массив таким образом, чтобы сначала располагались все элементы,
#    модуль которых не превышает 1, а потом все остальные.

import random
lenList = int(input('Введите количество элементов : '))

someList = [''] * lenList

for index in range(lenList):
    someList[index] = random.randint(-10, 10)

print(someList)

# list11 = [1, 5, -5, 10, -58, 1]
list = []

for item in someList:
    if abs(item) <= 1:
        list.insert(0, abs(item))
    if abs(item) > 1:
        list.append(abs(item))
print(list)

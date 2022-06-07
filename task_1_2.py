# Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X)
list1 = []
for x in range(1, 1001, 2): # берем нечетный
    list1.append(x ** 3)
print (list1)

# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7
len_list1 = len(list1)
print (len_list1)
total_sum = 0
for x in range(len_list1):
    sum_num = 0
    for i in str(list1[x]):
        sum_num += int(i)
    if sum_num % 7 == 0:
        total_sum += list1[x]
print(total_sum)

# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка
len_list1 = len(list1)
total_sum = 0
for x in range(len_list1):
    sum_num = 0
    for i in str(list1[x] + 17):
        sum_num += int(i)
    if sum_num % 7 == 0:
        total_sum += list1[x] + 17
print(total_sum)
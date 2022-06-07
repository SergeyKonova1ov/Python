# Реализовать склонение слова «процент» во фразе «N процентов»
list1 = [11, 12, 13, 14]
list2 = [0, 5, 6, 7, 8, 9]
list3 = [2, 3, 4]

for x in range(0, 101):

    if x in list1:
        print(str(x) + " процентов")
    elif x % 10 in list2:
        print(str(x) + " процентов")
    elif x % 10 in list3:
        print(str(x) + " процента")
    else:
        print(str(x) + " процент")


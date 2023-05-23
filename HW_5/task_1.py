# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он
# их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть,
# если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов,
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и
# “Пам парам”, если с ритмом все не в порядке
#
# *Пример:*
#
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
#     **Вывод:** Парам пам-пам

# Решение простым для меня способом

# data = input('Введите строку: ')
# data = data.split()
# d = dict()
# for word in data:
#     count = 0
#     for char in word:
#         if char == 'а' or char == 'о' or char == 'е' or char == 'у' or char == 'ю' or char == 'я' or char == 'и':
#             count = count + 1
#
#     d[word] = count
# if len(set(d.values())) == 1:
#     print("Парам пам-пам")
# else:
#     print("Пам парам")


# Попробовала с функцией

# def Song_of_Winnie(data):
#     data = data.split()
#     d = dict()
#     for word in data:
#         count = 0
#         for char in word:
#             if char == 'а' or char == 'о' or char == 'е' or char == 'у' or char == 'ю' or char == 'я' or char == 'и':
#                 count = count + 1
#         d[word] = count
#     if len(set(d.values())) == 1:
#         print("Парам пам-пам")
#     else:
#         print("Пам парам")
#
#
# Song_of_Winnie("Парам пам парам пам")

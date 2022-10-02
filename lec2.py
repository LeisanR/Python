# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# #data.writelines(colors)
# data.write('\nLINE 2\n')
# data.write('LINE 3\n') #\n переход 
# data.close()



#exit()  #после этой функции запись ниже работать не будет

# with open('file.txt', 'w') as data:
#     data.write('\nLINE 2\n')
#     data.write('LINE 3\n')


# path = 'file.txt'  #создаем путь к папке
# data = open('file.txt', 'r')  #откроем в режиме чтения r
# for line in data:   #при помощи цикла пробежимся по файлу
#     print(line)   #считаем все строки
# data.close()  #после того как закончили чтение, разорвем связь с файловой переменной и с файлом на диске


# import lec1 as l  # as l это сокращение при дальнешем использовании слова lec1
# print(l.f(1))



# def new_string(symbol, count=3):
#     return(symbol*count)
# print(new_string('4'))
# print(new_string(4))

#возможность передать неограниченное количество аргументов (для этого перед аргументом ставить *)
# def new(*string):
#     #res: str = '' 
#     res: int = 0 
#     for item in string:
#         res+=item  #склеивание строк
#     return res
# #print(new('a', 'b', 'c'))
# print(new(1, 2, 3))


#рекурсия - ф-ия вызывающая сама себя
# def fib(n):  #написали функцию, указали название и аргумент
#     if n in [1,2]:  #прописали логику выхода
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# print(fib(10))


#не работает
# list = []
# for e in range(1, 10):
#      list.append(list(e))
# print(e) # 1 1 2 3 5 8 13 21 34


#кортежи- некий неизменяемый список
#a = (3, 4, 6, 9)
# print(a[0])
# print(a[-2])

# for item in a:
#     print(item)

#словари неупорядоченные коллекции произвольных объектов с доступом по ключу
# dictionary = {}
# dictionary = \
#     {
#     'up': '↑',
#     'left': '←',
#     'down': '↓',
#     'right': '→'
#     }
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) # ←
# # типы ключей могут отличаться


# print(dictionary['up']) # ↑
# # типы ключей могут отличаться
# dictionary['left'] = '⇐'
# print(dictionary['left']) # ⇐
# #print(dictionary['type']) # KeyError: 'type'
# del dictionary['left'] # удаление элемента
# for item in dictionary: # for (k,v) in dictionary.items():
#  print('{}: {}'.format(item, dictionary[item]))
# # up: ↑
# # down: ↓
# # right: 



# #множества неупорядоченная совокупность элементов
# a = {1, 2, 3, 5, 8}
# b = {'2', '5', 8, 13, 21}
# print(type(a)) # set
# print(type(b)) # set


# a = {1, 2, 3, 5, 8}
# b = set([2, 5, 8, 13, 21])
# c = set((2, 5, 8, 13, 21))
# print(type(a)) # set
# print(type(b)) # set
# print(type(c)) # set
# a = {1, 1, 1, 1, 1}
# print(a) # {1}


# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red')
# print(colors) # {'green', 'blue','gray'}
# # colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok
# print(colors) # {'green', 'blue','gray'}
# colors.clear() # { }
# print(colors) # set()



# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}   объединение множеств
# i = a.intersection(b) # i = {8, 2, 5}
# dl = a.difference(b) # dl = {1, 3}
# dr = b.difference(a) # dr = {13, 21}
# q = a \
#  .union(b) \
#  .difference(a.intersection(b))
# # {1, 21, 3, 13}


# #Неизменяемое множество
# a = {1, 2, 3, 5, 8}
# b = frozenset(a)
# print(b) # frozenset({1, 2, 3, 5, 8})



# #Удаление множества
# list = [1,2,3,4,5]
# print(list.pop(3))
# print(list)


# #поставить на нужную позицию
# list = [1,2,3,4,5]
# print(list.insert(4, 3))
# print(list)


# #добавление в конец
# list = [1,2,3,4,5]
# print(list.append(100))
# print(list)

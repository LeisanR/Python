#print ('Hello world')
# типы данных и переменная
# int, float, boolean, str, list, None
value = None
print(type(value))
a = 123
b = 1.23
print(type(a))
print(type(b))
value = 1234
print(type(value))
s = 'Hello world'
print(s) #вывод строки
s = 'Hello \'world'
print(s) #вывод строки
s = 'Hello \nworld'
print(s) #вывод строки

print(a, b, s) #интерполяция
print(a, '-' ,b, '-' , s) #интерполяция
print('{1} - {2} - {0}' .format(a, b, s)) #интерполяция
print(f'{a} - {b} - {s}') #интерполяция
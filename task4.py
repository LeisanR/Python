#Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
print('номер четверти плоскости= ')
n=int(input())
if n==1:
    print('диапазон возможных координат точек в этой четверти: (x>0 и y>0)')
elif n==2:
    print('диапазон возможных координат точек в этой четверти: (x>0 и y<0)')
elif n==3:
    print('диапазон возможных координат точек в этой четверти: (x<0 и y<0)')
elif n==4:
    print('диапазон возможных координат точек в этой четверти: (x<0 и y>0)')
else:
    print('в диапазоне только 4 четверти')
#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# n = int(input('Введите число N: '))
# res = 1
# for i in range(1, n+1):
#     res *= i
#     print(res, end=', ')

# def F(input):
#     f=1
#     for i in range(2, input+1):
#         f*=i
#     return f
# print([F(i) for i in range(1, int(input('N = '))+1)])


def fib(N):
    if N==1:
        return N
    return N*fib(N-1)

#print(fib(5))

N=int(input('N: '))
lst=[]
for i in range(1, N+1):
    lst.append(fib(i))
print(lst)


# def fib(N):
# last = 1
# for i in range(1, N + 1): # 1 * 2 * 3 * 4
# last *= i
# yield last


# N = int(input('N: '))
# lst = list(fib(N))

# print(lst)
# print(lst)
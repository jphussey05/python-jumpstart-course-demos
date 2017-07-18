# def factorial(n):
#     if n == 1:
#         return 1
#
#     return n * factorial(n - 1)
#
#
# print("5!={:,} 3!={:,} 11!={:,} 25!={:,}".format(
#     factorial(5),  # 120
#     factorial(3),  # 6
#     factorial(11),  # 39916800
#     factorial(25)  # 15511210043330985984000000
# ))


# def fib():
#     nums = []
#
#     current=0
#     next = 1
#
#     while True:
#         current, next = next, next + current
#         nums.append(current)
#
#     return nums
#
# print('via lists')
# for n in fib():
#     print(n, end=', ')

#
from time import sleep


def fib_co():

    current=0
    next = 1

    while True:
        current, next = next, next + current
        yield current

print('\nvia yield')
for n in fib_co():
    # if n > 1000:
    #     break

    print(n)
    sleep(.5)
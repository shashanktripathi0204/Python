def add(*args):
    sums = 0
    for i in args:
        sums += i
    return sums


print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
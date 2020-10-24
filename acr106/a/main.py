import math


def ans():
    N = int(input())

    A = 1
    B = 1
    while True:
        five = N - pow(3, A)
        if (five <= 0):
            print('-1')
            return
        B = 1
        while (N >= (pow(3, A) + pow(5, B) - 10)):
            if (N == int(pow(3, A) + pow(5, B))):
                print("{0:d} {1:d}".format(A, B))
                return
            B += 1
        A += 1


ans()

from math import gcd
from fractions import Fraction # для представления чисел в виде дроби

def all_rationals():
    yield Fraction(0, 1)  # начинаем с 0 
    n = 1
    while True:
        for i in range(1, n + 1):  
            if gcd(i, n) == 1:    #  gcd находит наибольший общий делитель чисел, если он равен 1, то дробь несократимая (чтобы избежать повторы)
                yield Fraction(i, n)   # положительная дробь
                yield Fraction(-i, n)  # отрицательная дробь
        n += 1


gen = all_rationals()

for _ in range(50):
    print(next(gen))

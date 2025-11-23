from math import gcd
from fractions import Fraction


def all_rationals():
    yield Fraction(0, 1)  # начинаем с 0

    n = 1
    while True:
        # Только несократимые дроби с знаменателем = n
        for p in range(-n, n + 1):
            if gcd(abs(p), n) == 1 or p == 0:  # только несократимые дроби
                yield Fraction(p, n)

        # Только несократимые дроби с числителем = n
        for q in range(1, n):
            if gcd(n, q) == 1:  # только несократимые дроби
                yield Fraction(n, q)
                yield Fraction(-n, q)

        n += 1


gen = all_rationals()
for _ in range(50):
    print(next(gen))

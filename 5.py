from fractions import Fraction
from math import gcd


def rationals():
    """
    Используется диагональный обход по возрастанию s = |p| + q,
    где q > 0, p — целое, и дробь p/q несократима.
    Ноль представлен только как 0/1.
    """
    s = 1  # s = |p| + q, минимальная сумма для допустимой дроби (0/1 → s = 0+1 = 1)
    while True:
        # q — знаменатель, от 1 до s (т.к. |p| = s - q ≥ 0 ⇒ q ≤ s)
        for q in range(1, s + 1):
            p_abs = s - q  # |p|
            if p_abs == 0:
                # Только 0/1 разрешён
                if q == 1:
                    yield Fraction(0, 1)
                # при q > 1 — 0/q игнорируем (дубль нуля)
            else:
                # Рассматриваем +p и -p
                for p in (p_abs, -p_abs):
                    if gcd(p_abs, q) == 1:  # несократимая дробь
                        yield Fraction(p, q)
        s += 1

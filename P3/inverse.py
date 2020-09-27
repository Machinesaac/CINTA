def egcd(a, m):
    l1, r1 = 1, 0
    l2, r2 = 0, 1
    if a < m:
        a, m = m, a
    while m != 0:
        q = a // m
        s = a % m
        l1, r1, l2, r2 = l2, r2, l1 - q * l2, r1 - q * r2
        a, m = m, s

    return l1, r1


def inverse(a, m):
    _, inv = egcd(a, m)

    return inv if inv > 0 else m + inv


print(inverse(4, 7))

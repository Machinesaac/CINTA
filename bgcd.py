def bgcd(a, b):
    k = 0
    while ((a | b) & 1) == 0:
        a >>= 1
        b >>= 1
        k += 1

    while b & 1 == 0:
        b >>= 1
    while a:
        while a & 1 == 0:
            a >>= 1
        if a < b:
            a, b = b, a
        a -= b

    return b << k

print(bgcd(40,8))
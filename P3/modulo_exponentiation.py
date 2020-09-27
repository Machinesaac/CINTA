def mexp1(x, y, m):
    print(y)
    if y == 0:
        return 1
    if y & 1 == 1:
        return (x * (int(pow(mexp1(x, (y - 1) // 2, m) % m, 2)) % m)) % m
    else:
        return int(pow(mexp1(x, y // 2, m) % m, 2)) % m


def mexp2(x, y, m):
    sum = 1
    while y:
        if y & 1:
            sum = (sum * x) % m
        y = y // 2
        x *= x
    return sum



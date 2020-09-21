def ebgcd(a, b):
    m = [1, 0, 0, 1]

    def msub(x, y):
        if y == 0:
            return m[0], m[1]
        d = x // y
        m[0], m[2] = m[2], m[0] - d * m[2]
        m[1], m[3] = m[3], m[1] - d * m[3]
        x, y = y, x % y

        return msub(x, y)

    return msub(a, b)


print(ebgcd(13, 9))

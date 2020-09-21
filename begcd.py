def begcd(u, v):
    def msub(x, y):
        if x == 0:
            return m[2], m[3]
        while x & 1 == 0:
            x >>= 1
            if (m[0] | m[1]) & 1 == 0:
                m[0] >>= 1
                m[1] >>= 1
            else:
                m[0] = (m[0] + b) >> 1
                m[1] = (m[1] - a) >> 1
        while y & 1 == 0:
            y >>= 1
            if (m[2] | m[3]) & 1 == 0:
                m[2] >>= 1
                m[3] >>= 1
            else:
                m[2] = (m[2] + b) >> 1
                m[3] = (m[3] - a) >> 1

        if x >= y:
            x = x - y
            m[0] = m[0] - m[2]
            m[1] = m[1] - m[3]
        else:
            y = y - x
            m[2] = m[2] - m[0]
            m[3] = m[3] - m[1]

        return msub(x, y)
    a = u
    b = v
    m = [1, 0, 0, 1]
    while (a | b) & 1 == 0:
        a >>= 1
        b >>= 1

    return msub(a, b)


print(begcd(15, 7))

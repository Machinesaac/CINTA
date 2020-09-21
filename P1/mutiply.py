def multiply(a, b):
    i = 0
    my_sum = 0
    while b != 0:
        bit = b & 1
        if bit:
            a <<= 1
            my_sum += a
        b >>= 1
    return my_sum


print(multiply(5, 6))

def multiply(a, b):
    i = 0
    my_sum = 0
    while b != 0:
        bit = b & 1
        if bit:
            my_sum += a << i
        i += 1
        b >>= 1
    return my_sum

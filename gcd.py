def gcd(a, b):
    # return a if b == 0 else gcd(b, a % b)
    while b:
        a, b = b, a % b
    return a


print(gcd(15, 7))

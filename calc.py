

def is_prime(p):
    """
    determine if 2**p - 1 is prime
    """
    if p == 2:
        return True

    s = 4
    m = 2**p - 1
    for i in xrange(p - 2):
        s = ((s * s) - 2) % m
        print s

    return s == 0


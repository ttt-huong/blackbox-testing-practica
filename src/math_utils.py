import math

def gcd(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int) or isinstance(a, bool) or isinstance(b, bool):
        raise TypeError("Inputs must be integers")
    if a == 0 and b == 0:
        raise ValueError("GCD of 0 and 0 is undefined")
    return math.gcd(a, b)

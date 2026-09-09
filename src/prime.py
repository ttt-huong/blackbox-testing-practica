def is_prime(n) -> bool:
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("Input must be an integer")
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

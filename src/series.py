import math

def calculate_alternating_sum(n: int) -> int:
    if n < 1:
        raise ValueError("n must be a positive integer")
    return sum((-1) ** (i - 1) * i for i in range(1, n + 1))

def sum_of_factorials(n: int) -> int:
    if n < 1:
        raise ValueError("n must be a positive integer")
    return sum(math.factorial(i) for i in range(1, n + 1))

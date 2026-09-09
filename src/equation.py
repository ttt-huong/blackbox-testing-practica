import math

def solve_quadratic_equation(a, b, c):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))) or isinstance(a, bool) or isinstance(b, bool) or isinstance(c, bool):
        raise TypeError("Coefficients must be numbers")
    
    if a == 0:
        if b == 0:
            if c == 0:
                return "INFINITE_SOLUTIONS"
            else:
                return "NO_SOLUTION"
        else:
            return (-c / b,)
    
    delta = b ** 2 - 4 * a * c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return (x1, x2)
    elif delta == 0:
        x = -b / (2 * a)
        return (x,)
    else:
        return "NO_SOLUTION"

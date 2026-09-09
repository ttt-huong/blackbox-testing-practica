def calculate_rectangle_perimeter(length, width):
    if not (isinstance(length, (int, float)) and isinstance(width, (int, float))) or isinstance(length, bool) or isinstance(width, bool):
        raise TypeError("Length and width must be numbers")
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers")
    return 2 * (length + width)

def calculate_rectangle_area(length, width):
    if not (isinstance(length, (int, float)) and isinstance(width, (int, float))) or isinstance(length, bool) or isinstance(width, bool):
        raise TypeError("Length and width must be numbers")
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers")
    return length * width

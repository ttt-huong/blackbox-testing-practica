import pytest
from src.geometry import calculate_rectangle_perimeter, calculate_rectangle_area
from src.equation import solve_quadratic_equation
from src.calendar_utils import get_days_in_month
from src.prime import is_prime
from src.series import calculate_alternating_sum, sum_of_factorials
from src.math_utils import gcd

# --- Bài 1: Tính chu vi hình chữ nhật (Dữ liệu hợp lệ) ---
def test_rectangle_perimeter_valid():
    assert calculate_rectangle_perimeter(5, 3) == 16
    assert calculate_rectangle_perimeter(4.5, 2.5) == 14.0

# --- Bài 2: Tính diện tích hình chữ nhật (Dữ liệu hợp lệ) ---
def test_rectangle_area_valid():
    assert calculate_rectangle_area(6, 4) == 24
    assert calculate_rectangle_area(3.5, 2.0) == 7.0

# --- Bài 3: Giải phương trình bậc 2 (Dữ liệu hợp lệ) ---
def test_quadratic_equation_valid():
    # Trường hợp 2 nghiệm phân biệt (Delta > 0)
    assert solve_quadratic_equation(1, -3, 2) == (2.0, 1.0)
    # Trường hợp nghiệm kép (Delta = 0)
    assert solve_quadratic_equation(1, -2, 1) == (1.0,)
    # Trường hợp vô nghiệm thực (Delta < 0)
    assert solve_quadratic_equation(1, 1, 1) == "NO_SOLUTION"

# --- Bài 4: Tính số ngày của tháng (Dữ liệu hợp lệ) ---
def test_days_in_month_valid():
    assert get_days_in_month(1, 2023) == 31
    assert get_days_in_month(4, 2023) == 30
    assert get_days_in_month(2, 2024) == 29  # Năm nhuận
    assert get_days_in_month(2, 2023) == 28  # Năm không nhuận

# --- Bài 5: Kiểm tra số nguyên tố (Dữ liệu hợp lệ) ---
def test_is_prime_valid():
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(17) is True
    assert is_prime(4) is False
    assert is_prime(9) is False

# --- Bài 6: Tính tổng S = 1 - 2 + 3 - 4 + ... + n (Dữ liệu hợp lệ) ---
def test_alternating_sum_valid():
    assert calculate_alternating_sum(1) == 1
    assert calculate_alternating_sum(5) == 3
    assert calculate_alternating_sum(6) == -3

# --- Bài 7: Tìm UCLN của a và b (Dữ liệu hợp lệ) ---
def test_gcd_valid():
    assert gcd(12, 18) == 6
    assert gcd(13, 7) == 1
    assert gcd(5, 5) == 5

# --- Bài 8: Tính tổng S = 1! + 2! + ... + n! (Dữ liệu hợp lệ) ---
def test_sum_of_factorials_valid():
    assert sum_of_factorials(1) == 1
    assert sum_of_factorials(3) == 9   # 1! + 2! + 3! = 9
    assert sum_of_factorials(4) == 33  # 1! + 2! + 3! + 4! = 33
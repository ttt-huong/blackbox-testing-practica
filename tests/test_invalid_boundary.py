import pytest
from src.geometry import calculate_rectangle_perimeter, calculate_rectangle_area
from src.equation import solve_quadratic_equation
from src.calendar_utils import get_days_in_month
from src.prime import is_prime
from src.series import calculate_alternating_sum, sum_of_factorials
from src.math_utils import gcd

# --- Bài 1: Tính chu vi hình chữ nhật (Biên & Dữ liệu không hợp lệ) ---
def test_rectangle_perimeter_boundary_and_invalid():
    # Giá trị biên dương rất nhỏ
    assert calculate_rectangle_perimeter(0.01, 0.01) == pytest.approx(0.04)
    # Cạnh bằng 0 (Biên không hợp lệ)
    with pytest.raises(ValueError):
        calculate_rectangle_perimeter(0, 5)
    # Cạnh âm (Không hợp lệ)
    with pytest.raises(ValueError):
        calculate_rectangle_perimeter(-2, 4)
    # Sai kiểu dữ liệu
    with pytest.raises(TypeError):
        calculate_rectangle_perimeter("abc", 3)

# --- Bài 2: Tính diện tích hình chữ nhật (Biên & Dữ liệu không hợp lệ) ---
def test_rectangle_area_boundary_and_invalid():
    # Biên hình vuông đơn vị 1x1
    assert calculate_rectangle_area(1, 1) == 1
    # Cạnh bằng 0
    with pytest.raises(ValueError):
        calculate_rectangle_area(5, 0)
    # Cạnh âm
    with pytest.raises(ValueError):
        calculate_rectangle_area(-3, -4)

# --- Bài 3: Giải phương trình bậc 2 (Biên suy biến & Dữ liệu sai) ---
def test_quadratic_equation_boundary_and_invalid():
    # Biên a = 0 (Trở thành pt bậc nhất bx + c = 0)
    assert solve_quadratic_equation(0, 2, -4) == (2.0,)
    # a = 0, b = 0, c != 0 (Vô nghiệm)
    assert solve_quadratic_equation(0, 0, 5) == "NO_SOLUTION"
    # a = 0, b = 0, c = 0 (Vô số nghiệm)
    assert solve_quadratic_equation(0, 0, 0) == "INFINITE_SOLUTIONS"
    # Sai kiểu dữ liệu
    with pytest.raises(TypeError):
        solve_quadratic_equation("a", 1, 2)

# --- Bài 4: Tính số ngày của tháng (Biên thế kỷ & Dữ liệu sai) ---
def test_days_in_month_boundary_and_invalid():
    # Biên năm nhuận thế kỷ (chia hết cho 400)
    assert get_days_in_month(2, 2000) == 29
    # Biên năm không nhuận thế kỷ (chia hết cho 100 nhưng không chia hết cho 400)
    assert get_days_in_month(2, 1900) == 28
    # Biên tháng 12
    assert get_days_in_month(12, 2023) == 31
    # Tháng < 1 (Không hợp lệ)
    with pytest.raises(ValueError):
        get_days_in_month(0, 2024)
    # Tháng > 12 (Không hợp lệ)
    with pytest.raises(ValueError):
        get_days_in_month(13, 2024)
    # Năm âm (Không hợp lệ)
    with pytest.raises(ValueError):
        get_days_in_month(5, -2020)

# --- Bài 5: Kiểm tra số nguyên tố (Biên & Dữ liệu sai) ---
def test_is_prime_boundary_and_invalid():
    # Các giá trị biên: 0, 1 (không phải số nguyên tố)
    assert is_prime(1) is False
    assert is_prime(0) is False
    # Số nguyên âm
    assert is_prime(-7) is False
    # Số thực (Sai kiểu dữ liệu)
    with pytest.raises(TypeError):
        is_prime(3.5)

# --- Bài 6: Tính tổng S đan dấu (Biên & Dữ liệu sai) ---
def test_alternating_sum_boundary_and_invalid():
    # Giá trị biên n = 2
    assert calculate_alternating_sum(2) == -1
    # n = 0 (Không hợp lệ)
    with pytest.raises(ValueError):
        calculate_alternating_sum(0)
    # n âm (Không hợp lệ)
    with pytest.raises(ValueError):
        calculate_alternating_sum(-5)

# --- Bài 7: Tìm UCLN (Biên & Dữ liệu sai) ---
def test_gcd_boundary_and_invalid():
    # Biên 1 số bằng 0
    assert gcd(0, 8) == 8
    # Số âm: UCLN(-12, 18) = 6
    assert gcd(-12, 18) == 6
    # Biên đặc biệt: UCLN(0, 0) không xác định -> Báo lỗi
    with pytest.raises(ValueError):
        gcd(0, 0)

# --- Bài 8: Tính tổng giai thừa (Biên & Dữ liệu sai) ---
def test_sum_of_factorials_boundary_and_invalid():
    # Giá trị biên n = 2
    assert sum_of_factorials(2) == 3
    # n = 0 (Không hợp lệ)
    with pytest.raises(ValueError):
        sum_of_factorials(0)
    # n âm (Không hợp lệ)
    with pytest.raises(ValueError):
        sum_of_factorials(-3)
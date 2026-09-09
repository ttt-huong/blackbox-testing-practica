# BẢNG TỔNG HỢP DANH SÁCH TEST CASE KIỂM THỬ HỘP ĐEN

## Bài 1: Tính chu vi hình chữ nhật
| Mã TC | Phân loại | Đầu vào ($a, b$) | Kỳ vọng đầu ra (Expected) | Kỹ thuật áp dụng | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TC1.1** | Hợp lệ | $a = 5, b = 3$ | $P = 16$ | Phân lớp tương đương (Số nguyên dương) | PASSED |
| **TC1.2** | Hợp lệ | $a = 4.5, b = 2.5$ | $P = 14.0$ | Phân lớp tương đương (Số thực dương) | PASSED |
| **TC1.3** | Biên | $a = 0.01, b = 0.01$ | $P = 0.04$ | Phân tích giá trị biên ($a, b \to 0^+$) | PASSED |
| **TC1.4** | Không hợp lệ | $a = 0, b = 5$ | Báo lỗi `ValueError` | Phân tích giá trị biên ($a = 0$) | PASSED |
| **TC1.5** | Không hợp lệ | $a = -2, b = 4$ | Báo lỗi `ValueError` | Phân lớp tương đương (Cạnh âm) | PASSED |
| **TC1.6** | Không hợp lệ | $a = \text{"abc"}, b = 3$ | Báo lỗi `TypeError` | Dữ liệu sai kiểu dữ liệu | PASSED |

---

## Bài 2: Tính diện tích hình chữ nhật
| Mã TC | Phân loại | Đầu vào ($a, b$) | Kỳ vọng đầu ra (Expected) | Kỹ thuật áp dụng | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TC2.1** | Hợp lệ | $a = 6, b = 4$ | $S = 24$ | Phân lớp tương đương (Số nguyên dương) | PASSED |
| **TC2.2** | Hợp lệ | $a = 3.5, b = 2.0$ | $S = 7.0$ | Phân lớp tương đương (Số thực dương) | PASSED |
| **TC2.3** | Biên | $a = 1, b = 1$ | $S = 1$ | Phân tích giá trị biên | PASSED |
| **TC2.4** | Không hợp lệ | $a = 5, b = 0$ | Báo lỗi `ValueError` | Phân tích giá trị biên ($b = 0$) | PASSED |
| **TC2.5** | Không hợp lệ | $a = -3, b = -4$ | Báo lỗi `ValueError` | Phân lớp tương đương (Số âm) | PASSED |

---

## Bài 3: Giải phương trình bậc 2 ($ax^2 + bx + c = 0$)
| Mã TC | Phân loại | Đầu vào ($a, b, c$) | Kỳ vọng đầu ra (Expected) | Kỹ thuật áp dụng | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TC3.1** | Hợp lệ | $a = 1, b = -3, c = 2$ | $(2.0, 1.0)$ (2 nghiệm pb) | Phân lớp tương đương ($\Delta > 0$) | PASSED |
| **TC3.2** | Hợp lệ | $a = 1, b = -2, c = 1$ | $(1.0,)$ (Nghiệm kép) | Phân tích giá trị biên ($\Delta = 0$) | PASSED |
| **TC3.3** | Hợp lệ | $a = 1, b = 1, c = 1$ | `"NO_SOLUTION"` (Vô nghiệm) | Phân lớp tương đương ($\Delta < 0$) | PASSED |
| **TC3.4** | Biên suy biến | $a = 0, b = 2, c = -4$ | $(2.0,)$ (1 nghiệm) | Phân tích giá trị biên ($a = 0, b \ne 0$) | PASSED |
| **TC3.5** | Biên suy biến | $a = 0, b = 0, c = 5$ | `"NO_SOLUTION"` | Phân tích giá trị biên ($a = 0, b = 0, c \ne 0$) | PASSED |
| **TC3.6** | Biên suy biến | $a = 0, b = 0, c = 0$ | `"INFINITE_SOLUTIONS"` | Phân tích giá trị biên ($a = b = c = 0$) | PASSED |
| **TC3.7** | Không hợp lệ | $a = \text{"a"}, b = 1, c = 2$ | Báo lỗi `TypeError` | Sai kiểu dữ liệu | PASSED |

---

## Bài 4: Tính số ngày của một tháng
| Mã TC | Phân loại | Đầu vào (`month, year`) | Kỳ vọng đầu ra | Kỹ thuật áp dụng | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TC4.1** | Hợp lệ | `month = 1, year = 2023` | 31 | Phân lớp tương đương (Tháng 31 ngày) | PASSED |
| **TC4.2** | Hợp lệ | `month = 4, year = 2023` | 30 | Phân lớp tương đương (Tháng 30 ngày) | PASSED |
| **TC4.3** | Hợp lệ | `month = 2, year = 2024` | 29 | Năm nhuận thường (chia hết cho 4) | PASSED |
| **TC4.4** | Hợp lệ / Biên | `month = 2, year = 2000` | 29 | Biên năm nhuận thế kỷ (chia hết 400) | PASSED |
| **TC4.5** | Hợp lệ / Biên | `month = 2, year = 1900` | 28 | Biên năm không nhuận thế kỷ (chia 100) | PASSED |
| **TC4.6** | Hợp lệ | `month = 2, year = 2023` | 28 | Năm thường không nhuận | PASSED |
| **TC4.7** | Biên | `month = 12, year = 2023` | 31 | Biên tháng 12 | PASSED |
| **TC4.8** | Không hợp lệ | `month = 0, year = 2024` | Báo lỗi `ValueError` | Biên dưới tháng ($month < 1$) | PASSED |
| **TC4.9** | Không hợp lệ | `month = 13, year = 2024` | Báo lỗi `ValueError` | Biên trên tháng ($month > 12$) | PASSED |
| **TC4.10** | Không hợp lệ | `month = 5, year = -2020` | Báo lỗi `ValueError` | Năm âm | PASSED |

---

## Bài 5: Kiểm tra số nguyên tố
| Mã TC | Phân loại | Đầu vào ($n$) | Kỳ vọng đầu ra | Kỹ thuật áp dụng | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TC5.1** | Biên / Hợp lệ | $n = 2$ | `True` | Phân tích giá trị biên (SNT nhỏ nhất, chẵn) | PASSED |
| **TC5.2** | Hợp lệ | $n = 3$ | `True` | Phân lớp tương đương (SNT lẻ nhỏ) | PASSED |
| **TC5.3** | Hợp lệ | $n = 17$ | `True` | Phân lớp tương đương (SNT lớn hơn) | PASSED |
| **TC5.4** | Hợp lệ | $n = 4$ | `False` | Phân tích giá trị biên (Hợp số nhỏ nhất) | PASSED |
| **TC5.5** | Hợp lệ | $n = 9$ | `False` | Phân lớp tương đương (Hợp số lẻ) | PASSED |
| **TC5.6** | Biên | $n = 1$ | `False` | Phân tích giá trị biên ($n = 1$) | PASSED |
| **TC5.7** | Biên | $n = 0$ | `False` | Phân tích giá trị biên ($n = 0$) | PASSED |
| **TC5.8** | Không hợp lệ | $n = -7$ | `False` | Phân lớp số âm | PASSED |
| **TC5.9** | Không hợp lệ | $n = 3.5$ | Báo lỗi `TypeError` | Dữ liệu số thực | PASSED |

---

## Bài 6: Tính tổng $S = 1 - 2 + 3 - 4 + \dots + (-1)^{n-1} \cdot n$
| Mã TC | Phân loại | Đầu vào ($n$) | Kỳ vọng đầu ra | Kỹ thuật áp dụng | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TC6.1** | Biên / Hợp lệ | $n = 1$ | $1$ | Phân tích giá trị biên ($n = 1$) | PASSED |
| **TC6.2** | Biên / Hợp lệ | $n = 2$ | $-1$ | Phân tích giá trị biên ($n = 2$) | PASSED |
| **TC6.3** | Hợp lệ | $n = 5$ | $3$ | Phân lớp tương đương ($n$ lẻ) | PASSED |
| **TC6.4** | Hợp lệ | $n = 6$ | $-3$ | Phân lớp tương đương ($n$ chẵn) | PASSED |
| **TC6.5** | Không hợp lệ | $n = 0$ | Báo lỗi `ValueError` | Phân tích giá trị biên ($n = 0$) | PASSED |
| **TC6.6** | Không hợp lệ | $n = -5$ | Báo lỗi `ValueError` | Phân lớp số âm | PASSED |

---

## Bài 7: Tìm UCLN của $a$ và $b$
| Mã TC | Phân loại | Đầu vào ($a, b$) | Kỳ vọng đầu ra | Kỹ thuật áp dụng | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TC7.1** | Hợp lệ | $a = 12, b = 18$ | $6$ | Phân lớp tương đương (Có ước chung $> 1$) | PASSED |
| **TC7.2** | Hợp lệ | $a = 13, b = 7$ | $1$ | Phân lớp tương đương (Nguyên tố cùng nhau) | PASSED |
| **TC7.3** | Biên | $a = 5, b = 5$ | $5$ | Phân tích giá trị biên ($a = b$) | PASSED |
| **TC7.4** | Biên | $a = 0, b = 8$ | $8$ | Phân tích giá trị biên ($a = 0$) | PASSED |
| **TC7.5** | Hợp lệ | $a = -12, b = 18$ | $6$ | Xử lý số âm $\text{gcd}(\|a\|, \|b\|)$ | PASSED |
| **TC7.6** | Không hợp lệ | $a = 0, b = 0$ | Báo lỗi `ValueError` | Biên không xác định | PASSED |

---

## Bài 8: Tính tổng $S = 1! + 2! + 3! + \dots + n!$
| Mã TC | Phân loại | Đầu vào ($n$) | Kỳ vọng đầu ra | Kỹ thuật áp dụng | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TC8.1** | Biên / Hợp lệ | $n = 1$ | $1$ | Phân tích giá trị biên ($n = 1$) | PASSED |
| **TC8.2** | Biên / Hợp lệ | $n = 2$ | $3$ | Phân tích giá trị biên ($n = 2$) | PASSED |
| **TC8.3** | Hợp lệ | $n = 3$ | $9$ ($1! + 2! + 3! = 9$) | Phân lớp tương đương | PASSED |
| **TC8.4** | Hợp lệ | $n = 4$ | $33$ ($1! + 2! + 3! + 4! = 33$) | Phân lớp tương đương | PASSED |
| **TC8.5** | Không hợp lệ | $n = 0$ | Báo lỗi `ValueError` | Phân tích giá trị biên ($n = 0$) | PASSED |
| **TC8.6** | Không hợp lệ | $n = -3$ | Báo lỗi `ValueError` | Phân lớp số âm | PASSED |
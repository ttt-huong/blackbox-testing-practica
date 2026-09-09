# BÀI THỰC HÀNH: KIỂM THỬ HỘP ĐEN (BLACK-BOX TESTING)

## 📌 Giới thiệu dự án
Dự án được xây dựng nhằm áp dụng các kỹ thuật **Kiểm thử hộp đen (Black-box Testing)** để thiết kế ca kiểm thử và kiểm tra mã nguồn cho 8 bài toán cơ bản:
1. **Bài 1**: Tính chu vi hình chữ nhật
2. **Bài 2**: Tính diện tích hình chữ nhật
3. **Bài 3**: Giải phương trình bậc 2 ($ax^2 + bx + c = 0$)
4. **Bài 4**: Tính số ngày của một tháng (xử lý năm nhuận, năm thế kỷ)
5. **Bài 5**: Kiểm tra số nguyên tố
6. **Bài 6**: Tính tổng $S = 1 - 2 + 3 - 4 + \dots + (-1)^{n-1} \cdot n$
7. **Bài 7**: Tìm Ước chung lớn nhất (UCLN) của $a$ và $b$
8. **Bài 8**: Tính tổng $S = 1! + 2! + 3! + \dots + n!$ (có hàm tính giai thừa)

---

## 🎯 Kỹ thuật kiểm thử hộp đen áp dụng
- **Phân lớp tương đương (Equivalence Partitioning)**:
  - Chia miền giá trị đầu vào thành miền dữ liệu hợp lệ (Valid Partition) và không hợp lệ (Invalid Partition).
  - Kiểm tra các trường hợp đại diện cho từng lớp.
- **Phân tích giá trị biên (Boundary Value Analysis)**:
  - Tập trung kiểm thử tại các giá trị biên như $0, 1, 2$, số âm sát 0, biên tháng $1, 12$, năm nhuận thế kỷ chia hết 400 ($2000$), năm không nhuận thế kỷ chia hết 100 ($1900$).
- **Kiểm thử dữ liệu không hợp lệ & ngoại lệ**:
  - Đảm bảo chương trình ném ngoại lệ rõ ràng (`ValueError`, `TypeError`) khi nhận cạnh $\le 0$, tháng ngoài $[1, 12]$, sai kiểu dữ liệu...

---

## 📁 Cấu trúc thư mục dự án
```text
blackbox-testing-practica/
├── src/                        # Mã nguồn 8 thuật toán
│   ├── geometry.py             # Bài 1, Bài 2
│   ├── equation.py             # Bài 3
│   ├── calendar_utils.py       # Bài 4
│   ├── prime.py                # Bài 5
│   ├── series.py               # Bài 6, Bài 8
│   └── math_utils.py           # Bài 7
├── tests/                      # Bộ kiểm thử tự động
│   ├── test_valid_cases.py     # Kiểm thử dữ liệu hợp lệ (Issue #1)
│   └── test_invalid_boundary.py # Kiểm thử biên và ngoại lệ (Issue #2)
├── docs/
│   └── TEST_CASES.md           # Bảng chi tiết toàn bộ test case
├── pytest.ini                  # Cấu hình đường dẫn pytest
├── requirements.txt            # Thư viện pytest
└── README.md                   # Báo cáo tổng quan dự án
```

---

## 🚀 Hướng dẫn cài đặt và chạy kiểm thử

### 1. Cài đặt thư viện:
```bash
pip install -r requirements.txt
```

### 2. Chạy toàn bộ kiểm thử:
```bash
pytest -v
```

---

## 📊 Kết quả chạy kiểm thử (Test Execution Results)
- `tests/test_valid_cases.py`: 8/8 PASSED (Đóng Issue #1)
- `tests/test_invalid_boundary.py`: 8/8 PASSED (Đóng Issue #2)
- **Tổng kết**: 100% Test cases đều PASSED.

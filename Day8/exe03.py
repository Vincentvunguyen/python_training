# Nhập hai số a và b từ bàn phím. In ra số lớn nhất và nhỏ nhất trong hai số
"""a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))"""

a, b = map(float("Nhập a và b: ").split())
if a > b:
    print(f"Số lớn nhất là {a}, số nhỏ nhất là {b}")
elif a < b:
    print(f"Số lớn nhất là {b}, số nhỏ nhất là {a}")
else:
    print(f"Hai số bằng nhau")

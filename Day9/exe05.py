# Nhập vào một số nguyên dương n tính tổng các chữ số của n. Ví dụ: n = 4312 => S = 4 + 3 + 1 + 2 = 10
number = int(input("Nhập vào số dương: "))
s = 0

while number <= 0:
    print("Số nhập vào phải là số dương")
    number = int(input("Nhập lại một số dương: "))

while number > 0:
    m = number % 10
    s = s + m
    number = number // 10

print(s)

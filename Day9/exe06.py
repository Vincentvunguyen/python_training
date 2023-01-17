# Nhập vào một số nguyên dương n. Đếm số lượng số chẵn và lẻ trong đoạn [0, n]
n = int(input("Nhập vào số dương: "))


while n <= 0:
    print("Số nhập vào phải là số dương")
    n = int(input("Nhập vào số dương: "))

even = 0
odd = 0
for i in range(0, n):
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print(f"Số lượng số chẵn là {even}")
print(f"Số lượng số lẻ là {odd}")

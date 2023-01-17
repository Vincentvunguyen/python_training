# Đếm số lượng số nguyên tố trong [1, 100]
amount = 0

for n in range(2, 101):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            break
    else:
        amount = amount + 1
        print(n, end=" ")

print(f"\nSố lượng số nguyên tố là {amount}")

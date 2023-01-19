# Đếm số chẵn và lẻ trong đoạn [0, 1000] theo 2 cách: thông thường và list comprehension
"""
even = 0
odd = 0
for i in range(0, 1001):
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print(f"Số lượng số chẵn là {even}")
print(f"Số lượng số lẻ là {odd}")"""

evens = [i for i in range(0, 1001) if i % 2 == 0]
odds = [i for i in range(0, 1001) if i % 2 != 0]

print(f"Số lượng số chẵn là {len(evens)}")
print(f"Số lượng số lẻ là {len(odds)}")

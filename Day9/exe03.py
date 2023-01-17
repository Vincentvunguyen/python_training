# In ra các số chia hết cho 3 trong đoạn [1, 1000]
for i in range(1, 100):
    if i % 3 != 0:
        continue

    print(i)

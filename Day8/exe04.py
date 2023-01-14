# Giải và biện luận phương trình bậc nhất một ẩn ax + b = 0 (ẩn x, a và b là hai số cho trước)
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
print(f"Phương trình cần giải {a}x + {b} = 0")

if a == 0:
    if b == 0:
        print("Phương trình có vô số nghiệm")
    else:
        print("Phương trình vô nghiệm")
elif a != 0 and b ==0:
    print(f"Phương trình có nghiệm bằng duy nhất bằng 0")
else:
   print(f"Phương trình có nghiệm duy nhất bằng {-b/a}")

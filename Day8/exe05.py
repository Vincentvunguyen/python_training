import math

# Giải và biện luận phương trình bậc nhất một hai ax^2 + bx + c = 0 (ẩn x, a, b, c là ba số cho trước)
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
c = float(input("Nhập số c: "))
print(f"Phương trình cần giải {a}x^2 + {b}x + {c} = 0")

if a == 0:
    if b == 0:
        if c == 0:
            print(" Phương trình có vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        print(f"Phương trình có một nghiệm {-c/b}")
else:
    d = b*b - 4*a*c
    if d == 0:
        print(f"Phương trình có nghiệm kép x1 = x2 = {-b/(2*a)}")
    elif d > 0:
        print(f"Phương trình có 2 nghiệm x1 = {(-b+math.sqrt(d))/(2*a)} và x2 = {(-b-math.sqrt(d))/(2*a)}")
    else:
        print("Phương trình vô nghiệm")

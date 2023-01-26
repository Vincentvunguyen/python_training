# Định nghĩa 4 hàm add, subtract, divide, multiply (+, -, /, *). Mỗi hàm nhận vào hai tham số thực hiện lần lượt các phép toán cộng, trừ, chia, nhân. Lưu ý hàm nên trả về thay vì in ra.
x = float(input("Nhập x: "))
y = float(input("Nhập y: "))

def add(x, y):
    print(x+y)

def subtract(x, y):
    print(x-y)

def divine(x, y):
    if y == 0:
        print("Không thể thực hiện phép chia")
    else:
        print(x/y)

def multiply(x, y):
    print(x*y)


add(x,y)
subtract(x,y)
divine(x,y)
multiply(x,y)

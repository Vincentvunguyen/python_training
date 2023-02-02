# Tạo một class hình chữ nhật chứa hai thuộc tính: chiều dài và chiều rộng
length = int(input("Nhập chiều dài: "))
width = int(input("Nhập chiều rộng: "))

class Rectagle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def chu_vi(self):
        return (self.length + self.width)
    
    def dien_tich(self):
        return (self.length * self.width)*2

    def __str__(self):
        return f'''Hình chữ nhật có chiều dài là {self.length} - chiều rộng là {self.width}
Chu vi hình chữ nhật {self.chu_vi()}
Diện tích hình chữ nhật là {self.dien_tich()}'''

rectagle1 = Rectagle(length, width)
print(rectagle1)

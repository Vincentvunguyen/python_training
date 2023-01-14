# Nhập vào một năm bất kỳ. Kiểm tra xem năm đó có phải là năm nhuận hay không ?
year = int(input("Nhập năm: "))
if year % 400 == 0:
    print("Năm nhuận")
elif year % 4 == 0 and year % 100 != 0:
    print("Năm nhuận")
else:
    print("Không phải năm nhuận")

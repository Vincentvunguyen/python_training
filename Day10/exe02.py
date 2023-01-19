# Nhập vào một danh sách những số nguyên và hiển thị gấp đôi của các số trong danh sách sử dụng list comprehension
lst_numbers = [int(i) for i in input(
    "Nhập vào danh sách các số nguyên: ").split()]
print(lst_numbers)

double_numbers = [i * 2 for i in lst_numbers]

print(double_numbers)


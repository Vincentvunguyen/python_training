numbers = [1, 2, 3.5, 4]

# gia tri lon nhat cua list nếu là sơ, nếu là str thì là str dài nhất
max_value = max(numbers) 
print(max_value)

# them 100 vao cuoi list
numbers.append(100)  
print(numbers)

# xoa gia tri 1 hoac del numbers[1]
numbers.remove(1)  
print(numbers)

# lay ra gia tri cuoi cung va gan vao last_value va xoa khoi list
last_value = numbers.pop()  
print(last_value)

 # them 1 list vao list hien co
numbers.extend([3.5, 1000, 2, 125]) 
print(numbers)

 # thay doi gia tri 75 vao vi tri 0 (vi tri dau tien)
numbers[0] = 75 
print(numbers)

# them mot gia tri vao mot vi tri bat ki
numbers.insert(1, 35) 
print(numbers)

# dem so luong gia tri 1000 trong list
amount = numbers.count(1000) 
print(amount)

# tim vi tri cua 3.5 trong list, chi tra ve vi tri dau tien
index_of_3p5 = numbers.index(3.5) 
print(index_of_3p5)

# dem do dai cua list (so luong gia tri trong list)
do_dai= len(numbers) 
print(do_dai)

# dao nguoc list
numbers.reverse() 
print(numbers)

# sap xep lai list, neu muon xep tu lon den be numbers.sort(reverse = True)
numbers.sort() 
print(numbers)

# xoa toan bo gia tri trong list
numbers.clear() 
print(numbers)



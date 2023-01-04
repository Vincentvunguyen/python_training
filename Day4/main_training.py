numbers = [1, 2, 3.5, 4]

max_value = max(numbers) # gia tri lon nhat cua list
print(max_value)

numbers.append(100)  # them 100 vao cuoi list
print(numbers)

numbers.remove(1)  # xoa gia tri 1 hoac del numbers[1]
print(numbers)

last_value = numbers.pop()  # lay ra gia tri cuoi cung va gan lao last_value
print(last_value)

numbers.extend([3.5, 1000, 2, 125])  # them 1 list vao list hien co
print(numbers)

numbers[0] = 75  # thay doi gia tri 75 vao vi tri 0 cua 2 (vi tri dau tien)
print(numbers)

numbers.insert(1, 35) # them mot gia tri vao mot vi tri bat ki
print(numbers)

amount = numbers.count(1000) # dem so luong gia tri 3.5 trong list
print(amount)

index_of_3p5 = numbers.index(3.5) # tim vi tri cua 3.5 trong list
print(index_of_3p5)

do_dai= len(numbers) # dem do dai cua list (so luong gia tri trong list)
print(do_dai)

numbers.reverse() # dao nguoc list
print(numbers)

numbers.sort() # sap xep lai list, neu muon xep tu lon den be numbers.sort(reverse = True)
print(numbers)

numbers.clear() # xoa toan bo gia tri trong list
print(numbers)



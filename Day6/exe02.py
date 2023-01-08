# Tạo set trống
set_a = set()

# Thêm 'Anna' vào set_a
set_a.add("Anna")
print(set_a)

# Thêm một tuple ('Kenny', 'Jen', 'Danny')
name = ('Kenny', 'Jen', 'Danny')
print(type(name))
set_a.update(name)

# In ra set_a và tính chiều dài của nó
print(set_a)
print(len(set_a))

# Xóa 'Jen' ra khỏi set_a
set_a.remove("Jen")
print(set_a)

# Xóa tất cả các giá trị từ set_a
set_a.clear()
print(set_a)

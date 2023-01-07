students = [["SV001", "Bob", 23], [
    "SV002", "Kenny", 34], ["SV003", "Henry", 45]]

# Lấy ra thông tin của sinh viên thứ nhất và in ra định dạng "ID: {id}, name: {name} - age: {age}"
id1 = students[0][0]
name1 = students[0][1]
age1 = students[0][2]
print(f"""ID: {id1}, name: {name1} - age: {age1}""")

# Lấy ra tuổi của sinh viên thứ hai
age2 = students[1][2]
print(age2)

# Lấy ra thông tin hai sinh viên cuối cùng
new_students = students[-2:]
print(new_students)
print(
    f"""ID: {students[1][0]}, name: {students[1][1]} - age: {students[1][2]}""")
print(
    f"""ID: {students[2][0]}, name: {students[2][1]} - age: {students[2][2]}""")

#  Lấy ra id của sinh viên thứ ba
id3 = students[2][0]
print(id3)

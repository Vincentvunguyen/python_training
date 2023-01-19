import json
people = {
    "Emma": 71,
    "Jack": 45,
    "Amy": 15,
    "Ben": 29
}
# In ra người già nhất
for key, value in people.items():
    if value == max(people.values()):
        print(f"Người lớn tuổi nhất là {key}: {value}")

# Tạo ra một dict mới dựa vào people dict với tuổi của mỗi người tăng gấp đôi
double_age = {
    k: v*2
    for k, v in people.items()
}
print(json.dumps(double_age, indent=4))

# In ra enumerate các key trong people dict
new_lst = [key for key in people]
print(list(enumerate(new_lst)))

# Sử dụng hàm dict để biến enumerate bên trên trở thành dict
new_people = dict(enumerate(new_lst))
print(json.dumps(new_people, indent=4))

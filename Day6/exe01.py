friends = [("Bob", "Male"),
           ("Anna", "Female"),
           ("Max", "Male")]

# Cho biết chiều dài của friends
print(len(friends))

# Lấy ra phần tử đầu, cuối và giữa và kiểm tra kiểu của chúng
first_friends = friends[0]
middle_friends = friends[1]
last_friends = friends[-1]
print(type(first_friends))
print(type(middle_friends))
print(type(last_friends))

# Nhập vào tên (name) và giới tính (gender) của một người bạn sau đó append vào friends tuple gồm hai giá trị (name, gender)
new_value = ("Jack", "Male")
friends.append(new_value)
print(friends)

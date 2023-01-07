friends = ["Jen", "Jack", "Kenny", "Jelly", "Bob", "Henry", "Anne"]

# Lấy ra 4 người bạn đầu tiên trong friends
friends_one = friends[:4]
print(friends_one)

# Lấy ra 4 người bạn cuối trong friends
friends_two = friends[3:]
print(friends_two)

# Đảo ngược danh sách friends
friends_three = friends[::-1]
print(friends_three)

# Lấy ra những người bạn từ vị trí 1 đến hết
friends_four = friends[1:]
print(friends_four)

# Copy danh sách ban đầu thành một danh sách mới
friends_five = friends.copy()
print(friends_five)

# Lấy ra những người bạn từ vị trí 2 đến sát cuối
friends_six = friends[2:-1]
print(friends_six)

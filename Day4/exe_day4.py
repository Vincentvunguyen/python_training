# 1.Tạo list film
list_films = ["How I met your mother", "One Piece", "Gió", "X Files", "Avatar"]
print("Danh sách films ", list_films)

# 2.Sử dụng hàm input để nhập vào một bộ phim khác không có trong movies list
# 3.Thêm bộ phim vừa nhập vào cuối của danh sách movies
list_films.append(input("Nhập thêm film vào cuối: "))
print(list_films)

# 4.In ra bộ phim đầu tiên, cuối cùng và ở giữa movies list
count_list = len(list_films)
print(f""" Tên film đầu {list_films[0]} 
                giữa {list_films[count_list //2]}
                cuối: {list_films[-1]}""")

# 5.Tính tổng bộ phim có trong movies
print(f"Tổng số film trong list là {len(list_films)}")

# 6.Xóa bộ phim đầu và cuối trong movies
list_films.remove(list_films[0])
list_films.remove(list_films[-1])
print("Danh sách films hiện tại", list_films)

# 7.Lấy ra và xóa bộ phim cuối cùng trong movies
list_films.pop()
print("Danh sách films hiện tại", list_films)

# 8.Chèn một bộ phim bất kỳ vào đầu danh sách movies
list_films.insert(0, input("Chèn vào đầu list: "))
print("Danh sách films hiện tại", list_films)

# 9.Đếm số bộ phim có tiêu đề là "One Piece"
amount = list_films.count("One Piece")
print(f"Số tiêu đề One Piece là {amount}")

# 10.Tìm vị trí của bộ phim có tên là "gió"
index_of_Gio = list_films.index("Gió")
print(f"Vị trí của film Gió là {index_of_Gio}")


# 11.Thêm một danh sách bộ phim khác vào cuối danh sách movies ban đầu
list_films.extend(["Harry Potter", "Xmens"])
print("Danh sách films hiện tại", list_films)

# 12.Xóa tất cả các bộ phim có trong danh sách
list_films.clear()
print("Danh sách films cuối cùng", list_films)

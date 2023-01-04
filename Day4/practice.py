# Ex1 Tạo một movies list chứa tên các bộ phim đã xem
movie_list = ["Doremon", "gió", "OnePiece", "Dragonball", "Pokemon"]
print(f"danh sách phim {movie_list}")
# Ex2 Sử dụng hàm input để nhập vào một bộ phim khác không có trong movies list
insert_movie_list = movie_list.append(input("nhập thêm Phim :"))
# Ex3 Thêm bộ phim vừa nhập vào cuối của danh sách movies
print(f"nhập thêm phim : ", movie_list)
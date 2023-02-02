
# Định nghĩa cấu trúc dữ liệu 
movies = []

# # Kiểm tra các bộ phim duy nhất
prevs   = set()

# Thêm film
def add_movie()
        name = input("Nhập tên film: ")
        while name in prevs:
            print("Film đã có trong list")
            name = input("Nhập tên film: ")
         
        drt = input("Nhập director: ")
        year = input("Nhập năm sản xuất: ")
        movie = {
                "title": name,
                "director": drt,
                "release_year": year,
                }
        movies.append(movie)
        prevs   = set()

# Hiển thị thông tin film:
def print_movie_info(movie):
    print(f"{movie['title']} - Năm phát hành: ({movie['release_year']}) - Đạo diễn: {movie['director']}")

# Sửa thông tin của một bộ phim
def update_movie()
    if movies:
        movie_name = input("Nhập vào tên bộ phim: ")

        founds = [
            idx
            for idx, movie in enumerate(movies)
            if movie['name'] == movie_name
        ]

        if founds:
            position                            = founds[0]
            movies[position]['tilte']        = input("Nhập vào tên cần chỉnh sửa\t: ")
            movies[position]['director']        = input("Nhập vào tên đạo diễn\t: ")
            movies[position]['release_year']    = input("Nhập vào năm phát hành\t: ")

            print("Cập nhật bộ phim thành công!")
        else:
            print("Không có bộ phim có tên là", movie_name)
    else:
        print("Danh sách phim trống!")



# Định nghĩa một hàm được gọi là print_show_info nhận vào một tham số duy nhất đó là một dict:

def print_show_info(tv_show):
    print(f"{tv_show['title']} ({tv_show['initial_release']}) - {tv_show['seasons']} seasons")

name = input("Nhập title: ")
season = input("Nhập season: ")
year = input("Nhập năm sản xuất: ")
show_info = {
    "title": name,
    "seasons": season,
    "initial_release": year
}

print_show_info(show_info)

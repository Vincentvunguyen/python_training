import json
album_info = {
    "album_name": "The Dark Side of the Moon",
    "band": "Pink Floyd",
    "release_year": 1973,
    "track_list": [
        "Speak to Me",
        "Breathe",
        "On the Run",
        "Time",
        "The Great Gig in the Sky",
        "Money",
        "Us and Them",
        "Any Colour You Like",
        "Brain Damage",
        "Eclipse"
    ]
}
print(json.dumps(album_info, indent=4))

# Lấy ra giá trị của các key sau: album_name, release_year bằng hai cách
value = album_info['album_name']
print(value)

print(album_info.get('release_year'))

# Thay đổi giá trị của key: release_year từ 1973 thành 1971
album_info['release_yprint(json.dumps(album_info, indent = 4))ear'] = 1971

# Xóa phần tử với key là track_list
del album_info['track_list']
print(album_info)

# Thêm một key mới là amount = 2000 bằng hai cách
# Cach 1: album_info.update(amount = "2000")
# Cach 2:
new_value = {
    'amount': 2000
}
album_info.update(new_value)
print(json.dumps(album_info, indent=4))

# Làm trống dict: album_info
album_info.clear()
print(album_info)

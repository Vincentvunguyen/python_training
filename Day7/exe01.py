art_students = {"John", "Max", "Anna", "Bob", "Obito"}

math_students = {"Max", "Mery", "David", "Anna", "Naruto", "John"}

# Tìm những người bạn học cả vẽ lẫn toán
art_math = art_students.intersection(math_students)
print("Những người bạn học cả vẽ lẫn toán", art_math)

# Tìm những người bạn học vẽ nhưng không học toán
art_not_math = art_students.difference(math_students)
print("Những người bạn học vẽ nhưng không học toán", art_not_math)

# Tìm những người bạn học toán nhưng không học vẽ
math_not_art = math_students.difference(art_students)
print("Những người bạn học toán nhưng không học vẽ", math_not_art)

# Tìm những người bạn học vẽ hay toán không phải cả hai
math_or_art = math_students.symmetric_difference(art_students)
print("Những người bạn học vẽ hay toán không phải cả hai", math_or_art)

# Tìm tất cả những người bạn
math_and_art = math_students.union(art_students)
print("Tất cả những người bạn", math_and_art)

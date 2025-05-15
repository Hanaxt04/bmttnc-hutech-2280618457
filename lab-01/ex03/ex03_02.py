def daonguoc(lst):
    return lst[::-1]

# Nhập danh sách từ người dùng và xử lý chuỗi
input_string = input("Nhập danh sách số nguyên cách nhau bởi dấu phẩy: ")
numbers = list(map(int, input_string.split(',')))
# Sử dụng hàm và in kết quả
result = daonguoc(numbers)
print("Danh sách sau khi đảo ngược là:", result)
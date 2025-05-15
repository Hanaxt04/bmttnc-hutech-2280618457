def tinhtongsochan(lst):
    tong = 0
    for i in lst:
        if i % 2 == 0:
            tong += i
    return tong
# Nhập danh sách từ người dùng và xử lý chuỗi
user_input = input("Nhập danh sách số nguyên cách nhau bởi dấu phẩy: ")
numbers = list(map(int, user_input.split(',')))
#sử dụng hàm và in kết quả
result = tinhtongsochan(numbers)
print("Tổng các số chẵn trong danh sách là:", result)
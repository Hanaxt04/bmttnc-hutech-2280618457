def taotuple(lst):
    return tuple(lst)
# Nhập danh sách từ người dùng và xử lý chuỗi
user_input = input("Nhập danh sách số nguyên cách nhau bởi dấu phẩy: ")
numbers = list(map(int, user_input.split(',')))

mytuple = taotuple(numbers)
print("list:", numbers)
print("tuple:", mytuple)

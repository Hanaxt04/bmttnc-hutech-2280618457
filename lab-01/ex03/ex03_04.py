def truycap(tuple_data):
    first_element = tuple_data[0]
    last_element = tuple_data[-1]
    return first_element, last_element
# Nhập tuple từ người dùng
user_input = eval(input("Nhập một tuple (vd: (1, 2, 3)): "))
first, last = truycap(user_input)
print(f"Phần tử đầu tiên: {first}")
print(f"Phần tử cuối cùng: {last}")
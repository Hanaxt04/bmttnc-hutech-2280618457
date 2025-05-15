def reverse_string(input_string):
    return input_string[::-1]

# Nhập chuỗi từ người dùng
user_input = input("Nhập một chuỗi: ")

# Gọi hàm và in kết quả
reversed_string = reverse_string(user_input)
print(f"Chuỗi đảo ngược là: {reversed_string}")
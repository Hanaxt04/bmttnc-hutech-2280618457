

# Nhập danh sách các số nhị phân 4 chữ số, cách nhau bởi dấu phẩy
binary_numbers = input("Nhập danh sách các số nhị phân 4 chữ số, cách nhau bởi dấu phẩy: ").split(',')




def get_binary_numbers_divisible_by_5(binary_numbers):
    divisible_by_5 = []
    for binary in binary_numbers:
        # Chuyển đổi số nhị phân sang thập phân
        decimal = int(binary, 2)
        # Kiểm tra nếu chia hết cho 5
        if decimal % 5 == 0:
            divisible_by_5.append(binary)
    return divisible_by_5


# Gọi hàm để lấy danh sách các số nhị phân chia hết cho 5
result = get_binary_numbers_divisible_by_5(binary_numbers)

# In ra các số nhị phân chia hết cho 5
print("Các số nhị phân chia hết cho 5 là:", ', '.join(result))
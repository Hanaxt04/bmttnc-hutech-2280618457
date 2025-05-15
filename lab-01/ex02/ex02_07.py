# Nhập nhiều dòng đầu vào từ người dùng
print("Nhập các dòng (nhập 'STOP' để kết thúc):")
lines = []

while True:
    line = input()
    if line.strip().upper() == "STOP":  # Kết thúc khi nhập 'STOP'
        break
    lines.append(line)

# Chuyển đổi tất cả các dòng thành chữ hoa
uppercase_lines = [line.upper() for line in lines]

# Hiển thị các dòng đã chuyển đổi
print("Các dòng sau khi chuyển thành chữ hoa:")
for line in uppercase_lines:
    print(line)
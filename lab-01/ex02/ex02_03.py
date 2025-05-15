#Nhập số từ người dùng
number = int(input("Nhập một số nguyên: "))
#Kiểm tra số đó có chẵn hay không 
if number % 2 == 0:
    print(number, "là số chẵn.")
else:
    print(number, "là số lẻ.")
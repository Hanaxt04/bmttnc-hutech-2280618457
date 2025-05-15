def demsolanxuathien(lst):
    count_dict = {}
    for i in lst:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    return count_dict
# Nhập danh sách từ người dùng
input_string = input("Nhập danh sách số nguyên cách nhau bởi dấu cách: ")
word_list = input_string.split()
# Sử dụng hàm và in kết quả
result = demsolanxuathien(word_list)
print("Số lần xuất hiện của từng từ trong danh sách là:", result)
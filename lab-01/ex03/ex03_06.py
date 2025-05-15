def xoaphantu(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return FFalse
#Sử dụng hàm in kết quả
my_ditc = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
key_to_remove = 'b'
result = xoaphantu(my_ditc, key_to_remove)
if result:
    print("Phần tử đã được xóa thành công:",my_ditc)
else:
    print("Phần tử không tồn tại trong từ điển")
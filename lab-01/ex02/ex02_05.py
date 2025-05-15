so_gio_lam = float(input("Nhập số giờ làm việc trong tuần: "))
luong_theo_gio = float(input("Nhập mức lương theo giờ: "))
gio_tieu_chuan = 44
gio_vuot_chuan = max(0, so_gio_lam - gio_tieu_chuan)
luong_thuc_nhan = gio_tieu_chuan * luong_theo_gio + gio_vuot_chuan * luong_theo_gio * 1.5
#In ra lương thực nhận
print("Lương thực nhận là:", luong_thuc_nhan)
from QuanLySV import QuanLySV

def main():
    qlsv = QuanLySV()
    while True:
        print("====== MENU QUẢN LÝ SINH VIÊN ======")
        print("1. Thêm sinh viên")
        print("2. Cập nhật thông tin sinh viên theo ID")
        print("3. Xóa sinh viên theo ID")
        print("4. Tìm sinh viên theo tên")
        print("5. Sắp xếp theo điểm trung bình")
        print("6. Sắp xếp theo tên chuyên ngành")
        print("7. Hiển thị danh sách sinh viên")
        print("0. Thoát")
        choice = input("Chọn chức năng: ")

        if choice == "1":
            qlsv.nhapSV()
        elif choice == "2":
            id = int(input("Nhập ID cần cập nhật: "))
            qlsv.updateSV(id)
        elif choice == "3":
            id = int(input("Nhập ID cần xóa: "))
            qlsv.deleteById(id)
        elif choice == "4":
            name = input("Nhập tên cần tìm: ")
            results = qlsv.findbyName(name)
            if results:
                for sv in results:
                    print(vars(sv))
            else:
                print("Không tìm thấy sinh viên.")
        elif choice == "5":
            qlsv.sortbydtb()
            print("Đã sắp xếp theo điểm trung bình.")
        elif choice == "6":
            qlsv.listSV.sort(key=lambda x: x._major)
            print("Đã sắp xếp theo tên chuyên ngành.")
        elif choice == "7":
            qlsv.show()
        elif choice == "0":
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()
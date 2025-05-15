import keyword
from SinhVien import SinhVien

class QuanLySV:
    listSV = []
    def generateID(self):
        maxId = 1
        if (self.soluongSV() > 0):
            maxId = self.listSV[0]._id
            for sv in self.listSV:
                if (sv._id > maxId):
                    maxId = sv._id
            maxId = maxId + 1
        return maxId
    
    def soluongSV(self):
        return self.listSV.__len__()
    
    def nhapSV(self):
        id = self.generateID()
        name = input("Nhập tên sinh viên: ")
        sex = input("Nhập giới tính sinh viên: ")
        major = input("Nhập chuyên ngành sinh viên: ")
        dtb = float(input("Nhập điểm trung bình sinh viên: "))
        sv = SinhVien(id, name, sex, major, dtb)
        self.xeploaiHocLuc(sv)
        self.listSV.append(sv)

    def updateSV(self, id):
        for sv in self.listSV:
            if (sv._id == id):
                name = input("Nhập tên sinh viên: ")
                sex = input("Nhập giới tính sinh viên: ")
                major = input("Nhập chuyên ngành sinh viên: ")
                dtb = float(input("Nhập điểm trung bình sinh viên: "))
                sv._name = name
                sv._sex = sex
                sv._major = major
                sv._dtb = dtb   
                self.xeploaiHocLuc(sv)
            else:
                print("Không tìm thấy sinh viên có id: ", id)

    def sortbyID(self):
        self.listSV.sort(key=lambda x: x._id, reverse=False)
    def sortbyName(self):
        self.listSV.sort(key=lambda x: x._name, reverse=False)
    def sortbydtb(self):
        self.listSV.sort(key=lambda x: x._dtb, reverse=False)
    def findbyId (self, id):
        searchResult = None 
        if (self.soluongSV() > 0):
            for sv in self.listSV:
                if (sv._id == id):
                    searchResult = sv
        return searchResult
    def findbyName(self, name):
        listSV = []
        if self.soluongSV() > 0:
            for sv in self.listSV:
                if name.lower() in sv._name.lower():
                    listSV.append(sv)
        return listSV
    
    def deleteById(self, id):
        isDele = False
        sv = self.findbyId(id)
        if (sv != None):
            self.listSV.remove(sv)
            isDele = True
        return isDele
    def xeploaiHocLuc(self, sv):
        if(sv._dtb >= 8):
            sv._hocluc = "Giỏi"
        elif(sv._dtb >= 6.5):
            sv._hocluc = "Khá"
        elif(sv._dtb >= 5):
            sv._hocluc = "Trung bình"
        else :
            sv._hocluc = "Yếu"

    def show(self):
        print("{:<5} {:<20} {:<10} {:<15} {:<10} {:<10}".format("ID", "Họ tên", "Giới tính", "Chuyên ngành", "Điểm TB", "Học lực"))
        if (self.listSV.__len__() > 0):
            for sv in self.listSV:
                print("{:<5} {:<20} {:<10} {:<15} {:<10} {:<10}".format(sv._id, sv._name, sv._sex, sv._major, sv._dtb, sv._hocluc))
        print("\n")
        def getListSV(self):
            return self.listSV
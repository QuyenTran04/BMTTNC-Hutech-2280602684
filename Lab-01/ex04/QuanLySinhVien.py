from SinhVien import SinhVien
class QuanLySinhVien:
    listSinhVien = []
    def generateId(self):
        maxId = 1
        if (self.soLuongSinhVien()>0):
            maxId = self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if (maxId < sv._id):
                    maxId = sv._id
            maxId += 1
        return maxId
    def soLuongSinhVien(self):
        return self.listSinhVien.__len__()
    def nhapSinhVien(self):
        svId = self.generateId()
        name = input("Nhap ten sinh vien: ")
        sex = input("Nhap gioi tinh sinh vien: ")
        major = input("Nhap nganh hoc sinh vien: ")
        diemTB = float(input("Nhap diem trung binh sinh vien: "))
        sv = SinhVien(svId, name, sex , major, diemTB)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)
    def updateSinhVien(self, ID):
        sv:SinhVien = self.findById(ID)
        if (sv != None):
            name = input("Nhap ten sinh vien: ")
            sex = input("Nhap gioi tinh sinh vien: ")
            major = input("Nhap nganh hoc sinh vien: ")
            diemTB = float(input("Nhap diem trung binh sinh vien: "))
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemTB = diemTB
            self.xepLoaiHocLuc(sv)
        else:
            print("Sinh vien co ID = {} khong ton tai".format(ID))
    def softByID(self):
        self.listSinhVien.sort(key=lambda x: x._id , reverse=False)
    def softByName(self):
        self.listSinhVien.sort(key=lambda x: x._name , reverse=False)
    def softByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x._diemTB , reverse=False)
    def findById(self, ID):
        searchResult = None
        if (self.soLuongSinhVien()>0):
            for sv in self.listSinhVien:
                if (sv._id == ID):
                    searchResult = sv
                    
        return searchResult
    def findByName(self, keyword):
        listSV = []
        if (self.soLuongSinhVien()>0):
            for sv in self.listSinhVien:
                if (keyword.upper() in sv._name.upper()):
                    listSV.append(sv)
        return listSV
    def deleteById(self, ID):
        isDelete = False
        sv = self.findById(ID)
        if (sv != None):
            self.listSinhVien.remove(sv)
            isDelete = True
        return isDelete
    def xepLoaiHocLuc(self, sv:SinhVien):
        if (sv._diemTB >= 8):
            sv._hocLuc = "Gioi"
        elif (sv._diemTB >= 6.5):
            sv._hocLuc = "Kha"
        elif (sv._diemTB >= 5):
            sv._hocLuc = "Trung binh"
        else:
            sv._hocLuc = "Yeu"

    def showSinhVien(self, listSV):
        print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}".format("ID", "Name", "Sex", "Major", "DiemTB", "HocLuc"))
        if (listSV.__len__() > 0):
            for sv in listSV:
                print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}".format(sv._id, sv._name, sv._sex, sv._major, sv._diemTB, sv._hocLuc))
        print("\n")
    def getListSinhVien(self):
        return self.listSinhVien
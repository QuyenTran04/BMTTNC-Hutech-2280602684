from QuanLySinhVien import QuanLySinhVien
qlsv = QuanLySinhVien()
while (1==1):
    print("*********************************************************")
    print("*    1. Nhap sinh vien                                  *")           
    print("*    2. Cap nhat sinh vien                              *")
    print("*    3. Xoa sinh vien                                   *")
    print("*    4. Tim kiem sinh vien                              *")
    print("*    5. Sap xep sinh vien theo diem trung binh          *")
    print("*    6. Sap xep sinh vien theo ten chuyen nganh         *")
    print("*    7. Hien thi danh sach sinh vien                    *")
    print("*    0. Thoat                                           *")
    print("*********************************************************")
    key = int(input("Nhap lua chon: "))
    if (key == 1):
       print("\n1. Them sinh vien")
       qlsv.nhapSinhVien()
       print("Them sinh vien thanh cong")
    elif (key == 2):
        if(qlsv.soLuongSinhVien() > 0):
            print("\n2. Cap nhat sinh vien")
            ID = int(input("Nhap ID sinh vien can cap nhat: "))
            qlsv.updateSinhVien(ID)
            print("Cap nhat sinh vien thanh cong")
        else:
            print("Khong co sinh vien nao de cap nhat")
    elif (key == 3):
        if(qlsv.soLuongSinhVien() > 0):
            print("\n3. Xoa sinh vien")
            ID = int(input("Nhap ID sinh vien can xoa: "))
            if (qlsv.deleteById(ID)):
                print("Xoa sinh vien",ID, "thanh cong")
            else:
                print("Khong tim thay sinh vien co ID = {}".format(ID))
        else:
            print("Khong co sinh vien nao de xoa")
    elif (key == 4):
        if(qlsv.soLuongSinhVien() > 0):
            print("\n4. Tim kiem sinh vien theo ten")
            name = input("Nhap ten sinh vien can tim: ")
            searchResult = qlsv.findByName(name)
        else:
            print("Danh sach sinh vien rong")

    elif (key == 5):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n5. Sap xep sinh vien theo diem trung binh")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("Danh sach sinh vien rong")
    elif (key == 6):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n6. Sap xep sinh vien theo ten chuyen nganh")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("Danh sach sinh vien rong")
    elif (key == 7):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n7. Hien thi danh sach sinh vien")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("Danh sach sinh vien rong")
    elif (key == 0):
        print("Ban da thoat chuong trinh")
        break
    else:
        print("\nKhong co lua chon nay")
        print("\nHay chon chuc nang trong menu")
        
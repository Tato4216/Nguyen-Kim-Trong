# kiểm tra số nhỏ nhất
def get_max_numbers():
    numbers=[]
    try:
        # nhập chuỗi list vào và kiểm tra độ dài
        # để loại bỏ trường hợp giá trị ít hơn 2

        n = int(input(("nhap số lượng phần tử trong mảng:")))
        if n<2:
            print(" khong thể sắp xếp")
            pass
        else:
            for i in range(n):
                numbers.append(int(input("phan tu thu {}:".format(i+1))))
        # tạo 1 list sắp xếp theo giá trị tăng dần
            sapxep=numbers.copy()
            sapxep.sort()
            print(" hai gia tri lớn nhất là {},{}".format(sapxep[-2],sapxep[-1]))
    except:
        print("nhap so tu nhien")
   

if __name__ =="__main__":
    get_max_numbers()
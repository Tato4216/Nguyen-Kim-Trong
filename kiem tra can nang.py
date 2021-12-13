def kiem_tra_can_nang():
    # nhap so can nang va chieu cao
    import math
    try:
        # can nang
        cannang = float(input("nhap can nang (kg): "))
        # chieu cao
        chieucao = float(input("nhap chieu cao (m):"))
        BMI = (cannang)/(chieucao**2)
        #BMI < 16: Gầy cấp độ III
        #16 <= BMI < 17:  Gầy cấp độ II
        #17<= BMI < 18.5: Gầy cấp độ I
        #18.5 <= BMI < 25: Bình thường
        #25 <= BMI < 30: Thừa cân
        #30 <= BMI < 35 : Béo phì cấp độ I
        #35 <= BMI < 40: Béo phì cấp độ II
        #BMI > 40: Béo phì cấp độ III
        if BMI <16:
            print(" Gầy cấp độ III")
        elif 6 <= BMI < 17: 
            print(" Gầy cấp độ II")
        elif 17<= BMI < 18.5: 
            print(" Gầy cấp độ I")
        elif 18.5 <= BMI < 25: 
            print(" Bình thường")
        elif 25 <= BMI < 30: 
            print("Thừa cân")
        elif 30 <= BMI < 35 : 
            print("Béo phì cấp độ I")
        elif 35 <= BMI < 40: 
            print("Béo phì cấp độ II")
        elif BMI > 40: 
            print("Béo phì cấp độ III")
        else:
            print("nhap sai du lieu")
    except:
        print("Error, out of range")
if __name__ == "__main__":
    kiem_tra_can_nang()

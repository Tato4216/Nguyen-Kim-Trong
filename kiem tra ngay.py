def kiem_tra_ngay():
    # nhap so tu 1 den 7 de kiem tra
    
    try:
        num = int(input("nhap ngay (form 1 to 7): "))
        if num == 1:
            print("Monday")
        elif num == 2:
            print("Tuesday")
        elif num == 3:
            print("Wednesday")
        elif num == 4:
            print("Thursday")
        elif num == 5:
            print("Friday")
        elif num == 6:
            print("Saturday")
        elif num == 7:
            print("Sunday")
        else:
            # nam ngoai 1 den 7 thi bao loi
            print("Error, out of range")
    except:
        print("Error, out of range")
if __name__ == "__main__":
    kiem_tra_ngay()

# kiểm tra số nhỏ nhất
def get_min_numbers(numbers):
    # gán giá trị biến kiểm tra result cho số đầu tiên trong chuỗi
    result = numbers[0]
    for num in numbers:
        if result > num:
             result = num
    return result
# thêm giá trị vào chuỗi số
def add_item(myTempList, item):    
    myTempList.append(item)
if __name__ =="__main__":
    numbers=[]
    while True:
        print("Do you want to add numbers? -\n"
        "1. Add\n" 
        "2. No")
        try:
            option = int(input("Select option 1 or 2: "))
            # nếu là 1 {yes} thì tiếp tục thêm số vào chuỗi
            if option == 1:
                a=input("nhap so ")
                add_item(numbers,a)
                print("chuoi so ", numbers)

            # nếu là 2{no} thì thoát chuỗi nhập vào kiểm tra giá trị nhỏ nhất trong chuỗi
            elif option == 2:
                min_number = get_min_numbers(numbers)
                print("Min number: ", min_number)
                break
        except:
            print("nhap sai")
    # kiểm tra lấy số nhỏ nhất
    

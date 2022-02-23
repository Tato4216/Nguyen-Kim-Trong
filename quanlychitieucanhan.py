# hàm thêm mục chi tiêu vào mảng chi tiêu hiện tại
def add_item(myTempList, item):    
    myTempList.append(item)

# hàm xác định vị trí mục chi tiêu cần xóa
def find_index_item(myTempList, item_name):
    result = -1
    length = len(myTempList)
    for i in range(length):
        if myTempList[i]['name'] == item_name:
            result = i
    return result

# hàm xóa mục chi tiêu theo yêu cầu
def remove_item(myTempList, item_name):
    if find_index_item(myTempList, item_name) > -1:
        del myTempList[find_index_item(myTempList, item_name)]
    else:
        print(item_name + " not in list")
# nhập chuỗi giá trị thu chi

if __name__ == "__main__":
    # nhập danh sách có sẵn
    myitemlist= [{'name':'cafe','cost':600,'date':'20/11/2021'},
    {'name':'shopping','cost':700,'date':'12/6/2021'},
    {'name':'camping','cost':400,'date':'30/10/2021'}]
    print("your item list: ",myitemlist)
    while True:
        print("what do you do? \n"
            "1. add \n "
            "2.remove")
        option=int(input("select 1 or 2: "))
        name_input = input("input name:")
        # bằng 1 thì thêm list vào mảng thu chi
        if option ==1:
            cost_input = int(input("item cost: "))
            date_input = input("date :")
            item = {'name':name_input,"cost":cost_input,"date":date_input}
            add_item(myitemlist,item)
            print("your item list: ",myitemlist)
        # bằng 2 thì xóa list trong mảng thu chi
        elif option ==2:
            remove_item(myitemlist,name_input)
            print(" your item list",myitemlist)
        # nhập sai thì hiển thị lỗi
        else:
            print("input invalid")
    

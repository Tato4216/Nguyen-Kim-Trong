#from pyrsistent import b
product_db  = {
            1: 'xà phòng',
            2: 'nước ngọt' ,
            3: 'sữa tắm ',
            4: 'dầu gội' ,
            5: 'dầu xả',
            6: 'thuốc'  
           }
def thongbao():
    print(" các thao tác")
    print("[1] hiển thị sản phẩm")
    print("[2] cập nhật sản phẩm")
    print("[3] xóa sản phẩm")
    print("[4] kết thúc chương trình")
    print("[5] hiển thị danh sách")
    
def id_product (id_prod,*args:dict):
    for key,values in product_db.items():
        if key < id_prod:
            continue
        elif key>id_prod:
            print("Không tìm thấy sản phẩm với id: {}".format(id_prod))
            break
        else:
            return values
def update_product(id_prod, name_prod,*args:dict):
    upprod = {id_prod:name_prod}
    for key,values in product_db.items():
        if key == id_prod:
            values  = name_prod
        else:
            product_db.update(upprod)
            break
if __name__ == "__main__":
    print(product_db)
    thongbao()
    while True:
        option = int(input("Enter your choice: "))
        if option == 1:
            product_id = int(input("Nhập id: "))
            print(id_product(product_id,product_db))
        elif option ==2:
            product_id = int(input("Nhập id: "))
            product_name= str(input("Nhập tên sản phẩm:"))
            update_product(product_id,product_name,product_db)
            print(product_db)
        elif option ==3:
            product_id = int(input("Nhập id: "))
            if id_product(product_id):
                del product_db[product_id]
                print("Xóa thành công")
            else:
                print("Product doesn't exist")
        elif option==4:
            print("Chương trình kết thúc")
            break
        elif option == 5:
            print(product_db)
        else:
            print("Error")

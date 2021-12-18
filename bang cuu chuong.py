def bangcuuchuong():
    # nhap bien chay i, j cho so trong bang cuu chuong
    for i in range(1,10):
        for j in range (1,10):
            # hien ket qua nhan bang cuu chuong
            print(str(i)+' x '+str(j)+' = '+str(i*j))
if __name__ == "__main__":
    bangcuuchuong()
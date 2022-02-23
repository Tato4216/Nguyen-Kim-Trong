def doitien():
    import math
    a = float(input(" nhập gía tiền tệ USD: "))
    b = float(input("nhập tỉ giá quy đổi 1 USD sang VND: "))
    c = a *b
    print(" giá tiền tệ VND là ",c)
if __name__ == "__main__":
    doitien()

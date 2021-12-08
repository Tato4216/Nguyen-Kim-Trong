def nhiet():
    import math
    # nhập nhiệt độ C
    co = float(input(" nhiet do C : "))
    # tính đổi sang độ F
    fo = ( 9 * co / 5 ) + 32
    # hiện giá trị nhiệt độ F
    print(" nhiet do F: ", fo)
if __name__ == "__main__":
    nhiet()
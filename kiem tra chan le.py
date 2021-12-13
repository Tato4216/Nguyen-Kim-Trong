num_check=float(input("nhap so"))
msg=""
# kiem tra xem co la so nhien
msg = "so chan" if num_check %2 == 0 else "so le" if num_check % 2 ==1 else "khong la so tu nhien"
print(msg)

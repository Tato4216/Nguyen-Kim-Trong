num_check=int(input("nhap so"))
msg=""
# toan tu 3 ngoi
msg = "chia het" if num_check %2 == 0 else "khong chia het"
print(msg)

# if else thong thuong
msg = ""
if(num_check%2  == 0):
    msg = "chia het"
else:
    msg = "khong chia het"
print(msg)

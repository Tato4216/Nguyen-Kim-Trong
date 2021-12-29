# cách 1 dùng hàm để đếm từng phần tử trong chuỗi nhập vào
def count_chars(txt):
    result = 0
    for i in txt:
        result += 1
    return result
input_str = input('Your string: ')
# cách 2 dùng hàm len để đếm độ dài của chuỗi
length=len(input_str)
#Bước 3: Gọi hàm đếm và in ra kết quả cho người dùng

print('Length: ', count_chars(input_str))
print(length)

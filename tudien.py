ds ={'school':'trường học',
         'love':'tình yêu',
         'day':'ngày',
         'house':'ngôi nhà'
         }
input_word =input("từ cần dịch là: ")

def transalte(ds,tu_nhap):
    if tu_nhap in ds.keys():
        print ("nghĩa của từ là:",ds[tu_nhap])
    else:
        print ( "chưa có nghĩa trong từ điển")
if __name__ == "__main__":
    transalte(ds,input_word)

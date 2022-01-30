file = input ("nhap file: ")
path= "D:\\classpython\\Nguyen-Kim-Trong-1\\" 
pathFile =path + file
try:
    fPath = open(pathFile)
except:
    print("file is not avalible")
    exit()

counts = dict()
for line in fPath:
    words = line.split()
    for word in words:
        if word not in counts:
             counts[word]=1
        else:
            counts[word] +=1
print(counts)
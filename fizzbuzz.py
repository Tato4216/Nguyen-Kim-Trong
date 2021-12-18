def fizzbuzz():
    try:
        num1=int(input("nhap so bat ki 1: "))
        num2=int(input("nhap so bat ki 2: "))
        if num2 < num1 :
            print ("so sau can lon hon so dau")
        else:
            for i in range(num1,num2+1):
                if i%3 ==0 and i % 5==0:
                    print("fizzbuzz")
                elif i%3 ==0:
                    print("fizz")
                elif i%5 ==0:
                    print("buzz")
                else:
                    print(str(i))
    except:
        print ("nhap sai du lieu")
if __name__ == "__main__":
    fizzbuzz()
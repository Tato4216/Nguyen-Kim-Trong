def sort_numbers(num1,num2,num3):
    temp=0
    # nếu 2 nhỏ hơn 1 và 3 thì đổi 2 với 1 ( 2 lên đầu)
    if num2 < num1 and num2 < num3:
        temp = num1
        num1 = num2
        num2 = temp
    # nếu 3 nhỏ hơn 1 và 2 thì đổi chỗ 1 và 3 ( 3 lên đầu)
    elif num3 < num1 and num3 < num2:
        temp = num1
        num1 = num3
        num3 = temp 
    # so sánh 2 và 3 để đổi chỗ 
    if num3 < num2:
        temp = num2
        num2 = num3
        num3 = temp
    return (num1,num2,num3)
if __name__ == "__main__":
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    z = int(input("Enter third number: "))
    a, b, c = sort_numbers(x, y, z)
    print("Original numbers: ", x, y, z)
    print("Sorted numbers: ", a, b, c)
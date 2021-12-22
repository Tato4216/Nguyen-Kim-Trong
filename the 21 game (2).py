def game21():
    import random as rd
    while True:
        current_number = 0
        turn = rd.randint(0,1)
        # luot choi dau ngau nhien giua may tinh hoac con nguoi
        if turn==0:
            current_player = 'human'
        elif turn==1:
            current_player='computer'
        while int(current_number) < 21:
            # hien diem hien tai
            print('Điểm hiện tại: '+str(current_number))
            # luot choi cua con nguoi
            if current_player =='human':
                while True:
                    # nhap gia tri chon cua con nguoi va neu khong trong [1,2,3] thi yeu cau nhap lai
                    player_choice = int(input('Nhập điểm thêm: '))
                    if player_choice > 0 and player_choice <4:
                        break
                    else: 
                        print("yeu cau nhap lai")
                # tang gia tri bien dem tong 21
                current_number += player_choice
                # kiem tra gia tri bien dem tong 21
                if current_number >=21:
                    print(str(current_number) + ' You lost')
                else:
                    current_player = 'computer'  
                    # chuyen sang luot cua may tinh 
            else: 
                current_player ='computer'
                # gia tri chon ngau nhien
                computer_choice = rd.randint(1,3)
                print('Điểm máy thêm: '+str(computer_choice))
                current_number += computer_choice
                # kiem tra gia tri bien dem tong 21
                if current_number >=21:
                    print(str(current_number)+' You win')
                else:
                    current_player='human'
        # hoi xem co choi lai ko
        play_again = str(input('Play again?(y/n)'))
        if play_again[0] == 'y':
            continue
        else:
            break
if __name__ == '__main__':
    game21()
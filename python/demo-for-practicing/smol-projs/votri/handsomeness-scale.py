# Đừng code khi buồn ngủ, nhìn vô tri vc
import time

print('THƯỚC ĐỌ ĐỘ ĐẸP TRAI')
time.sleep(1)


def most_handsome_guy(handsome_record):
    """Cuộc cạnh tranh nhan sắc gay gắt giữa các anh trai"""
    handsomest_score = 0
    for handsome_guy in handsome_record:
        handsome_amount = handsome_record[handsome_guy]
        if handsome_amount > handsomest_score:
            handsomest_score = handsome_amount
            winner = handsome_guy
    print(f'\nChúc mừng {winner}!\nCậu là người đẹp trai nhất với độ đẹp trai {handsomest_score}/100!')


retry = True
while retry:
    handsomeness = {}
    name = input('Anh tên là gì?\n')
    retry_scale = True
    while retry_scale:
        handsome_score = int(input('Trên thang từ 0 đến 100, anh nghĩ anh đẹp trai bao nhiêu điểm?\n'))
        if handsome_score < 0:
            print('Ánh biết bạn đẹp trai mà, làm gì tự ti thế ba?\nSuy nghĩ lại lần nữa đi\n')
            time.sleep(1)
            retry = True
        elif handsome_score > 100:
            print('Ánh biết là bạn đẹp trai, nhưng mà tự tin quá vậy ba :))\nChọn lại một cách trung thực đi.\n')
            time.sleep(1)
            retry = True
        else:
            retry_scale = False
            handsomeness[name] = handsome_score
            should_continue = input('Còn ai muốn đọ nhan sắc không? (Nhập Y/N)\n').lower()
            if should_continue == 'y':
                print("ANH TIẾP THEO!")
                time.sleep(0.5)
            elif should_continue == 'n':
                print('...Đang cạnh tranh sắc đẹp giữa các anh...')
                time.sleep(2)
                most_handsome_guy(handsomeness)
                time.sleep(2)
                retry_whole_ask = input('Bạn muốn đo lại nhan sắc? (Y/N)\n').upper()
                if retry_whole_ask == 'N':
                    retry = False
                    print('Hẹn mấy anh trai đẹp lần sau nhá! :>')
#Đừng có nạp men khi code, please, không vô tri lắm!

import random
import time


input('Nhấn nút Enter để bắt đầu chơi!')
while True:
    money = random.randint(10, 900)
    print('Bạn muốn mua pet?')
    time.sleep(1)
    print(f'Giả sử bạn đang có số tiền: {money}$.\nHãy mua con pet với tất cả số tiền mình có!\n')
    time.sleep(1)

    row1 = ['🐛','🐍','🐞']
    row2 = ['🦨','🐅','🐊']
    row3 = ['🐉','🦖','🐼']
    choice = [row1, row2, row3]
    print(f'{row1}\n{row2}\n{row3}')
    item = input('\nHãy chọn toạ độ bé pet mà bạn muốn? (VD: Toạ độ (2;3) thì nhập 23)\n')

    horizontal= int(item[1])
    vertical = int(item[0])
    pet = str(choice [horizontal - 1] [vertical - 1])

    print(f'Bạn đã mua bé {pet}!')
    time.sleep(1)

    price = random.randint(20, 400)
    print(f'Một bé {pet} có giá {price}$!')
    time.sleep(2)
    if money >= price:
        quantity = money // price
        net = price * quantity
        left = money - net

        print(f'{money}$ là đủ để mua {quantity} bé {pet}!')

        if left == 0:
            print(f'Và vừa đủ xài hết luôn!\n')
        else:
            print(f'Và còn dư tận {left}$!\n')

        time.sleep(1)
        print(f'Chi phí tổng cộng là {net}$!')
        time.sleep(1)
        while True:
            confirm = input('Bạn có chắc chắn muốn thanh toán? (Y/N)\n')
            if confirm.lower().startswith('y'):
                break

        print('ĐANG TRẢ TIỀN')
        time.sleep(1)
        for i in range (1,4):
            print('💰'* i )
            time.sleep(1)
        print('ĐANG IN BIÊN LAI')
        time.sleep(1)
        for k in range (3,0,-1):
            print('🧾' * k)
            time.sleep(1)
        print('Đây là các bé pet của bạn!')
        time.sleep(1)
        print(f'{pet}' * quantity)
        print('Cảm ơn bạn vì đã mua hàng!')

        var = input('Bạn có muốn thử mua lại? (Y/N)\n')
        if var.lower().startswith('n'):
            print('Bye! Khi nào có tiền rồi quay lại!')
            break

    else:
        print('Bạn đã bị đuổi khỏi shop do nghèo!')
        time.sleep(2)
        var = input('Bạn có muốn thử mua lại? (Y/N)\n')
        if var.lower().startswith('n'):
            print('Bye! Khi nào có tiền rồi quay lại!')
            break




import random
import time

input('Nhấn Enter để bắt đầu dùng!')
print('Đặt tên cho con không còn là vấn đề trăn trở nữa với...')
time.sleep(1)
print('Công cụ đặt tên con do Ánh tạo ra!')
time.sleep(1)
while True:
    a = ['a', 'e', 'i', 'o', 'u']
    b = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n'
         'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    c = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N',
         'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
    length = int(input('Bạn muốn tên con bạn dài bao nhiêu âm tiết?\n'))
    print('Đang tạo tên, đợi xíu nhé :>\n')
    time.sleep(0.5)
    if length < 7:
        name = ""
        for char in range (1, length + 1):
            name += random.choice(c)
            name += random.choice(a)
            name += random.choice(b)
        print(f'Tên của con bạn là {name}!\n\nMột cái tên rất tuyệt vời!\n')
        time.sleep(1)

        nickname = int(input('Bạn muốn thêm bao nhiêu ký tự nhảm nhí vào tên con bạn?\n'))
        if -1 < nickname < 10:
            begin_letter = random.choice(c)
            b.extend(a)

            name_list = []
            for char in range (1, nickname):
                name_list += random.choice(b)
            random.shuffle(name_list)
            shit = ''
            for char in name_list:
                shit += char
            print('Tên đầy đủ của con bạn là ' + name + ' ' + begin_letter + shit + '!\n\nMột cái tên rất tuyệt vời!')
        else:
            print(f'Khỏi ký tự nhảm nhí đi, dài quá!\nTên con bạn là {name} là đủ rồi.')
    else:
        print('Tên gì dài thế? Bớt làm khổ con bạn đi.')

    var = input('Bạn có muốn chọn lại tên? (Y/N)\n')
    if var.lower().startswith('n'):
        print('Bye! Khi nào có thêm đứa nữa thì quay lại chọn tên!')
        break

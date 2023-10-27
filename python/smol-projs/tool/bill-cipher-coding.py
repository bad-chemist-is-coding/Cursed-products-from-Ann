#Tool này để giải hoặc tự tạo các mã giống các loại mã thường thấy trong Gravity Falls
import time
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'
            , 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x'
            , 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'
            , 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x'
            , 'y', 'z']
num1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13',
        '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26']
num2 = [' 1', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9', ' 10', ' 11', ' 12', ' 13',
        ' 14', ' 15', ' 16', ' 17', ' 18', ' 19', ' 20', ' 21', ' 22', ' 23', ' 24', ' 25', ' 26']
print('TOOL GIẢI MÃ/ DỊCH MÃ GRAVITY FALLS\n')
time.sleep(0.5)
print('Hỡi thần dân Gravity Falls, bộ máy giải mã các loại mã của Gravity Falls đã xuất hiện!')
time.sleep(1)

# CÁC HÀM CỦA CÁC MÃ
def caesar(start_text_a, shift_amount_a, direction_a):
    end_text_a = ''
    if direction_a == 'B':
        shift_amount_a *= -1
    for char in start_text_a:
        if char in alphabet:
            position_a = alphabet.index(char)
            new_position_a = position_a + shift_amount_a
            end_text_a += alphabet[new_position_a]
        else:
            end_text_a += char
    if direction_a == 'B':
        print(f'Mã của bạn sau khi bị mã hoá là {end_text_a}\n')
    if direction_a == 'A':
        print(f'Mã của bạn dịch ra là {end_text_a}\n')
def atbash(start_text_b, direction_b):
    end_text_b = ''
    for char in start_text_b:
        if char in alphabet:
            position_b = alphabet.index(char)
            new_position_b = position_b + (25 - 2 * position_b)
            end_text_b += alphabet[new_position_b]
        else:
            end_text_b += char
    if direction_b == 'B':
        print(f'Mã của bạn sau khi bị mã hoá là {end_text_b}\n')
    if direction_b == 'A':
        print(f'Mã của bạn dịch ra là {end_text_b}\n')
def a1z26(start_text_c, direction_c):
    end_text_c = ''
    if direction_c == 'A':
        for char in start_text_c:
            if char in num1:
                position = num1.index(char)
                end_text_c += alphabet[position]
            else:
                end_text_c += char
        print(f'Mã của bạn dịch ra là {end_text_c}\n')
    elif direction_c == 'B':
        for char in start_text_c:
            if char in alphabet:
                position = alphabet.index(char)
                end_text_c += num2[position]
            else:
                end_text_c += char
        print(f'Mã của bạn sau khi bị mã hoá là {end_text_c}\n')


retry = True
while retry:
    code_type = input('Bạn muốn dùng loại mã nào sau đây?\nA. Caesar                B. Atbash\nC. A1Z26                 D. Vigenere\n').upper()

    #   I. Mã Caesar:
    # Thế chữ cái gốc ban đầu bằng chữ cái thứ 3 đằng trước nó.
    retry_a = True
    if code_type == 'A':
        print('\nMã Caesar dùng cách thế chữ cái gốc ban đầu bằng chữ cái thứ 3 đằng trước nó.\n')
        while retry_a:
            dic = input('Bạn muốn giải mã (A) hay mã hoá (B)?\n').upper()
            text_a = input('Nhập nội dung của bạn (Nếu tiếng việt thì không dấu. VD: Toi yeu Bach Khoa)\n').lower()
            caesar(start_text_a=text_a, shift_amount_a=-3, direction_a=dic)

            troll = True
            while troll:
                ask_retry = input('Bạn có muốn:\nA. Thử lại mã Caesar\nB. Thử mã khác\nC. Dẹp luôn vụ mã để ngủ\n').upper()
                if ask_retry == 'A':
                    troll = False
                    retry_a = True
                if ask_retry == 'B':
                    troll = False
                    retry_a = False
                    retry = True
                if ask_retry == 'C':
                    retry_a = False
                    time.sleep(0.5)
                    print('Tôi biết bạn muốn thử lại mà :)\n')
                    time.sleep(0.5)
                    retry = False

    #   II. Mã Atbash:
    # Đổi vị trí các chữ cái, ví dụ ở đây là chữ A thành chữ Z
    retry_b = True
    if code_type == 'B':
        print('\nMã Atbash dùng cách đảo lộn vị trí các chữ cái, ví dụ ở đây là chữ A thành chữ Z.\n')
        while retry_b:
            dic = input('Bạn muốn giải mã (A) hay mã hoá (B)?\n').upper()
            text_b = input('Nhập nội dung của bạn (Nếu tiếng việt thì không dấu. VD: Toi yeu Bach Khoa)\n').lower()
            atbash(start_text_b=text_b, direction_b=dic)

            troll = True
            while troll:
                ask_retry = input(
                    'Bạn có muốn:\nA. Thử lại mã Atbash\nB. Thử mã khác\nC. Dẹp luôn vụ mã để ngủ\n').upper()
                if ask_retry == 'A':
                    troll = False
                if ask_retry == 'B':
                    troll = False
                    retry_b = False
                    retry = True
                if ask_retry == 'C':
                    retry_b = False
                    time.sleep(0.5)
                    print('Tôi biết bạn muốn thử lại mà :)\n')
                    time.sleep(0.5)
                    retry = False

    #   III. Mã A1Z26:
    # Giải các dãy số: chữ số n tương ứng với chữ cái thứ n trong bảng chữ cái tiếng Anh.
    retry_c = True
    if code_type == 'C':
        print('\nMã A1Z26 giải mã các dãy số theo quy luật chữ số n tương ứng với chữ cái thứ n.\n')
        while retry_c:
            dic = input('Bạn muốn giải mã (A) hay mã hoá (B)?\n').upper()
            text_c = ''
            if dic == 'A':
                text_c = input('Nhập dãy số mật mã của bạn? (Ví dụ nhập "3 10 20 4")\n').split(' ')
            else:
                text_c = input('Nhập nội dung của bạn (Nếu tiếng việt thì không dấu. VD: Toi yeu Bach Khoa)\n').lower()

            a1z26(start_text_c=text_c, direction_c=dic)

            troll = True
            while troll:
                ask_retry = input(
                    'Bạn có muốn:\nA. Thử lại mã A1Z26\nB. Thử mã khác\nC. Dẹp luôn vụ mã để ngủ\n').upper()
                if ask_retry == 'A':
                    troll = False
                    retry_c = True
                if ask_retry == 'B':
                    troll = False
                    retry_c = False
                    retry = True
                if ask_retry == 'C':
                    retry_c = False
                    time.sleep(0.5)
                    print('Tôi biết bạn muốn thử lại mà :)\n')
                    time.sleep(0.5)
                    retry = False

    #IV. Mã Vigenere:
    # Bộ giải mã nối tiếp của Caesar, nhưng các chữ cái sẽ phụ thuộc vào 1 từ khóa nhất định.
    if code_type == 'D':
        print('Mã Vigenere là bộ giải mã nối tiếp của Caesar, nhưng các chữ cái '
              'sẽ phụ thuộc vào 1 từ khóa nhất định.\n')
        time.sleep(2)
        print('Nói chứ bảng mã này hơi phức tạp, trình Ánh chưa đủ tới nên chưa làm được tool '
               'giải mã cho mã Vigenere này...Ehe :)\n')
        time.sleep(3)
        troll = True
        while troll:
            ask_retry = input('Bạn muốn:\nA. Thử các mã khác\nB. Dẹp luôn vụ mã để ngủ\n').upper()
            if ask_retry == 'A':
                troll = False
            if ask_retry == 'B':
                time.sleep(1)
                print('Tôi biết bạn muốn thử lại mà :)\n')
                time.sleep(1)

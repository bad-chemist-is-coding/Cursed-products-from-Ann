import random
import time

print('ĐOÁN TUỔI NGƯỜI BẠN DATE\n')
input('Nhấn Enter để bắt đầu.')

EZ = 10
HARD = 5
ASIAN_MODE = 2


def difficulty():
    dif = input('Chọn độ khó:\nA. Dễ                     B. Khó                 C. Asian mode ☠️\n').lower()
    if dif == 'a':
        return EZ
    elif dif == 'b':
        return HARD
    else:
        return ASIAN_MODE


def age_check(date_name, attempt, true_age):
    again = True
    while again:
        your_guess = int(input('👉 Tuổi bạn đoán: '))
        if your_guess == true_age:
            again = False
            print('\n🟩 Bạn đã đoán đúng tuổi! Xin chúc mừng 🥳')
            time.sleep(2)
            print('...hoặc không... ☠️')
        elif attempt == 1:
            again = False
            print(f'\n🟥 Bạn đã đoán trật hết tuổi!\nTuổi thật của {date_name} là {true_age}! 🤭')
            time.sleep(1)
            print('\nCó đoán tuổi mà cũng không làm được thì sao chinh phục được người ta?? 💔')
        elif 101 > your_guess > true_age:
            attempt -= 1
            print(f'\nRõ ràng là {date_name} trẻ hơn mà, sao bạn đoán già thế? 👶\nBạn còn {attempt} lần đoán tuổi nữa.\n')
        elif 0 < your_guess < true_age:
            attempt -= 1
            print(f'\nNhìn {date_name} trẻ đến vậy sao?? Thật ra là già hơn đó. 👩‍🦳👨‍🦳\nBạn còn {attempt} lần đoán tuổi nữa.\n')
        else:
            again = False
            print(f'\nNghĩ sao mà {date_name} {your_guess} tuổi lận thế? 😱\n{date_name} đã giận bỏ về. 😤\nBạn đã thua trong đường tình.')


reset = True
while reset:
    name = str(input('\nTên người bạn muốn hẹn hò?\n').capitalize())
    print(f'\nBạn đang hẹn hò với {name} qua ứng dụng hẹn hò nhưng không biết tuổi của họ.')
    time.sleep(0.5)
    print('Ngày gặp mặt, bạn quyết định đoán tuổi của họ.')
    time.sleep(0.5)

    real_age = random.randint(0, 101)
    guess_attempt = difficulty()
    print(f'Bạn có {guess_attempt} lần đoán tuổi của {name}!')
    print(f'Tuổi của {name} dao động từ 0 đến 100 tuổi\n')

    age_check(date_name=name, attempt=guess_attempt, true_age=real_age)
    should_reset = input('\nBạn muốn đi hẹn hò lại với người khác? (Y/N)\n').lower()
    if should_reset == 'n':
        reset = False
        print('Chúc bạn sớm có bồ! ❤️')

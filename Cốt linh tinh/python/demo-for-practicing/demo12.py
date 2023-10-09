import random
import time

print('Project: Number Guessing game')

EASY = 10
DIF = 5


def difficulty():
    lvl = input('Chọn độ khó:\nA. Dễ                          B. Khó\n').upper()
    if lvl == 'A':
        return EASY
    if lvl == 'B':
        return DIF


def num_checking(num, attempt):
    check_again = True
    while check_again:
        guessing = int(input('Chọn số của bạn: '))
        if guessing == num:
            check_again = False
            print('Giỏi ghê ta\n')
        elif attempt == 0:
            check_again = False
            print(f'Thua rồi. Số của Ánh là {num}\n')
        elif -1 < guessing < num:
            attempt -= 1
            print(f'Thấp quá, bạn còn {attempt} lần đoán.\n')
        elif 101 > guessing > num:
            attempt -= 1
            print(f'Cao quá, bạn còn {attempt} lần đoán.\n')

        else:
            check_again = False
            print('Số lạ quá, nghỉ chơi đi\n')


def game():
    reset = True
    while reset:
        ann_number = random.randint(1, 101)
        guess_attempt = difficulty()
        print(f'Bạn có {guess_attempt} lần để đoán.\n')
        time.sleep(0.5)
        print('Ánh đang nghĩ về 1 số từ 0 đến 100. Đoán đi!\n')
        num_checking(num=ann_number, attempt=guess_attempt)
        ask_restart = input('Bạn muốn thử lại? (Y/N)\n').lower()
        if ask_restart == 'n':
            print('Bye!')
            reset = False


game()

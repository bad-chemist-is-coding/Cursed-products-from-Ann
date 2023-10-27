import time
import random
from who_is_more_popular_data import data

print('AI CÓ NHIỀU FOLLOWER TRÊN INSTAGRAM HƠN??')
input('Nhấn ENTER để bắt đầu chơi')

print('\nGhi 10 điểm để chiến thắng trò chơi')
time.sleep(1)


def define_data(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name} là {account_description} đến từ {account_country}"


def check_ans(guessing, fol_acc_a, fol_acc_b):
    if fol_acc_a > fol_acc_b:
        return guessing == 'a'
    else:
        return guessing == 'b'


retry = True
while retry:
    score = 0
    cont = True
    while cont:
        account_a = random.choice(data)
        account_b = random.choice(data)
        if account_a == account_b:
            account_b = random.choice(data)
        if score == 10:
            cont = False
            print('\n🟩🟩 Thật ghê gớm, bạn đã phá đảo trò chơi vô tri này. 🥳')
            time.sleep(1)
            ask = input("🤩 Bạn muốn thử lại? (Y/N)").lower()
            if ask == "n":
                retry = False
                cont = False
                print('👋 Mốt rảnh ghé chơi! 👋')
        print(f"\n❤️ Hãy so sánh ❤️\n📍 Tài khoản Instagram A của {define_data(account_a)}")
        print("                       vs")
        print(f"📍 Tài khoản Instagram B của {define_data(account_b)}")

        guess = input("👉 Tài khoản bạn đoán là (Nhập A/B): ").lower()

        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]

        correct_ans = check_ans(guessing=guess, fol_acc_a=a_follower_count, fol_acc_b=b_follower_count)

        if correct_ans:
            score += 1
            print(f'\n🟩 Giỏi quá ta! Đoán đúng òi, bạn có {score} điểm hiện tại 😱')
            time.sleep(1)
        else:
            cont = False
            print(f'\n🟥 Đoán trật òi, bạn đã dừng cuộc chơi với {score} điểm')
            time.sleep(1)
            ask = input("🤩 Bạn muốn thử lại? (Y/N)\n").lower()
            if ask == "n":
                retry = False
                cont = False
                print('👋 Mốt rảnh ghé chơi! 👋')

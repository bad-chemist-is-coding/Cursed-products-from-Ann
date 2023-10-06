import random
import time

# Code này hơi lỏ do Ánh chưa quen tối ưu hoá code :))

input('♠ Nhấn Enter để bắt đầu đấu Xì Ách với Ánh ♣\n(nếu bạn không sợ thua 😼)')


def deal_cards():
    """Bóc ngẫu nhiên lá bài"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
             11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
             11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
             11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, ]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    elif (10 not in cards and 9 not in cards and 8 not in cards and 7 not in cards and 6 not in cards
          and 5 not in cards and 4 not in cards and 3 not in cards and 2 not in cards and len(cards) == 2):
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare1(player_score, ann_score):
    if player_score > 21 and ann_score > 21:
        return "🟦 Ánh đã quắc, và bạn cũng vậy, cả hai đều thua nhé ☺️"
    elif player_score == ann_score:
        return "🟦 Bạn và Ánh cùng non, huề nhé 😘"
    elif player_score == 0:
        return "🟦 Ghê, Xì trùm luôn ta, dữ luôn ha 🙂"
    elif ann_score == 0:
        return "🟥 Gọi Ánh là Xì Trum hiền vì Ánh là Xì Trùm 😏"
    elif player_score < 22 and len(player_cards) == 5:
        return "🟩 Cứ ngỡ là bạn ngủ luôn mà ai dè Ngũ linh hén. 😬"
    elif ann_score < 22 and len(ann_cards) == 5:
        return "🟥 Hehe, Ánh Ngũ linh, còn bạn ngủ luôn. 🤡"
    elif player_score < 16 and player_score != 0:
        return "🟥 Đã non rồi còn không rút thêm, bạn thua rồi 😋"
    elif player_score > 21:
        return "🟥 Hahahahaha, quắc cần câu! 🥱"
    elif ann_score > 21:
        return "🟩 Ánh là quắc, còn bạn là nhất, được chưa? 🙃"
    elif player_score > ann_score:
        return "🟩 Thắng luôn ta, chúc mừng. 😐"
    elif player_score < ann_score:
        return "🟥 Đoán xem ai là con gà nào? 🐤"


def compare2(player_score, ann_score, final_result):
    if player_score == 0:
        final_result += 2
        return final_result
    elif ann_score == 0:
        final_result += -2
        return final_result
    elif player_score < 22 and len(player_cards) == 5:
        final_result += 2
        return final_result
    elif ann_score < 22 and len(ann_cards) == 5:
        final_result += -2
        return final_result
    elif ann_score > 21 and player_score > 21:
        return final_result
    elif player_score < 16 and player_score != 0:
        final_result += -1
        return final_result
    elif player_score > 21:
        final_result += -1
        return final_result
    elif ann_score > 21:
        final_result += 1
        return final_result
    elif player_score > ann_score:
        final_result += 1
        return final_result
    elif player_score < ann_score:
        final_result += -1
        return final_result
    else:
        return final_result


def compare3(final_result, final_candy):
    if final_result == -2:
        final_candy = money - 2 * bet_value[bet1]
        return int(final_candy)
    elif final_result == +2:
        final_candy = money + 2 * bet_value[bet1]
        return int(final_candy)
    elif final_result == -1:
        final_candy = money - bet_value[bet1]
        return int(final_candy)
    elif final_result == 1:
        final_candy = money + bet_value[bet1]
        return int(final_candy)
    else:
        return int(final_candy)


def bet_result(final_of_final_result, last_final_candy):
    if final_of_final_result == -2:
        return print(f'\nBạn thua đậm mất {2 * bet_value[bet1]} viên kẹo và còn {last_final_candy} viên trong túi. 😱')
    elif final_of_final_result == +2:
        return print(f'\nBạn thắng đậm thêm {2 * bet_value[bet1]} viên kẹo và có {last_final_candy} viên trong túi. 😳')
    elif final_of_final_result == -1:
        return print(f'\nBạn thua mất {bet_value[bet1]} viên kẹo và còn {last_final_candy} viên trong túi. 🤏')
    elif final_of_final_result == 1:
        return print(f'\nBạn thắng thêm {bet_value[bet1]} viên kẹo và có {last_final_candy} viên trong túi. 😮')
    else:
        return print(f'\nBạn chẳng mất hay thêm viên kẹo nào cả nên vẫn có {last_final_candy} viên kẹo trong túi.')


def ask_sure_again():
    sure_again = True
    while sure_again:
        should_again = input(
            'Bạn muốn đấu lại chứ 😇 (Ánh sẽ xoá nợ và cho bạn reset lại số viên kẹo)? (Y/N)\n').lower()
        if should_again == 'n':
            print('\nÁnh biết bạn muốn chơi lại với Ánh mà 😍')
            reset_game = True
        if should_again == 'y':
            sure_again = False


reset_game = True

while reset_game:
    money = random.randint(1, 24)

    again_again = True
    while again_again:
        print('♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠')
        print(f'🍬 Túi bạn hiện có {money} viên kẹo 🍬')
        time.sleep(1)

        bet1 = input('Bạn muốn đánh đổi bao nhiêu viên kẹo?\nA. 25 viên kẹo                B. 50 viên kẹo\n'
                     'C. 75 viên kẹo                D. 100 viên kẹo\n').lower()
        bet_value = {'a': 25, 'b': 50, 'c': 75, 'd': 100}
        print(f'Bạn đã liều mình cược {bet_value[bet1]} viên kẹo! Dù túi chưa chắc đủ. 😃')
        time.sleep(0.5)
        print('\nBắt đầu nè.')
        time.sleep(0.5)

        player_cards = []
        ann_cards = []
        game_over = False

        for _ in range(2):
            player_cards.append(deal_cards())
            ann_cards.append(deal_cards())

        while not game_over:
            player_score = int(calculate_score(player_cards))
            ann_score = int(calculate_score(ann_cards))
            print(f"\nÁnh spoil nhẹ lá bài đầu tiên của Ánh nè: {ann_cards[0]} 😉")
            print(f"Bài của bạn là: {player_cards}\nTuổi hiện tại của bạn là: {player_score}\n")

            if player_score == 0 or ann_score == 0:
                game_over = True
            elif len(player_cards) == 5:
                game_over = True
            else:
                player_deal = input('👉 Bạn muốn rút thêm lá nữa? (Y/N)\n').lower()
                if player_deal == 'y':
                    player_cards.append(deal_cards())
                    game_over = False
                if player_deal == 'n' and len(player_cards) == 4:
                    sure = input('Rút thêm 1 lá nữa để Ngũ linh đi...hoặc ngủ luôn.💀 (Y/N)\n').lower()
                    if sure == 'n':
                        game_over = True
                    elif sure == 'y':
                        player_cards.append(deal_cards())
                        game_over = False
                if player_deal == 'n' and len(player_cards) == 3:
                    sure = input('Rút thêm lá nữa đi. Ánh biết bạn muốn rút thêm mà😏 (Y/N)\n').lower()
                    if sure == 'n':
                        game_over = True
                    elif sure == 'y':
                        player_cards.append(deal_cards())
                        game_over = False
                if player_deal == 'n' and len(player_cards) == 2:
                    sure = input('Định dằn non à? Rút thêm lá nữa đi. Bạn sợ à?😏 (Y/N)\n').lower()
                    if sure == 'y':
                        player_cards.append(deal_cards())
                        game_over = False
                    elif sure == 'n':
                        game_over = True

        while ann_score != 0 and ann_score < 17:
            ann_cards.append(deal_cards())
            ann_score = calculate_score(ann_cards)

        print(
            f"💅💅💅💅💅💅💅💅\nBộ bài cuối cùng của bạn là: {player_cards}\nTuổi cuối cùng của bạn là: {player_score}\n💅💅💅💅💅💅💅💅")
        time.sleep(1)
        print('\n👉Ánh đang khéo léo rút bài.👈\n')
        time.sleep(2)
        print(
            f"😼😼😼😼😼😼😼😼\nÁnh đã khoe toàn bộ bài là: {ann_cards}\nTuổi cuối cùng của Ánh là: {ann_score}\n😼😼😼😼😼😼😼😼\n")

        print(compare1(player_score, ann_score, ))
        result = 0
        last_final_result = compare2(player_score, ann_score, final_result=result)
        final_of_final_candy = int(compare3(final_result=last_final_result, final_candy=money))
        bet_result(final_of_final_result=last_final_result, last_final_candy=final_of_final_candy)
        time.sleep(0.5)
        if final_of_final_candy > 0:
            print(f'Bạn làm Ánh càng muốn bòn rút hết kẹo của bạn. 🙇‍♀️')
            ask_again_again = input('\nBạn muốn đấu tiếp với số kẹo hiện có? (Y/N)\n').lower()
            money = final_of_final_candy
            if ask_again_again == 'n':
                again_again = False
                ask_sure_again()
        elif final_of_final_candy < 0:
            print('Haha chơi kiểu gì mà bị nợ viên kẹo thế kia?? Đúng là non cái hand 😌')
            time.sleep(1)
            print('Bạn bị đuổi khỏi sòng do nợ Ánh kẹo. 💀\n')
            again_again = False
            ask_sure_again()

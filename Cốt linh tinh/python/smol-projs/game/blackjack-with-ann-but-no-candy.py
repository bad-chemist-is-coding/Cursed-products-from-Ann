import random
import time

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


def compare(player_score, ann_score):
    if player_score > 21 and ann_score > 21:
        return "Ánh đã quắc, và bạn cũng vậy, cả hai đều thua nhé ☺️"
    elif player_score < 16 and player_score != 0:
        return "Đã non rồi còn không rút thêm, bạn thua rồi 😋"
    elif player_score == ann_score:
        return "Bạn và Ánh cùng non, huề nhé 😘"
    elif player_score == 0:
        return "Ghê, Xì trùm luôn ta, dữ luôn ha 🙂"
    elif ann_score == 0:
        return "Gọi Ánh là Xì Trum hiền vì Ánh là Xì Trùm 😏"
    elif player_score > 21:
        return "Hahahahaha, non! 🥱"
    elif ann_score > 21:
        return "Ánh là quắc, còn bạn là nhất, được chưa? 🙃"
    elif player_score > ann_score:
        return "Ờ, bạn thắng, chúc mừng. 😐"
    elif player_score < ann_score:
        return "Đoán xem ai là con gà nào? 🐤"
    elif 15 < player_score < 21 and len(player_cards) == 5:
        return "Cứ ngỡ là bạn ngủ luôn mà ai dè Ngũ linh hén. 😬"
    elif 15 < ann_score < 21 and len(player_cards) == 5:
        return "Hehe, Ánh Ngũ linh, còn bạn ngủ luôn. 🤡"



again = True
while again:
    player_cards = []
    ann_cards = []
    game_over = False

    for _ in range(2):
        player_cards.append(deal_cards())
        ann_cards.append(deal_cards())

    while not game_over:
        player_score = calculate_score(player_cards)
        ann_score = calculate_score(ann_cards)
        print(f"\nÁnh spoil nhẹ lá bài đầu tiên của Ánh nè: {ann_cards[0]} 😉")
        print(f"Bài của bạn là: {player_cards}\nTuổi hiện tại của bạn là: {player_score}\n")

        if player_score == 0 or ann_score == 0:
            game_over = True
        elif len(player_cards) == 5:
            game_over = True
        else:
            player_deal = input('Bạn muốn rút thêm lá nữa? (Y/N)\n').lower()
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
                sure = input('Rút thêm lá nữa đi. Tôi biết bạn muốn rút thêm mà😏 (Y/N)\n').lower()
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

    print(f"💅💅💅💅💅💅💅💅\nBộ bài cuối cùng của bạn là: {player_cards}\nTuổi cuối cùng của bạn là: {player_score}\n💅💅💅💅💅💅💅💅")
    time.sleep(1)
    print('\nÁnh đang khéo léo rút bài.\n')
    time.sleep(2)
    print(f"😼😼😼😼😼😼😼😼\nÁnh đã khoe toàn bộ bài là: {ann_cards}\nTuổi cuối cùng của Ánh là: {ann_score}\n😼😼😼😼😼😼😼😼\n")

    print(compare(player_score, ann_score))

    sure_again = True
    while sure_again:
        should_again = input('\nBạn muốn đấu lại chứ? (Y/N)\n').lower()
        if should_again == 'n':
            print('Ánh biết bạn muốn chơi lại với Ánh mà 😍')
        if should_again == 'y':
            sure_again = False

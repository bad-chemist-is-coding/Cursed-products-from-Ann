import time
import random
from support_file_system import System

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
         11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
         11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
         11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
bot_cards = []
player_score = []
bot_score = []

sys = System(player_score, bot_score, cards, player_cards, bot_cards)


class Bot:

    def __init__(self, bot_name, bot_cards, bot_score):
        self.name = bot_name
        self.card = bot_cards
        self.score = bot_score
        self.order = None
        self.bet = None
        for _ in range(2):
            bot_cards.append(sys.deal_card(cards))
        self.score = sys.calculate_score(bot_cards)

    def deal_more_cards(self):
        while self.score != 0 and self.score < 17:
            self.card.append(sys.deal_card(cards))
            self.score = sys.calculate_score(self.card)


class Player:
    def __init__(self, player_name, player_cards, player_score, money, bet):
        self.name = player_name
        self.money = money
        self.bet = bet
        self.card = player_cards
        self.score = player_score
        self.order = None
        for _ in range(2):
            player_cards.append(sys.deal_card(cards))
        self.score = sys.calculate_score(player_cards)

    def money_female_house(self):
        self.money = random.randint(1, 100)
        print(f'\n🍬 Túi bạn hiện có {self.money} viên kẹo 🍬')
        time.sleep(0.5)
        print('Hehe, hãy sống sót đến cuối ván mà còn kẹo để thắng nhé! 😗')
        input("[Nhấn Enter để tiếp tục]")

    def deal_more_cards(self):
        self.score = sys.calculate_score(self.card)
        player_deal = input('👉 Bạn muốn rút thêm lá nữa? (Y/N)\n').lower()
        if player_deal == 'y':
            self.card.append(sys.deal_card(cards))
            self.score = sys.calculate_score(self.card)
        if player_deal == 'n' and len(self.card) == 4:
            sure = input('Rút thêm 1 lá nữa để Ngũ linh đi...hoặc ngủ luôn.💀 (Y/N)\n').lower()
            if sure == 'n':
                return True
            elif sure == 'y':
                self.card.append(sys.deal_card(cards))
                self.score = sys.calculate_score(self.card)
        if player_deal == 'n' and len(self.card) == 3:
            sure = input('Rút thêm lá nữa đi. Ánh biết bạn muốn rút thêm mà😏 (Y/N)\n').lower()
            if sure == 'n':
                return True
            elif sure == 'y':
                self.card.append(sys.deal_card(cards))
                self.score = sys.calculate_score(self.card)
        if player_deal == 'n' and len(self.card) == 2:
            sure = input('Định dằn non à? Rút thêm lá nữa đi. Bạn sợ à?😏 (Y/N)\n').lower()
            if sure == 'y':
                self.card.append(sys.deal_card(cards))
                self.score = sys.calculate_score(self.card)
            elif sure == 'n':
                return True
        elif len(self.card) == 5:
            return True

    def deal_more_cards_female_house(self):
        self.score = sys.calculate_score(self.card)
        player_deal = input('👉 Bạn nên rút thêm lá nữa? (Y/N)\n').lower()
        if player_deal == 'y':
            self.card.append(sys.deal_card(cards))
            self.score = sys.calculate_score(self.card)
        if player_deal == 'n' and len(self.card) == 4:
            sure = input('Lỡ Ngũ linh sao nhỉ? Nên rút không? (Y/N) 😀\n').lower()
            if sure == 'n':
                return True
            elif sure == 'y':
                self.card.append(sys.deal_card(cards))
                self.score = sys.calculate_score(self.card)
        elif player_deal == 'n' and len(self.card) == 3:
            sure = input('Thấy còn hơi ít lá. Rút thêm không? (Y/N) 😀\n').lower()
            if sure == 'n':
                return True
            elif sure == 'y':
                self.card.append(sys.deal_card(cards))
                self.score = sys.calculate_score(self.card)
        elif player_deal == 'n' and len(self.card) == 2:
            sure = input('Chưa rút thêm lá nào mà nhỉ? Rút thêm không? (Y/N) 😀\n').lower()
            if sure == 'y':
                self.card.append(sys.deal_card(cards))
                self.score = sys.calculate_score(self.card)
            elif sure == 'n':
                return True
        elif len(self.card) == 5:
            return True

    def bet_candy(self, money, alive):
        print(f'\n🍬 Túi bạn hiện có {money} viên kẹo 🍬')
        time.sleep(1)
        while alive:
            bet = int(input('Số kẹo bạn muốn đánh đổi: '))
            if bet > 200:
                print('Bạn giỡn mặt hả, gì mà cược bằng cả tính mạng thế? Cho cơ hội làm lại đó 😑')
                time.sleep(0.5)
            elif bet <= 1:
                print("Haha, hài hước quá, chọn lại đi 😑")
            elif bet >= money:
                print(f'Máu đó! Bạn đã liều mình cược {bet} viên kẹo! Dù không đủ 😃')
                self.bet = bet
                alive = False
            elif bet < money:
                print(f'Bạn đã an toàn cược {bet} viên kẹo, nước đi an toàn đấy. 😊')
                self.bet = bet
                alive = False

class Mode:

    def choose_mode(self, mode):
        if mode > 4:
            print('Xin lỗi, không đủ Ánh để cho bạn chơi 😔\n')
            time.sleep(0.5)
            return True
        elif mode < 1:
            print('Gì mà đòi âm Ánh vậy? Muốn Ánh từ cõi âm lên chơi cùng à?? 😈\n')
            time.sleep(0.5)
            return True
        else:
            print(f"💁‍♀️ Bạn đã lập sòng Xì Ách với {mode} Ánh! 💁‍♀️\n")
            time.sleep(1)
            return False

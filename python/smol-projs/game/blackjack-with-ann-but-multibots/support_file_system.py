import random


class System:

    def __init__(self, player_score, bot_score, player_cards, bot_cards, cards):
        self.player_score = player_score
        self.bot_score = bot_score
        self.player_cards = player_cards
        self.bot_cards = bot_cards

    def deal_card(self, cards):
        self.card = random.choice(cards)
        return self.card

    def calculate_score(self, cards):
        if sum(cards) == 21 and len(cards) == 2:
            return 0
        elif (10 not in cards and 9 not in cards and 8 not in cards and 7 not in cards and 6 not
              in cards and 5 not in cards and 4 not in cards and 3 not in cards and 2 not in cards and
              11 not in cards and len(cards) == 2):
            return 0
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)

    def compare_score_for_result(self, bot_name, bot_cards, player_cards, player_score, bot_score):
        if player_score > 21 and bot_score > 21:
            return f"🟦 {bot_name} đã quắc, và bạn cũng vậy, cả hai chạy kẹo nhé ☺️"
        elif player_score == bot_score:
            return f"🟦 Bạn và {bot_name} đều bằng nhau, chạy kẹo nhé 😘"
        elif player_score == 0:
            return "🟩 Ghê, Xì trùm luôn ta, dữ luôn ha 🙂"
        elif bot_score == 0:
            return "🟥 Gọi Ánh là Xì Trum hiền vì Ánh là Xì Trùm 😏"
        elif bot_score < 21 and len(bot_cards) == 5:
            return f"🟥 Hehe, {bot_name} Ngũ linh, còn bạn ngủ luôn. 🤡"
        elif player_score < 21 and len(player_cards) == 5:
            return "🟩 Cứ ngỡ là bạn ngủ luôn mà ai dè Ngũ linh hén. 😬"
        elif player_score < 16 and player_score != 0:
            return "🟥 Đã non rồi còn không rút thêm, bạn thua rồi 😋"
        elif player_score > 21:
            return "🟥 Hahahahaha, quắc cần câu! 🥱"
        elif bot_score > 21:
            return f"🟩 {bot_name} là quắc, còn bạn là nhất, được chưa? 🙃"
        elif player_score > bot_score:
            return f"🟩 Thắng {bot_name} luôn ta, chúc mừng. 😐"
        elif player_score < bot_score:
            return "🟥 Đoán xem ai là con gà nào? 🐤"

    def compare_score_of_bots_for_result(self, female_house_name, bot_name, female_house_cards, bot_cards, bot_score,
                                         female_house_score):
        if bot_score > 21 and female_house_score > 21:
            return f"🟦 {female_house_score} và {bot_name} đều quắc, cả hai chạy kẹo."
        elif bot_score == female_house_score:
            return f"🟦 {bot_name} và {female_house_name} đều bằng nhau, cả hai chạy kẹo."
        elif bot_score == 0:
            return f"🟩 {bot_name} đã đánh gục {female_house_name} bằng Xì trùm."
        elif female_house_score == 0:
            return f"🟥 {female_house_name} làm Xì Trùm đánh gục {bot_name}."
        elif female_house_score < 22 and len(female_house_cards) == 5:
            return f"🟥 Nhà cái {female_house_name} đã Ngũ linh!"
        elif bot_score < 22 and len(bot_cards) == 5:
            return f"🟩 {bot_name} được Ngũ linh!!"
        elif bot_score > 21:
            return f"🟥 {bot_name} quắc!"
        elif female_house_score > 21:
            return f"🟩 {female_house_name} bị quắc, còn {bot_name} ăn"
        elif bot_score > female_house_score:
            return f"🟩 {bot_name} đã thắng {female_house_name}! "
        elif bot_score < female_house_score:
            return f"🟥 {bot_name} đã thua {female_house_name}!"

    def compare_result_to_return_signals(self, player_score, bot_score, player_cards, bot_cards, final_result):
        if player_score == 0:
            final_result += 2
            return final_result
        elif bot_score == 0:
            final_result += -2
            return final_result
        elif bot_score < 22 and len(bot_cards) == 5:
            final_result += -2
            return final_result
        elif player_score < 22 and len(player_cards) == 5:
            final_result += 2
            return final_result
        elif bot_score > 21 and player_score > 21:
            return final_result
        elif player_score < 16 and player_score != 0:
            final_result += -1
            return final_result
        elif player_score > 21:
            final_result += -1
            return final_result
        elif bot_score > 21:
            final_result += 1
            return final_result
        elif player_score > bot_score:
            final_result += 1
            return final_result
        elif player_score < bot_score:
            final_result += -1
            return final_result
        else:
            return final_result

    def compare_to_calculate_candy(self, final_result, money, bet):
        if final_result == -2:
            final_candy = money - 2 * bet
            return int(final_candy)
        elif final_result == +2:
            final_candy = money + 2 * bet
            return int(final_candy)
        elif final_result == -1:
            final_candy = money - bet
            return int(final_candy)
        elif final_result == 1:
            final_candy = money + bet
            return int(final_candy)
        else:
            final_candy = money
            return int(final_candy)

    def speccial_case_check(self, player_score, bot_score):
        if player_score == 0 or bot_score == 0:
            return True
        else:
            return False

    def bet_result(self, final_result, bet, last_final_candy, bot_name):
        if final_result == -2:
            return print(
                f'Bạn thua đậm {bot_name} mất {2 * bet} viên kẹo và còn {last_final_candy} viên trong túi. 😱\n')
        elif final_result == +2:
            return print(
                f'Bạn thắng đậm {bot_name} thêm {2 * bet} viên kẹo và có {last_final_candy} viên trong túi. 😳\n')
        elif final_result == -1:
            return print(f'Bạn thua {bot_name} mất {bet} viên kẹo và còn {last_final_candy} viên trong túi. 🤏\n')
        elif final_result == 1:
            return print(f'Bạn thắng {bot_name} thêm {bet} viên kẹo và có {last_final_candy} viên trong túi. 😮\n')
        elif final_result == 0:
            return print(
                f'Bạn chẳng mất hay thêm viên kẹo nào cả nên vẫn có {last_final_candy} viên kẹo trong túi. 👏\n')

    def bet_result_of_bots(self, final_result, bet, last_final_candy, bot_name, female_house_name):
        if final_result == -2:
            return print(
                f'{bot_name} thua đậm {female_house_name} thêm {2 * bet} viên kẹo và {female_house_name} có {last_final_candy} viên trong túi.\n')
        elif final_result == +2:
            return print(
                f'{bot_name} thắng đậm {female_house_name} mất {2 * bet} viên kẹo và {female_house_name} còn {last_final_candy} viên trong túi.\n')
        elif final_result == -1:
            return print(
                f'{bot_name} thua {female_house_name} thêm {bet} viên kẹo và {female_house_name} có {last_final_candy} viên trong túi.\n')
        elif final_result == 1:
            return print(
                f'{bot_name} thắng {female_house_name} mất {bet} viên kẹo và {female_house_name} còn {last_final_candy} viên trong túi.\n')
        elif final_result == 0:
            return print(
                f'{female_house_name} chẳng mất hay thêm viên kẹo nào cả nên vẫn có {last_final_candy} viên kẹo trong túi.\n')

        def bet_result(self, final_result, bet, last_final_candy, bot_name):
            if final_result == -2:
                return print(
                    f'Bạn thua đậm {bot_name} mất {2 * bet} viên kẹo và còn {last_final_candy} viên trong túi. 😱\n')
            elif final_result == +2:
                return print(
                    f'Bạn thắng đậm {bot_name} thêm {2 * bet} viên kẹo và có {last_final_candy} viên trong túi. 😳\n')
            elif final_result == -1:
                return print(f'Bạn thua {bot_name} mất {bet} viên kẹo và còn {last_final_candy} viên trong túi. 🤏\n')
            elif final_result == 1:
                return print(f'Bạn thắng {bot_name} thêm {bet} viên kẹo và có {last_final_candy} viên trong túi. 😮\n')
            elif final_result == 0:
                return print(
                    f'Bạn chẳng mất hay thêm viên kẹo nào cả nên vẫn có {last_final_candy} viên kẹo trong túi. 👏\n')

    def bet_result_for_player_not_female_house(self, final_result, bet, last_final_candy, female_house_name,
                                               female_house_last_final_candy):
        if final_result == -2:
            return print(
                f'Bạn thua đậm {female_house_name} mất {2 * bet} viên kẹo và còn {last_final_candy} viên trong túi. 😱\n'
                f'và {female_house_name} còn {female_house_last_final_candy} viên kẹo.')
        elif final_result == +2:
            return print(
                f'Bạn thắng đậm {female_house_name} thêm {2 * bet} viên kẹo và có {last_final_candy} viên trong túi. 😳\n'
                f'và {female_house_name} còn {female_house_last_final_candy} viên kẹo.')
        elif final_result == -1:
            return print(
                f'Bạn thua {female_house_name} mất {bet} viên kẹo và còn {last_final_candy} viên trong túi. 🤏\n'
                f'và {female_house_name} còn {female_house_last_final_candy} viên kẹo.')
        elif final_result == 1:
            return print(
                f'Bạn thắng {female_house_name} thêm {bet} viên kẹo và có {last_final_candy} viên trong túi. 😮\n'
                f'và {female_house_name} còn {female_house_last_final_candy} viên kẹo.')
        elif final_result == 0:
            return print(
                f'Bạn chẳng mất hay thêm viên kẹo nào cả nên vẫn có {last_final_candy} viên kẹo trong túi. 👏\n'
                f'và {female_house_name} còn {female_house_last_final_candy} viên kẹo.')

    def compare_to_calculate_candy_for_female_house_not_player(self, final_result, female_house_bet, player_bet):
        if final_result == -2:
            final_female_house_candy = female_house_bet + 2 * player_bet
            return int(final_female_house_candy)
        elif final_result == +2:
            final_candy = female_house_bet - 2 * player_bet
            return int(final_candy)
        elif final_result == -1:
            final_candy = female_house_bet + player_bet
            return int(final_candy)
        elif final_result == 1:
            final_candy = female_house_bet - player_bet
            return int(final_candy)
        else:
            final_candy = female_house_bet
            return int(final_candy)

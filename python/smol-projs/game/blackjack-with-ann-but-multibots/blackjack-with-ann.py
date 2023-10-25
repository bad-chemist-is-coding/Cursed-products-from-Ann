import random
import time
from support_file_system import System
from support_file_bot_and_player import Bot, Player, Mode
# Lỡ có Xì Trùm mà vẫn chơi bình thường thì đó là tính năng nha ^^
# Phiên bản ultra-vip tích hợp nhiều tính năng mới!!!
restart = True
while restart:
    dice = list(range(1, 7))
    cards = []
    bot_name = []
    bot_cards = []
    bot_score = []
    bot_order = []
    player_cards = []
    player_score = []
    bot_1_cards = []
    bot_2_cards = []
    bot_3_cards = []
    bot_4_cards = []
    bot_1_score = []
    bot_2_score = []
    bot_3_score = []
    bot_4_score = []
    money = random.randint(1, 100)
    bet = []

    final_final_candy = 0
    final_final_candy_of_female_house = 0

    mode = Mode()
    bot = Bot(bot_name, bot_cards, bot_score)
    sys = System(player_score, bot_score, player_cards, bot_cards, cards)
    print('♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠')
    print("🃏 XÌ ÁCH CÙNG SÒNG ÁNH 🃏")
    print('♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠\n')
    rechoose = True
    mode_chosen = None
    while rechoose:
        mode_chosen = int(input("❓ Bạn muốn chơi Xì Ách với bao nhiêu Ánh? (Tối đa 4 ánh thôi)"
                                "\nSố Ánh bạn muốn chơi: "))
        rechoose = mode.choose_mode(mode_chosen)
    player = Player("Bạn", player_cards, player_score, money, bet)
    input("Các bạn sẽ tung xúc sắc để quyết định thứ tự chơi!\n🎲 Nhấn Enter để đổ xúc sắc 🎲\n")
    ann_1 = Bot("Bé Ánh", bot_1_cards, bot_1_score)
    ann_2 = Bot("Chị Ánh", bot_2_cards, bot_2_score)
    ann_3 = Bot("Cô Ánh", bot_3_cards, bot_3_score)
    ann_4 = Bot("Bà Ánh", bot_4_cards, bot_4_score)

    rollers = [player, ann_1]
    if mode_chosen == 2:
        rollers.append(ann_2)
    elif mode_chosen == 3:
        rollers.append(ann_2)
        rollers.append(ann_3)
    elif mode_chosen == 4:
        rollers.append(ann_2)
        rollers.append(ann_3)
        rollers.append(ann_4)

    for people in rollers:
        order_set = random.choice(dice)
        people.order = order_set
        print(f"🎲 {people.name} đã lắc ra số {people.order}")
        dice.remove(order_set)
    sorted_roller = sorted(rollers, key=lambda people: people.order, reverse=True)
    sorted_list = [people for people in sorted_roller]
    mode_game = input("\n❓ Bạn muốn làm nhà con (A) hay nhà cái (B)? (Gõ 'A' hoặc 'B')\n").lower()
    if mode_game == 'b':
        player.money_female_house()
        sorted_list.remove(player)
        formatted_name = [f"{person.name}, " for person in sorted_list]
        print("\n🤙 Thứ tự chơi của sòng là " + "".join(formatted_name))
        time.sleep(1)
        for bets in sorted_list:
            bet_values_of_bots = random.randint(1, 100)
            bets.bet = bet_values_of_bots
            print(f"🍭 {bets.name} đã cược {bets.bet} viên kẹo!")
        input("\n[Nhấn Enter để bắt đầu chia bài]")
        print("\n🖐️ Bạn phát cho mỗi Ánh hai lá bài")
        time.sleep(1)

        game_over_because_of_special_cases = False
        while not game_over_because_of_special_cases:
            for name in sorted_list:
                print(f"\n♣ Bạn đưa tụ bài cho {name.name} bốc thêm bài. 🃏👌")
                time.sleep(1)
            ann_1.deal_more_cards()
            ann_2.deal_more_cards()
            ann_3.deal_more_cards()
            ann_4.deal_more_cards()
            time.sleep(1)
            print("--------------------")
            print("👍 Đến lượt bạn 👍")
            game_over = False
            while not game_over:
                print(f"💕 Bài của bạn là: {player.card}\n🔥 Tuổi hiện tại của bạn là {player.score}")
                game_over = player.deal_more_cards_female_house()
            print(f"\n✨ Tuổi cuối cùng của bạn là {player.score}! ✨")
            print("--------------------")
            game_over_because_of_special_cases = True
        time.sleep(0.5)
        print("\n💀 Đang chuẩn bị xét bài các nhà con 💀\n")
        time.sleep(1)
        input(f"[Nhấn Enter để bắt đầu xét bài]")
        for char in sorted_list:
            print('\n~~~~~~~~~~~~~')
            print(
                f'🔥 Bài của {char.name} là {char.card}.\n🤜 Tuổi của {char.name} là {char.score}')
            time.sleep(1)
            print(sys.compare_score_for_result(char.name, char.card, player.card, player.score,
                                               char.score))
            final_result = 0
            final_result = sys.compare_result_to_return_signals(player.score, char.score, player.card,
                                                                char.card,
                                                                final_result)
            final_candy = sys.compare_to_calculate_candy(final_result, player.money, char.bet)
            time.sleep(0.5)
            sys.bet_result(final_result, char.bet, final_candy, char.name)
            player.money = final_candy
            input(f"[Gõ Enter để tiếp tục]")
            final_final_candy = final_candy



    elif mode_game == 'a':
        alive = True
        player.bet_candy(player.money, alive)
        player_order = sorted_list.index(player)
        sorted_list.remove(player)
        sorted_list[0].bet = random.randint(1, 100)
        time.sleep(2)
        print(f"\n{sorted_list[0].name} là nhà cái và có trong túi {sorted_list[0].bet} viên kẹo! 🍭")
        female_house = sorted_list[0]
        female_order = sorted_list.index(female_house)
        sorted_list.remove(female_house)
        time.sleep(1)
        for bets in sorted_list:
            bet_values_of_bots = random.randint(1, 100)
            bets.bet = bet_values_of_bots
            print(f"🍭 {bets.name} đã cược {bets.bet} viên kẹo!")
        print(f"🍭 Còn bạn cược {player.bet} viên kẹo!")
        sorted_list.insert(player_order - 1, player)
        formatted_name = [f"{person.name}, " for person in sorted_list]
        time.sleep(1)
        print("\n🤙 Thứ tự chơi của sòng là " + "".join(formatted_name))
        input("\n[Nhấn Enter để bắt đầu sòng]")
        print(f"\n🖐️ {female_house.name} phát cho mỗi người hai lá bài")
        time.sleep(1)
        game_over_because_of_special_cases = False
        while not game_over_because_of_special_cases:
            for person in sorted_list:
                if person == player:
                    time.sleep(1)
                    game_over = False
                    while not game_over:
                        print("\n--------------------")
                        print(f"♣ {female_house.name} đưa bài cho bạn bốc 🃏👌")
                        print(f"💕 Bài của bạn là: {player.card}\n🔥 Tuổi hiện tại của bạn là {player.score}")
                        game_over = player.deal_more_cards()
                    print(f"\n✨ Tuổi cuối cùng của bạn là {player.score}! ✨")
                    print("--------------------")
                    time.sleep(1)
                elif person != player:
                    print(f"\n♣ {female_house.name} đã đưa tụ bài cho {person.name} bốc thêm bài. 🃏👌")
                    time.sleep(1)
            ann_1.deal_more_cards()
            ann_2.deal_more_cards()
            ann_3.deal_more_cards()
            ann_4.deal_more_cards()
            game_over_because_of_special_cases = True
        print(f"\n😰 Nhà cái {female_house.name} đang căng thẳng bốc bài 😰")
        time.sleep(2)
        print("\n💀 Nhà cái đang chuẩn bị xét bài các nhà con 💀\n")
        time.sleep(2)
        print(
            f"🌝 Bài của {female_house.name} là {female_house.card}.\n🌚 Tuổi của {female_house.name} là "
            f"{female_house.score}")
        time.sleep(3)
        last_final_candy = 0
        last_final_of_female_house = 0
        for char in sorted_list:
            if char == player:
                print('\n~~~~~~~~~~~~~')
                print(f'💕 Bài của bạn là: {player.card}\n🔥 Tuổi của bạn là {player.score}')
                time.sleep(1)
                print(sys.compare_score_for_result(female_house.name, female_house.card, player.card, player.score,
                                                   female_house.score))
                final_result = 0
                final_result = sys.compare_result_to_return_signals(player.score, female_house.score, player.card,
                                                                    female_house.card, final_result)
                time.sleep(0.5)
                last_final_of_female_house = (sys.compare_to_calculate_candy_for_female_house_not_player
                                              (final_result, female_house.bet, player.bet))
                last_final_candy = sys.compare_to_calculate_candy(final_result, player.money, player.bet)
                sys.bet_result_for_player_not_female_house(final_result, player.bet, last_final_candy,
                                                           female_house.name, last_final_of_female_house)
                female_house.bet = last_final_of_female_house
                input(f"[Gõ Enter để {female_house.name} tiếp tục]")
            elif char != player:
                print('\n~~~~~~~~~~~~~')
                print(f'🔥 Bài của {char.name} là {char.card}.\n🔥 Tuổi của {char.name} là {char.score}')
                print(sys.compare_score_of_bots_for_result(female_house.name, char.name, female_house.card, char.card,
                                                           char.score, female_house.score))
                final_result = 0
                final_result = sys.compare_result_to_return_signals(char.score, female_house.score, char.card,
                                                                    female_house.card, final_result)
                final_candy = (sys.compare_to_calculate_candy_for_female_house_not_player
                               (final_result, female_house.bet, char.bet))
                time.sleep(0.5)
                sys.bet_result_of_bots(final_result, char.bet, final_candy, char.name, female_house.name)
                female_house.bet = final_candy
                input(f"[Gõ Enter để {female_house.name} tiếp tục]")
        final_final_candy = last_final_candy
        final_final_candy_of_female_house = last_final_of_female_house
    time.sleep(1)
    print(f"\n☘ Cuối cùng, bạn còn {final_final_candy} viên kẹo trong túi! ☘")
    time.sleep(1)
    if final_final_candy < 0:
        print("Chơi kiểu gì mà nợ kẹo luôn vậy, bạn bị đuổi khỏi sòng 🤦‍♀️")
        time.sleep(1)
        if final_final_candy_of_female_house < 0:
            print("Cùng với nhà cái do cả hai đều nợ nần 🤡")
    elif final_final_candy > 0:
        print("Ảo thật đấy, chơi thế mà cuối cùng vẫn còn kẹo à 💅 \n💖 Chúc mừng 💖")
        time.sleep(1)
        if final_final_candy_of_female_house < 0:
            print("Còn nhà cái đi nấu rồi 🤡")
    again = input("Bạn muốn tham gia vào sòng khác? (Y/N)😏\n ").lower()
    if again == "n":
        print("Muốn chơi thì ghé sòng mấy Ánh nha 😉")
        restart = False

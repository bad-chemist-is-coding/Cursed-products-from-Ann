import time
import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if (sum(cards) == 21 or 11 in cards and 11 in cards) and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(player_score, computer_score):

    if player_score > 21 and computer_score > 21:
        return "Draw"

    if player_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has BJ"
    elif player_score == 0:
        return "Win with a BJ"
    elif player_score > 21:
        return "Lose"
    elif computer_score > 21:
        return "Win"
    elif player_score > computer_score:
        return "Win"
    else:
        return "Lose"

def play_game():
    player_cards = []
    computer_cards = []
    game_over = False

    for _ in range(2):
        player_cards.append(deal_card())  # Do deal_card() return danh sách nên phải dùng hàm append thanh vì +=
        computer_cards.append(deal_card())

    while not game_over:
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)
        print(f'Bài đầu tiên của máy: {computer_cards[0]}')
        print(f'Bài của bạn: {player_cards}\nTuổi của bạn: {player_score}')

        if player_score == 0 or computer_score == 0 or player_score > 21:
            game_over = True
        else:
            player_deal = input('Rút thêm lá nữa? (Y/N)\n').lower()
            if player_deal == "y":
                player_cards.append(deal_card())
            else:
                game_over = True

        while computer_score != 0 and computer_score < 16:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)

        print(f"Bài cuối cùng của bạn: {player_cards}\n Tuổi của bạn là: {player_score}")
        print(f"Bài cuối cùng của máy: {computer_cards}\n Tuổi của máy là: {computer_score}")
        print(compare(player_score, computer_score))

while input("Muốn chơi? (Y/N)").lower() == "y":
    play_game()

import random
import time

REMAINING_OXYGEN = 25
DEPTH = 32

characters = {
    "player_1": "🙂",
    "player_2": "🙁",
    "player_3": "🤬",
    "player_4": "🤮",
    "player_5": "🥵"
}

chips_on_map = []
player_map = []


def oxygen_level(oxygen_location):
    map = []
    for i in range(25, -1, -1):
        map.append(str(i))
    map[oxygen_location] = '🔴'
    print("Remaining Oxygen: ")
    print(" | ".join(map))


def undersea_level(player_move, chips_position_at_player):
    if len(chips_on_map) == 0 and len(player_map) == 0:
        for i in range(1, 34):
            if i == 1:
                chips_on_map.append("☢️")
            elif i < 9:
                chips_on_map.append("1️⃣")
            elif 8 < i < 17:
                chips_on_map.append("2️⃣")
            elif 16 < i < 25:
                chips_on_map.append("3️⃣")
            elif 24 < i < 34:
                chips_on_map.append("4️⃣")
        for i in range(1, 34):
            player_map.append("🐟")
    else:
        if player_move <= 0:
            player_map[0] = characters['player_1']
        else:
            player_map[player_move] = characters['player_1']
            chips_position_at_player = chips_on_map[player_map.index(characters["player_1"])]
    print(f"Vị trí kho báu người chơi đứng: {chips_position_at_player}")
    print("Undersea Map: ")
    print(" | ".join(chips_on_map))
    print("   ".join(player_map))


print("\n\t(☞ﾟヮﾟ)☞\tDEEP SEA ADVENTURE\t☜(ﾟヮﾟ☜)\n")

game_on = True
while game_on:
    replace = False
    treasure_position_at_player_position = 0 # Làm sao để đặt biến này nhưng không có giá trị 0
    oxygen_level(0)
    undersea_level(0, treasure_position_at_player_position)
    player_1_treasure = 0

    next_player = True

    while next_player:
        treasure_collection = []
        dice = random.randint(2, 6)
        order_drop = 0
        # Reduce Oxygen
        print("~~~~~~~~~~~~~")
        print(f"You are having {player_1_treasure} treasures, you will be reduced {player_1_treasure} oxygen player.")
        # Turn back?
        turn_back = input("You want to turn back to submarine? (Y/N): ").lower()
        if turn_back == "y":
            new_dice = dice * -1
        else:
            new_dice = dice

        # Roll the dice
        input("Enter to roll the dice")
        print("Số lắc ra (Có thể + hoặc -): " + f"{new_dice}")

        # Subtract the treasures
        move = dice - player_1_treasure
        print("Số di chuyển: " + f"{move}")
        if move < 1:
            print("You can't move")
            move = 0
        else:
            pass
        time.sleep(0.5)
        print("----------------")
        time.sleep(0.5)
        oxy_location = player_1_treasure
        player_position = new_dice
        REMAINING_OXYGEN = REMAINING_OXYGEN - oxy_location
        oxygen_level(25 - REMAINING_OXYGEN)
        DEPTH = DEPTH - player_position
        if DEPTH <= 0:
            player_depth = 0
            new_dice = 0
        else:
            player_depth = 32 - DEPTH
        undersea_level(player_depth, treasure_position_at_player_position)

        if player_depth <= 0:
            game_on = False
            next_player = False
        else:
            action = input("What do you want to do?\nA. Do nothing\nB. Pick up the treasure\nC. Drop the "
                           "treasure\nYour action (A/B/C): ").lower()
            if action == "a":
                pass
            elif action == "b" and treasure_position_at_player_position != "⚪":
                player_1_treasure += 1
                treasure_collection.append(treasure_position_at_player_position)
                print("\n Lượng kho báu bạn đang có:")
                print(treasure_collection) # Output ra vẫn là 0, trong khi mình muốn là vị trí của người chơi trên map
            elif action == "c" and treasure_position_at_player_position == "⚪" and len(treasure_collection) > 0:
                player_1_treasure -= 1
                print("\n Lượng kho báu bạn đang có:")
                print(treasure_collection)
                remove_choice = int(input("Nhập số thứ tự kho báu bạn muốn bỏ: "))
                remove_choice += 1
                treasure_collection.pop(remove_choice)
                print("Lượng kho báu bạn còn: ")
                print(treasure_collection)

            else:
                print("Sai cú pháp, tự động chon A. Do nothing")

import random
import time

REMAINING_OXYGEN = 25  # max oxygen level
DEPTH = 33  # max depth

characters = {  # Dictionary of characters
    "player_1": "🙂",
    "player_2": "🙁",
    "player_3": "🤬",
    "player_4": "🤮",
    "player_5": "🥵"
}


def oxygen_level(oxygen_location):  # Function to display oxygen level

    # Creating oygen map list
    map = []
    for i in range(25, -1, -1):  # For loop to insert oxygen map values
        map.append(str(i))

    # Insert red dot to show remaining oxygen
    map[oxygen_location] = '🔴'
    print("Remaining Oxygen: ")
    print(" | ".join(map))


chips_on_map = ["☢️", "1️⃣", "1️⃣", "1️⃣", "1️⃣", "1️⃣", "1️⃣", "1️⃣", "1️⃣", "2️⃣", "2️⃣", "2️⃣", "2️⃣", "2️⃣", "2️⃣",
                "2️⃣", "2️⃣", "3️⃣", "3️⃣", "3️⃣", "3️⃣", "3️⃣", "3️⃣", "3️⃣", "3️⃣", "4️⃣", "4️⃣", "4️⃣", "4️⃣", "4️⃣",
                "4️⃣", "4️⃣", "4️⃣"]


def undersea_level(player_position, treasure_at_player_position,
                   removed_treasure):  # Function to display the undersea map

    # Filling blank spots on the map
    if len(treasure_collection) != 0:
        for index in blank_chips_on_map:
            chips_on_map[index - 1] = "⚪"

    if removed_treasure != None:
        chips_on_map[player_position - new_move] = removed_treasure

    # Displaying the player's position
    player_map = []
    for i in range(1, 34):  # For loop to display player's map
        player_map.append("🐟")

    if player_position <= 0:
        player_map[0] = characters['player_1']

    else:
        player_map[player_position] = characters['player_1']  # Displaying player's position
        treasure_at_player_position = chips_on_map[
            player_position]  # Getting the position of the chip at the player's position

    print(f"Vị trí kho báu người chơi đứng: {treasure_at_player_position}")

    # Draw map
    print("Undersea Map: ")
    print(" | ".join(chips_on_map))
    print("   ".join(player_map))

    return treasure_at_player_position


# Title screen
print("\n\t(☞ﾟヮﾟ)☞\tDEEP SEA ADVENTURE\t☜(ﾟヮﾟ☜)\n")

# Gameplay loop
game_on = True
while game_on:

    chips_on_map = ["☢️", "1️⃣", "1️⃣", "1️⃣", "1️⃣", "1️⃣", "1️⃣", "1️⃣", "1️⃣", "2️⃣", "2️⃣", "2️⃣", "2️⃣", "2️⃣",
                    "2️⃣", "2️⃣", "2️⃣", "3️⃣", "3️⃣", "3️⃣", "3️⃣", "3️⃣", "3️⃣", "3️⃣", "3️⃣", "4️⃣", "4️⃣", "4️⃣",
                    "4️⃣", "4️⃣", "4️⃣", "4️⃣", "4️⃣"]
    # lvl_1_chip_score = random.randint(0, 3)
    # lvl_2_chip_score = random.randint(4, 7)
    # lvl_3_chip_score = random.randint(8, 11)
    # lvl_4_chip_score = random.randint(12, 15)
    treasure_at_player_position = None
    treasure_order_at_player_position = 0
    removed_treasure = None

    treasure_collection = []
    blank_chips_on_map = []
    dropped_treasures = []

    replace = False
    oxygen_level(0)
    undersea_level(0, treasure_at_player_position, removed_treasure)
    player_1_treasure = 0

    next_player = True

    while next_player:

        # Reduce Oxygen
        print("~~~~~~~~~~~~~")
        print(
            f"You are having {player_1_treasure} treasures, you will be reduced {player_1_treasure} oxygen player."
        )

        # Turn back?
        dice = random.randint(2, 6)
        move = dice - player_1_treasure  # Subtract the treasures
        turn_back = input("You want to turn back to submarine? (Y/N): ").lower()
        if turn_back == "y":
            new_move = move * -1
        else:
            new_move = move

        # Roll the dice
        input("Enter to roll the dice")

        print("Số lắc ra: " + f"{dice}")
        print("Số di chuyển: " + f"{move}")

        if move < 1:
            print("You can't move")
            new_move = 0

        else:
            pass

        time.sleep(0.5)
        print("----------------")
        time.sleep(0.5)

        oxy_location = player_1_treasure
        REMAINING_OXYGEN -= oxy_location
        oxygen_level(25 - REMAINING_OXYGEN)
        DEPTH -= new_move

        if DEPTH <= 0:
            player_position = 0
            new_dice = 0

        else:
            player_position = 33 - DEPTH

        treasure_at_player_position = undersea_level(
            player_position, treasure_at_player_position, removed_treasure)
        treasure_order_at_player_position = player_position + 1

        removed_treasure = None

        if player_position <= 0:
            game_on = False
            next_player = False

        else:
            action = input(
                "What do you want to do?\nA. Do nothing\nB. Pick up the treasure\nC. Drop the "
                "treasure\nYour action (A/B/C): ").lower()

            if action == "a":
                replace = False

            elif action == "b" and treasure_at_player_position != "⚪":
                player_1_treasure += 1
                treasure_collection.append(treasure_at_player_position)
                print("\nLượng kho báu bạn đang có:")
                print(" ".join(treasure_collection))
                blank_chips_on_map.append(treasure_order_at_player_position)
                replace = True

            elif action == "c" and treasure_at_player_position == "⚪" and len(treasure_collection) > 0:
                player_1_treasure -= 1
                print("\nLượng kho báu bạn đang có:")
                print(" ".join(treasure_collection))
                remove_choice = int(input("Nhập số thứ tự kho báu bạn muốn bỏ: "))
                removed_treasure = treasure_collection.pop(remove_choice - 1)
                print("Lượng kho báu bạn còn: ")
                print(" ".join(treasure_collection))
                blank_chips_on_map.remove(treasure_order_at_player_position)
                replace = True

            else:
                print("Sai cú pháp, tự động chon A. Do nothing")

            print("Kho báu bị loại bỏ: ")
            print(removed_treasure)
            print("SỐ THỨ TỰ BLANK CHIPS")
            print(blank_chips_on_map)

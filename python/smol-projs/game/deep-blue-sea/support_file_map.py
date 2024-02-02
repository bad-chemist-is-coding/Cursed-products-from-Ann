REMAINING_OXYGEN = 25
DEPTH = 32


def oxygen_level(oxygen_location):
    map = []
    for i in range(25, -1, -1):
        map.append(str(i))
    map[oxygen_location] = '🔴'
    print(" | ".join(map))


# oxygen_level(0)
# while True:
#     oxy_location = int(input("Pick an order: "))
#     REMAINING_OXYGEN = REMAINING_OXYGEN - oxy_location
#     oxygen_level(25 - REMAINING_OXYGEN)

characters = {
    "player_1": "🙂",
    "player_2": "🙁",
    "player_3": "🤬",
    "player_4": "🤮",
    "player_5": "🥵"
}




def undersea_level(player_move):
    chips_on_map = []
    player_map = []
    for i in range(1, 33):
        if i < 9:
            chips_on_map.append("1️⃣")
        elif 8 < i < 17:
            chips_on_map.append("2️⃣")
        elif 16 < i < 25:
            chips_on_map.append("3️⃣")
        elif 24 < i < 33:
            chips_on_map.append("4️⃣")
    for i in range(1, 33):
        player_map.append("🐟")
    player_map[player_move - 1] = characters['player_1']
    print(" | ".join(chips_on_map))
    print("   ".join(player_map))



# undersea_level(0)
# while True:
#     player_position = int(input("Pick a player position: "))
#     DEPTH = DEPTH - player_position
#     undersea_level(32 - DEPTH)

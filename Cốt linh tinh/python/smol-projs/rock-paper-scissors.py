import random

print("Project 4:\n\t OẲN TÙ TÌ")

rock = '''
    ___
---'   __)
      (_)
      (_)
      (__)
---.__(_)
'''
paper = '''
     ___
---'    _)___
           __)
          ___)
         ___)
---.__________)
'''
scissors ='''
    ___
---'   _)___
          __)
       ______)
      (__)
---.__(_)
'''
image = [scissors, rock, paper]

player = int(input("Oẳn tù tì, ra cái gì, ra cái này\n(Gõ 0 chọn kéo, 1 chọn búa, 2 chọn bao): "))
if player > 2 or player < 0:
    print("Không chơi lại nên chọn cái khác à? Gà! 🐔")
else:
    print(image[player])

    computer = random.randint(0, 2)
    print(f"Tôi ra:")
    print(image[computer])

    if player == 0 and computer == 2:
        print("Bạn là nhất, được chưa? 🙂")
    elif player == 2 and computer == 0:
        print(("Hahahaha, non! 😏"))
    elif computer > player:
        print("Hahahaha, non! 😏")
    elif player > computer:
        print("Bạn là nhất, được chưa? 🙂")
    elif player == computer:
        print("Khai thiệt đi, bạn hack tôi đúng không? 🙂")
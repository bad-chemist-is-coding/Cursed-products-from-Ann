import random

print("Project 4:\n\t OẲN TÙ TÌ")

while True:
    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''
    paper = '''
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    '''
    scissors ='''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
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

    var = input('Bạn có muốn chơi lại? (Y/N)\n')
    if var.lower().startswith('n'):
        print('Thắng bại tại kỹ năng, khi nào muốn thua thì quay lại nhá 🙂!')
        break
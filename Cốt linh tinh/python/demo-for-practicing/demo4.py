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


input("\n Wanna head to the next project?")
print("\nProject 3:\n\t WHERE'S MY PERRY?")

print("Ôi không, Perry đang bị Tiến sĩ Doofenshmirtz truy đuổi, \nhãy giúp Perry trốn trong các icon sau!")

row1 = ["🏫","🏥","🏰","🗻"]
row2 = ["🗽","🚒","🚀","💉"]
row3 = ["🛁","✈️","🏭","⚽️"]
map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Hãy chọn toạ độ bạn để giấu Perry! (VD: 23 là cột 2 hàng 3)\n")
#Do này là cái số nên khi nhập số vào position thì mỗi ký tự là 1 phần tử trong list (không cần'')
horizontal = int(position[0])
vertical = int(position[1])
map[vertical - 1][horizontal - 1] = "Perry"

print(f"{row1}\n{row2}\n{row3}")
print("Bạn đã thành công giấu Perry!")


input("\n Wanna head to the next project?")
print("\nProject 2:\n\t AI LÀ NGƯỜI ĐƯỢC CHỌN?")

import random

name_string = input("Hãy điền tên mọi người bạn muốn chọn ngẫu nhiên!\nCách nhau bằng dấu phẩy (VD: A, B, C)\n")
name = name_string.split(", ")
num_item = len(name)
choice = random.randint(0,num_item - 1)

print(f"Chúc mừng {name[choice]}! {name[choice]} là người được chọn!")


input("\n Wanna head to the next project?")
print("\nProject 1:\n\t TUNG ĐỒNG XU")

import random

input("Nhấn gì đó để tung!")

flip = random.randint(1,2)
if flip == 1:
    print("Đồng xu bạn tung là ngửa")
else:
    print("Đồng xu bạn tung là úp")
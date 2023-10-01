print("\nProject 2:\n\t AI LÀ NGƯỜI ĐƯỢC CHỌN?")

import random

while True:
    name_string = input("Hãy điền tên mọi người bạn muốn chọn ngẫu nhiên!\nCách nhau bằng dấu phẩy (VD: A, B, C)\n")
    name = name_string.split(", ")
    num_item = len(name)
    choice = random.randint(0,num_item - 1)

    print(f"Chúc mừng {name[choice]}! {name[choice]} là người được chọn!")

    var = input('Bạn có muốn random lại? (Y/N)\n')
    if var.lower().startswith('n'):
        print('Chúc bạn không bị mọi người nghĩ là mình gian lận trong việc random tên!\n(Vì không ai tin là bạn thật sự random đâu)')
        break
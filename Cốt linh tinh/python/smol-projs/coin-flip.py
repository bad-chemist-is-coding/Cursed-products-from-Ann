print("\nProject 1:\n\t TUNG ĐỒNG XU")

import random

while True:
    input("Nhấn gì đó để tung!")


    flip = random.randint(1,2)
    if flip == 1:
        print("Đồng xu bạn tung là ngửa")
    else:
        print("Đồng xu bạn tung là úp")

    var = input('Bạn có muốn tung lại? (Y/N)\n')
    if var.lower().startswith('n'):
        print('Bye! Khi nào muốn quyết định thứ gì đó quan trọng thì quay lại!')
        break
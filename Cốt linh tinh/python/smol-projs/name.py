print("Project 1:\n\tFRIENDLY GREETING")
while True:
    print('Fuck you,'+input("What's your name?\n")+"!")
    input('You feel hurt?\n')
    print("Let's try again")
    print('Fuck you again,'+input("What's your name again?\n")+"!")


    input("\nWanna head to the next project?")
    print("\nProject 2:\n\tẢO THUẬT: ĐOÁN SỐ KÝ TỰ")
    input("Tôi sẽ đoán số ký tự trong tên bạn")
    name=input("Bạn tên là gì?\n")
    length=len(name)

    print("Đáp án là:")
    print(length)
    print("Ghê chưa?")


    input("\nWanna head to the next project?")
    print("\nProject 3:\n\tCÁCH GỌI TÊN")

    last_name = input("Họ của bạn là gì? (VD: Võ)\n")
    middle_name = input("Tên đệm của bạn là gì? (VD: Trương Minh)\n")
    first_name = input("Tên của bạn là gì? (VD:Ánh)\n")

    print("Trong tiếng Anh, tên tiếng Việt của bạn là "+ first_name + " "+middle_name+" "+last_name+"!")

    var = input('Bạn có muốn thử lại? (Y/N)\n')
    if var.lower().startswith('n'):
        print('Chắc bạn không quay lại đâu vì cái này là cái đầu tiên Ánh làm \nnên cũng không có gì hay!')
        break


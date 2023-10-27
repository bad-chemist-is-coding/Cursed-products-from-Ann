print("\nProject 2:\n\t KIỂM TRA NĂM NHUẬN")

while True:
    year = int(input("Enter the year\n"))

    if year % 4 ==0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("LEAP YEAR")
            else:
                print("NOT A LEAP YEAR")
        else:
            print("LEAP YEAR")
    else:
        print("NOT A LEAP YEAR")

    var = input('Bạn có muốn tính lại? (Y/N)\n')
    if var.lower().startswith('n'):
        print('Không nhớ cách tính năm nhuận (kiến thức rất cơ bản) thì quay lại nhé!')
        break
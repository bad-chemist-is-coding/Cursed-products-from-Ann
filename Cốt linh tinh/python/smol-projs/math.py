print("Project 1:\n\t MÁY TÍNH TÍNH TRUNG BÌNH")

while True:
    values = input("Hãy nhập các giá trị mà bạn muốn tính trung bình\n").split()
    for n in range (0, len(values)):
        values[n] = int(values[n])
    #Chức năng hàm sum
    total = 0
    for va in values:
        total += va
    #Chức năng hàm len
    quantity = 0
    for number in values:
        quantity +=1
    a = total/quantity
    print(f"Vậy trung bình là {a}")

    var = input('Bạn có muốn tính lại? (Y/N)\n')
    if var.lower().startswith('n'):
        print('Học cách tính trung bình đi, không học vô thì quay lại tính nhé!')
        break
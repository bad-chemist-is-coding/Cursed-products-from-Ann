print("Project 1:\n\t MÁY TÍNH TÍNH TRUNG BÌNH")

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

input("\nWanna head to the next project?")
print("\nProject 2: \n\tFIZZBUZZ")
input("For those numbers divisible by 3, it would be Frizz.\n "
      "For those divisible by 5, it would be Buzz.\n"
      "For those with 3 and 5, it would be FizzBuzz.")
for number in range (0, 101, 1):
    if number % 3 == 0:
        print("Frizz")
    elif number % 5 ==0:
        print("Buzz")
    elif number % 3 == 0 and number % 5 ==0:
        print("FrizzBuzz")
    else:
        print(number)

input("\nWanna head to the next project?")
print("\nProject 3:\n\t LỰA CHỌN MẬT DANH ")
input("POV: Bạn là điêp viên nghiệp dư bắt đầu tự chọn tên hành nghề.\nHãy dùng bộ máy này để lựa chọn tên siêu ngầu!")

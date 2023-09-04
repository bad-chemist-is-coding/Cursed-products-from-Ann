
"""
OUTPUT
"""
"""CÁC LOẠI OUTPUT
a = 'Hello World!'
print(a)
a = 1.34
a = 1
a = True

#### METHOD
b = 'Bonjour tout la monde'
## Upper/ Lower / Title
print(b.title()) #Viết Hoa Chữ Đầu
print(b.lower()) #viết thường tất cả
print(b.upper()) #VIẾT HOA TẤT CẢ
print(b.isupper()) #True nếu tất cả chữ trong ele viết hoa
## Thay thế
print(b.replace('Bonjour','Hello')) #Thay thế ele = ele ở vị trí chỉ định
print(b+', Je suis Ann') #Thêm ele vào ele sẵn có (đầu hoặc cuối)
print(f'Je parle "{b}" avec lui') #Thêm ele vào giữa ele
print('Je parle "{}" avec elle et elle parle "{}" avec moi aussi!'.format(b,b)) #Thêm nhiều ele (và nhiều loại ele) trong ele mới
print('Je vois elle et je parle \n \t- {}! \nEt elle ri'.format(b)) # \n = new line; \t = tab

### FUNCTION
print(len(b))

### NUMBER
num1=1 #Integer
num2=2
num3=3
num4=4.2043 #float: số thập phân
## Caluculation
print(num1+num2)
print(num1-num2)
print(num2/num3)
print(num2//num3) #Chia lấy phần nguyên
print(num1*num3)
print(num2%num3) #Chia lấy phần dư
print(pow(num3,2)) #num3 mũ 2
print(num3 ** num2)
#Mức độ ưu tiên tính toán: ngoặc > mũ > nhân > chia > cộng > trừ
#Phép tính tính từ bên trái qua

## Max min value
print(max(num1, num4)) #giá trị lớn nhất trong các num được nhập
print(min(num1, num4))  #giá trị nhỏ nhất trong các num được nhập

print(round(num4), 2) #làm tròn số thập phân num4 tròn 2 chữ số thập phân
##Change value category
print(int(num4)) #Chuyển số thập phân sang số nguyên
print(float(num1)) #Chuyển số nguyên sang số thập phân
print(str(num1)) #Chuyển số nguyên thành chuỗi (không thể thực hiện phép tính)

### LIST
##Index
c = ['English', 'Vietnamese','French', 10, 3.14, True, False]
#!!!Python đếm list từ số 0
print(c[2]) #value thứ 2 trong list
print(c[True]) #True = 1, False = 0 ==> Hiện value thứ 1 ==> Vietnamese
print(c[5])
print(c[-3]) #Đếm ngược list từ cuối lên đầu
print(c[1: 5]) #Hiện các value chỉ mục từ 1 đến 4 (số value - 1)
print(c[-1: 3]) #Không cùng hướng xét nên output rỗng
#List adjustment
d = ['Vo','Trương','Minh','Anh', 7, 1.2004]
d.append('Kee') #Thêm ele vào cuối list
print(d)
d.insert(2, 'Rii') #Thêm ele vào vị trí chỉ mục trong list
print(d)
d. extend(c)
print(d) #Thêm list c vào list d
d.remove('Kee') #Phải chỉ ra đối tượng để loại bỏ
print(d)
d.pop(2) #Loại bỏ ele chỉ mục 2
print(d)
## Arrange
e = [1, 45, 23, 90, 12, 35, 99, 58]
e.sort() #Sắp xếp từ bé đến lớn
print(e)
e.reverse() #Sắp xếp từ lớn đến bé
print(e)
print(e.count(23)) #Tìm số lần ele được chỉ định xuất hiện trong list
"""



"""
Python basic codes
"""

"""1: INPUT - OUTPUT
print("Hello "+input("What's your name?\n")+"!")
###Python variables
name=input("What is your name?\n")
lenght=len(name)
print(lenght)"""

"""2: CALCULATION
print("123"+"345") #""=string
print(123+345) #Integer
print(3.1435) #Float
print(True, False) #Boolean
""""""Common error:
num_char = len(input("What is your name?"))
print("Your name has " + num_char + " characters.")
==> numbers don't work well with string
"""
"""num_char = len(input("What is your name?"))
print(type(num_char)) #hiển thị loại biến để kiểm tra loại biến
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")
score = 0
score += 1 #có nghĩa là giá trị score 0 sẽ +1 = 1)
print(score)
"""


"""3: FLOW
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))
## dùng = để gán giá trị, dùng == để so sánh hai giá trị bằng nhau
if height > 120: #> < >= <=
    print("You can play")
    age = int(input("How old are you?\n"))
    bill = 0
    if age < 12:
        bill=5
        print("Pay 5$")
    elif age <= 18:
        bill = 10
        print("Pay 10$")
    elif age >= 45 and age <60:
        print("Free")
    else:
        bill = 15
        print("Pay 15$")
    #Có thể dùng nhiều elif tuỳ thích
    want_photo= input("Want a photo taken? Y or N")
    if want_photo == "Y": #if này là kiểu additional thôi, nếu giá trị khác Y là nó sẽ nhảy xuống else ở dưới, ko cần ghi thêm else nữa.
        bill += 3
    print(f"Final bill is {bill}")
else:
    print("Fuck off")

#if/elif/else: A or B or C
# if condi1:
#   do A
# elif condi2:
#   do B
# else:
#   do C

#multiple if: A and B and C
# if condi1:
#   do A
# if condi2:
#   do B
# if:
#   do C

a = int(input("Choose your number to check\n"))
if a % 2 == 0:
        print("Even")
else:
        print("odd")
#Logical operation:
# A and B: A false ==> FALSE
# C or D: C and D false ==> FALSE
# not E: E true ==> FALSE
"""

"""4: RANDOM
import demo4_mymodule #import một file python khác vào file python này
print(demo4_mymodule.pi) #print ele pi trong file module

import random
random_integer = random.randint(1, 10) #Random số nguyên từ 1 đến 10
print(random_integer)
random_float = random.random() #Random số thập phân (0;1)
print(random_float)
random_Float = random.random() * 5 #Random số thập phân (0;5)
print(random_Float)

item_string = input("Give me items in your room, seperated by a comma.")
item = item_string.split(", ") #Tách tạo các ele trong list mình nhập cách nhau bằng dấu phẩy.
item_quantity = len(item)
import random
random_item = random.randint(0,item_quantity-1) #Do list bắt đầu từ 0
print(item[random_item])"""

###LOOP
fruits = ["Apple","Peach","Pear"]
for fruit in fruits:
    print(fruit) # Gán giá trị 3 lần và in 3 lần
    print(fruit + "Candy")

student_score = input("List of students' scores\n").split( )
for n in range(0, len(student_score)):
    student_score[n] = int(student_score[n])
print(student_score)
highest_score=0
for score in student_score:
    if score > highest_score:
        highest_score = score
print(f"The highest score is {highest_score}")
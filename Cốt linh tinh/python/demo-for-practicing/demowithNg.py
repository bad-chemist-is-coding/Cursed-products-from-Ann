def Hi():
    print("bonjour")
#có thể dùng end để không cho cái dòng xuống dòng
    print('Hello!', end=' ')
    print('Ánh')

a = 10
b = 20
def sum(first_arguement, second_arguement):
    return first_arguement + second_arguement

print(sum(a,b))

def hello(name):
    print(f'Chào con chó {name}')

hello('Nguyên')

name = "Nguyen Khung" #Global variatble

def ten():
    name = "Nguyen dien"
    print(name)

print(name)


# def gt(num):
#     rs = 1
#     for i in range (1, num+1):
#         rs = rs * i
#     return rs
#
# num = int(input())
# print(gt(num))

# def sum(num):
#     result = 0
#     for i in range (1, num+1):
#         result = result + i
#     return result
#
# num = int(input())
# print(sum(num))

def divisible(num):
        divide = num % 2
        if divide == 0:
            return True
        else:
            return False
num = int(input())
print(divisible(num))

#def thường cho repetive

# #Project
# def greet():
#     print('Xin chào')
#     print('Hello')
#     print('Bonjour')
# greet()
#
# #Function with input
# def greet_name (name):
#     print(f'Hello {name}')
# greet_name(input())
#
# #Function with more than 1 input
# def greet_with(ten, vitri):
#     print(f'Hello {ten}, you are at {vitri}')
# greet_with('Anh', 'home')
# greet_with(ten = 'Anh', vitri = 'home')
"""
#Project 2: Prime number checker
def prime(number):
    is_prime = True
    for i in range (2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number")
    else:
        print("It's not a prime number")

n = int(input())
prime(number=n)
"""
#Project 3: Caesar Cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'
            , 'm', 'n', 'o', 'p','q','r','s', 't', 'u', 'v', 'w', 'x'
            , 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'
            , 'm', 'n', 'o', 'p','q','r','s', 't', 'u', 'v', 'w', 'x'
            , 'y', 'z']
print('\nGIẢI MÃ HAY BỊ GIẢI MÃ\n\n')



def caesar(start_text, shift_amount, cipher_direction):
    end_text = ('')
    if cipher_direction == 'B':
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f'Mã của bạn dịch theo kiểu {cipher_direction} là {end_text} ')

# def encrypt(plain_text, shift_amount):
#     cipher_text = ''
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         cipher_text += alphabet[new_position]
#     print(f'Mã của bạn là {cipher_text}!')
# def decrypt(cipher_text, shift_amount):
#     plain_text = ''
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         plain_text += alphabet[new_position]
#     print(f'Mã của bạn dịch ra là {plain_text}!')
#
# if direction == "a":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "b":
#     decrypt(cipher_text=text, shift_amount=shift)
should_continue = True
while should_continue:
    direction = input("Muốn 'Mã hoá'(A) hay 'Giải mã'(B)? (A/B)\n").upper()
    text = input("Gõ nội dung (Không dấu nếu tiếng việt):\n").lower()
    shift = int(input("Bạn muốn chữ bị xê dịch bao nhiêu chữ:\n"))
    shift = shift % 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    result = input('Bạn muốn thử lại? (Y/N)\n').upper()
    if result == 'N':
        should_continue = False
        print('Au Revoir!')

""""
# Practice 1:
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 100 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leap(year):
        return 29
    else:
        return month_days[month - 1]

year = int(input('Enter a year: '))
month = int(input('Enter a month: '))
days = days_in_month(year, month)
print(days)
"""
# Practice 2
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = int(input('Số đầu: '))
num2 = int(input('Số sau: '))

for symbol in operation:
    print(symbol)
operation_symbol = input('Chọn một ký hiệu: ')
calculation_function = operation[operation_symbol]
answer = calculation_function(num1, num2)

print(f'{num1} {operation_symbol} {num2} = {answer}')

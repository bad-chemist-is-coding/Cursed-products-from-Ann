print("\nProject 3:\n\t WHERE'S MY PERRY?")

print("Ôi không, Perry đang bị Tiến sĩ Doofenshmirtz truy đuổi, \nhãy giúp Perry trốn trong các icon sau!")

row1 = ["🏫","🏥","🏰","🗻"]
row2 = ["🗽","🚒","🚀","💉"]
row3 = ["🛁","✈️","🏭","⚽️"]
map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Hãy chọn toạ độ bạn để giấu Perry! (VD: 23 là cột 2 hàng 3)\n")
#Do này là cái số nên khi nhập số vào position thì mỗi ký tự là 1 phần tử trong list (không cần'')
horizontal = int(position[0])
vertical = int(position[1])
map[vertical - 1][horizontal - 1] = "Perry"

print(f"{row1}\n{row2}\n{row3}")
print("Bạn đã thành công giấu Perry!")
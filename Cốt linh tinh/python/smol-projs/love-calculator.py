print("\nProject 4:\n\tHAI BẠN CÓ HỢP NHAU KHÔNG???")

your_name = input("Bạn tên gì? (2 từ không dấu)\n")
their_name = input("Crush bạn tên gì? (2 từ không dấu)\n")
name = your_name + their_name
low_name = name.lower()
#Cách tính điểm: Xét số chữ cái trong TRUE (hàng chục của điểm) LOVE (hàng đơn vị của điểm) xuất hiện trong tên của bạn và người ấy
t = low_name.count("t")
r = low_name.count("r")
u = low_name.count("u")
e = low_name.count("e")
chuc = str(t+r+u+e)
l = low_name.count("l")
o = low_name.count("o")
v = low_name.count("v")
e = low_name.count("e")

don_vi = str(l+o+v+e)
kq = int(chuc + don_vi)

if kq < 10 or kq > 90:
    print(f"Điểm tình yêu của bạn là {kq}! Quay xe đê bạn êi!!")
elif 40 < kq < 50:
    print(f"Điểm tình yêu của bạn là {kq}! Tiến tới đê bạn êi!!")
else:
    print(f"Điểm tình yêu của bạn là {kq}! Cũng bình thường, hên xui!")
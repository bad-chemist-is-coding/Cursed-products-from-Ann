print("Project:\n\t TÍNH THỜI GIAN CHẠY DEADLINE")
x = int(input("Bạn có bao nhiêu ngày để chạy deadline?\n"))
a = float(input("Để ngủ?\n"))
b = float(input("Để ăn?\n"))
c = float(input("Để di chuyển giữa các nơi?\n"))
d = float(input("Để nghỉ ngơi?\n"))
e = float(input("Để rơi vào trầm tư?\n"))

n=a+b+c+d+e
m=n-24
o=24-n
y=x*o

t = str(n)
u = str(m)
v = str(o)
q = str(y)
z = str(x)

print("Một ngày bạn dùng bao nhiêu tiếng")

if n>24:
    print("Bạn sống kiểu gì mà thiếu tận "+u+" tiếng một ngày dữ vậy?!")
    print("Khỏi chạy deadline đi má!")
else:
    print(f"Mỗi ngày bạn dành {t} tiếng để sống như người bình thường")
    print(f"Bạn nên dành {v} tiếng mỗi ngày để chạy deadline.")
    print(f"Bạn sẽ dành tổng cộng {q} tiếng để chạy kịp deadline trong {z} ngày!")


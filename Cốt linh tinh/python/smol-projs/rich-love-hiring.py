print("\nProject 3:\n\tTUYỂN ĐẠI GIA")

chon = input("Bạn muốn (1) Phú bà, (2) Phú ông hay (3) Đại gia hấp hối?\n(Chọn 1,2 hoặc 3)\n").lower()
goi_thang = input("Bạn có muốn đại gia của mình bao trọn gói tháng không?\n(Chọn Y (có) hoặc N (không)\n").lower()
dep = input("Bạn có chắc chắn muốn đai gia của mình là mỹ nữ/soái ca không?\n(Chọn Y (có) hoặc N (không)\n").lower()
gia = 0
if chon == "1":
    gia += 50
    print(f"Dịch vụ phú bà có giá là {gia} triệu!")
elif chon == "2":
    gia += 40
    print(f"Dịch vụ phú ông có giá là {gia} triệu!")
elif chon == "3":
    gia += 100
#Gói tháng
if goi_thang == "y":
    gia += 50
    print(f"Bạn đã trả thêm 50 triệu để người yêu của bạn sẽ bao bạn trọn gói tháng.")
    #Đẹp
if dep == "y":
    gia += 100
    print("Bạn đã trả thêm 100 triệu để người yêu của bạn đẹp tuyệt trần!")

print(f"Tổng tiền của cậu là {gia} triệu đồng/tháng.")
print("Chúc cậu sớm giàu cùng đại gia của mình!")
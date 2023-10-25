print("Project 5:\n\t GAME: LÀM LAB CÙNG ÁNH!")
print("Hãy cùng Ánh làm thí nghiệm nhé, "+input("Bạn tên là gì?\n")+"!")
print(input("Đừng để bị đuổi khỏi lab!"))

cau1 = input("Trưởng lab Ánh muốn bạn làm trợ lí trung thành. (Chọn Y/N)\n").lower()
if cau1 == "n":
    print("Ánh đã giận.\nÁnh đuổi bạn khỏi lab.\n\t GAME OVER!")
elif cau1 == "y":
    cau2 = input("Ánh hỏi bạn muốn làm thí nghiệm nào?\n\tA. Làm thí nghiệm chuẩn độ.\n\tB. Làm thí nghiệm điều chế SO2\n\tC. Làm bồ Ánh\n").lower()
    if cau2 == "c":
        print("Bạn đã chơi đùa tình cảm với Ánh.\n\tÁnh giận.\nÁnh đuổi bạn khỏi lab\n\tGAME OVER")
    elif cau2 == "b":
        cau2_2 = input("Bạn và Ánh đang đốt cháy lưu huỳnh. Khí bốc ra dữ dội.\nBạn đánh rơi nắp. Giờ cả lab nồng nặc mùi SO2.\n Bạn sẽ làm gì?\n\tA. Bỏ chạy\n\tB. Đóng nắp\n").lower()
        if cau2_2 == "a":
            print("Bạn bỏ chạy để lại Ánh bị ngất trong lab.\nBạn quên tắt đèn cồn nên lab bắt lửa.\nLab bị cháy, Ánh cũng vậy.\nGiờ thì không còn Ánh để đuổi bạn khỏi lab nữa!\n\t BẠN ĐÃ THẮNG!")
        elif cau2_2 == "b":
            print("Bạn bình tĩnh đóng nắp. Ánh hú hồn chim ém.\nÁnh đuổi bạn khỏi lab!\n\t GAME OVER")
        else:
            print("Có chọn đúng cú pháp bạn cũng không làm được nữa, nói chi làm thí nghiệm?\nÁnh đuổi bạn khỏi lab!\n\t GAME OVER")
    elif cau2 == "a":
        cau2_3 = input("Ánh chuẩn bị đầy đủ dụng cụ như hồi học lab hoá đại cương ở Bách Khoa.\nÁnh nhờ bạn lấy đồ.\nBạn sẽ đưa gì?\n\tA. Burette\n\tB. NaOH\n").lower()
        if cau2_3 == "a":
            cau2_3_2 = input("Ôi không!\nBạn đã làm vỡ burette!\nBạn sẽ làm gì?\n\tA. Bỏ chạy\n\tB. Đền tiền\n\tC. Bị thương\n").lower()
            if cau2_3_2 == "a":
                print("Bạn bỏ chạy lấy thân. Bạn để Ánh đền tiền.\nBạn không chỉ bị Ánh đuổi khỏi lab mà còn bị Ánh truy sát.\n\t GAME OVER")
            elif cau2_3_2 == "b":
                print("Bạn đền 1 triệu VND cho cái burette. Bạn giờ đã hết tiền.\nBạn đã hết giá trị với Ánh.\nÁnh đuổi bạn khỏi lab.\n\t GAME OVER")
            elif cau2_3_2 == "c":
                print("Bạn đòi kiện lab Ánh vì chiếc burette của lab đã làm bạn thương.\nÁnh nghèo nên không có tiền đền bù tổn hại của bạn nên Ánh đã hứa không đuổi bạn khỏi lab để bạn không kiện.\n\t BẠN ĐÃ THẮNG!")
            else:
                print("Có chọn đúng cú pháp bạn cũng không làm được nữa, nói chi làm thí nghiệm?\nÁnh đuổi bạn khỏi lab!\n\t GAME OVER")
        if cau2_3 == "b":
            cau2_3_3 = input("Ôi không!\nBạn đã đưa nhầm lọ axit sulfuric đậm đặc cho Ánh.\nDung dịch lỡ dính vào tay Ánh và Ánh đang bị bỏng.\nBạn sẽ làm gì?\n\tA. Lỡ rồi tạt luôn axit vào Ánh\n\tB. Hoảng loạn sơ cứu Ánh\n").lower()
            if cau2_3_3 == "a":
                input("Ánh đã nhập viện.\nVà không còn ai làm trưởng lab nữa nên bạn trở thành trưởng lab và không bị đuổi khỏi lab. Nhưng...")
                input("Bạn nghĩ bạn thắng rồi ư?")
                print("Ánh xuất viện và truy sát bạn, lấy lại danh hiệu trưởng lab.\nBạn bị Ánh đuổi khỏi lab và truy sát.\n\t GAME OVER")
            elif cau2_3_3 == "b":
                print("Bạn sơ cứu Ánh.\nÁnh ghim bạn vì đã đưa nhầm lọ.\nÁnh đuổi bạn khỏi lab.\nTuy nhiên, bạn đã chiến thắng con quỷ bên trong mình để cứu Ánh!\n\t BẠN ĐÃ THẮNG!")
            else:
                print("Có chọn đúng cú pháp bạn cũng không làm được nữa, nói chi làm thí nghiệm?\n Ánh đuổi bạn khỏi lab!\n\t GAME OVER")
    else:
        print("Có chọn đúng cú pháp bạn cũng không làm được nữa, nói chi làm thí nghiệm?\nÁnh đuổi bạn khỏi lab!\n\t GAME OVER")
else:
    print("Có chọn đúng cú pháp bạn cũng không làm được nữa, nói chi làm thí nghiệm?\nÁnh đuổi bạn khỏi lab!\n\t GAME OVER")


input("\nWanna head to the next project?")
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


input("\nWanna head to the next project?")
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


input("\nWanna head to the next project?")
print("\nProject 2:\n\t KIỂM TRA NĂM NHUẬN")

year = int(input("Enter the year\n"))

if year % 4 ==0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("LEAP YEAR")
        else:
            print("NOT A LEAP YEAR")
    else:
        print("LEAP YEAR")
else:
    print("NOT A LEAP YEAR")


input("\nWanna head to the next project?")
print("\nProject 1:\n\t KIỂM TRA BMI")

weight = float(input("How fat are you (kg)?\n"))
height = float(input("How short are you (m)?\n"))
bmi = round( weight / height ** 2 )

if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are a skeleton! (underweight)")
elif bmi < 25:
    print(f"Your bmi is {bmi}, you are a person! (normal weight)")
elif bmi < 30:
    print(f"Your bmi is {bmi}, you better save your ass with diets! (overweight")
elif bmi < 35:
    print(f"Your bmi is {bmi}, you need to save your ass with diets! (obese)")
else:
    print(f"You bmi is {bmi}, you must save your ass with diets!!! (clinically obese")
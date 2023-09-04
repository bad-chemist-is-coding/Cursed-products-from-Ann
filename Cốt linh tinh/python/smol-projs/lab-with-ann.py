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
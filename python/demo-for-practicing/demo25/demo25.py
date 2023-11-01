# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data) # Nếu vậy thì không xoá được dấu , với SPACE

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     # print(data) # Tạo một oop
#     temperatures = []
#     for row in data:
#         # print(row)  # Phân tách từng element thành string luôn, in ra row
#         # print(row[1]) # In row là luôn cái tên "temp"
#         if row[1] != "temp":
#             # temperatures.append(row[1]) # Chỉ lấy các số ở dạng str
#             temperatures.append(int(row[1])) # Lấy số ở dạng int
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data) # Output một bảng dữ liệu cực đẹp
# print(type(data)) # Kiểm tra kiểu dữ liệu của loại dữ liệu này lấy lại từ pandas
# # DataFrame: cái bảng data
# print(type(data["temp"]))
# Series: tương đương với list, vd như cột
# print(data["temp"]) # In ra cột temp || Gọn hơn method bên trên

data_dict = data.to.dict()
print(data_dict)






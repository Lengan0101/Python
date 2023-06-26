import datetime

x = datetime.datetime.now()

print(x.year) # hiển thị năm
print(x.strftime("%A")) # hiển thị thứ

# tạo đối tượng ngày tháng

x = datetime.datetime(2020, 5, 17)

# print(x)
print(x.strftime("%B")) # hiển thị tên tháng


# strftime(): phương thức được gọi là, và lấy một tham số, để chỉ định định dạng của chuỗi trả về


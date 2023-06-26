# x = "awesome"
# # để tạo một biến toàn cục bên trong 1 hàm, bạn có thể sử dụng từ khóa. global
# Hàm _Init_(), hàm này luôn được thực thi khi lớp học đang được bắt đầu
# sử dụng hàm _init_() để gán giá trị cho thuộc tính đối tượng hoặc khác
# def myfunc():
#     global x
#     x = "fantastic"
# #    print("Python is " + x)
    
# myfunc()

# print("Python is " + x)

# def myfunc(n):
#     return lambda a : a * n

# mydoubler = myfunc(2)
# mytripler = myfunc(3)

# print(mydoubler(11))
# print(mytripler(11))

# class Person:
#     def _init_(self, name, age):
#         self.name = name
#         self.age = age
        
#     def _str_(self):
#         return f"{self.name}({self.age})"
# p1 = Person("John", 36)
    
# print(p1)    

# class Person:
#     def _init_(self, name, age):
#         self.name = name
#         self.age = age
        
#     def myfunc(self):
#         print("Hello my name is "+ self.name)
        
# p1 = Person("John", 36)
# p1.myfunc()

# Hàm _str_() kiếm soát những gì sẽ được trả về khi đối tượng lớp được biểu diễn dưới dạng chuỗi

# class Person:
#     def _init_(self, name, age):
#         self.name = name
#         self.age = age

# p1 = Person("John", 36)

# print(p1)

class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age
        
    def _str_(self):
        return f"{self.name}({self.age})"
    
p1 = Person("John", 36)

print(p1)


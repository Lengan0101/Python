# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
        
#     def printname(self):
#         print(self.firstname, self.lastname)
        
#     # use the Person class to create an object, and then execute the printname method:
    
# x = Person("John", "Doe")
# x.printname()


# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
        
#     def printname(self):
#         print(self.firstname, self.lastname)
        
# class Student(Person):
#     def __init__(self, fname, lname, year):
#         super().__init__(fname, lname)
#         self.graduationyear = year
        
#     def welcome(self):
#         print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
            
        
# x = Student("Mike", "Olsen", 2019)
# x.welcome()

# mytupe = ("apple", "banana", "cherry")
# myit = iter(mytupe)

# print(next(myit))
# print(next(myit))
# print(next(myit))

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
    print(x)
    
# lặp qua ký tự của một chuỗi:
mystr = "banana"
for x in mystr:
    print(x)
    
# __iter__() bạn phải thực hiện các phương thức và cho đối tượng của bạn
# phương pháp hoạt động tương tư, bạn có thể thực hiện các tháo tác(khởi tạo, v.v),
# nhưng phải luôn trả về đối tượng iterator Bản thân

# __next__(): phương pháp này cũng cho phép bạn làm hoạt động, và phải trả về mục tiếp theo trong chuỗi
    
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else: 
            raise StopIteration
    
myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)

#stoplteration: để ngăn việc lặp lại diễn ra mãi mãi

# đa hình Python

# đối với chuỗi trả về số ký tự: len()

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(len(thisdict))

# đa hình lớp
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def move(self):
        print("Drive!")
        
class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def move(self):
        print("Sail!")
        
class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def move(self):
        print("Sail!")
        
class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def move(self):
        print("Fly!")
        
car1 = Car("Ford", "Mustang") # create a Car class
boat1 = Boat("Ibiza", "Touring 20") # create a Boat class
plane1 = Plane("Boeing", "747") #create a Plane class

for x in (car1, boat1, plane1):
    x.move()

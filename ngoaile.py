# define Python user-defined exceptions
# class InvalidAgeException(Exception):
#     "Raised when the iput value is less than 18"
#     pass

# # you need to gues this number

# number = 18

# try :
#     input_num = int(input("Enter a number: "))
#     if input_num < number:
#         raise InvalidAgeException
#     else:
#         print("Eligible to vote")
        
# except InvalidAgeException:
#     print("Exception occurred: Invalid age")

# tùy chỉnh các lớp trong Python

class SalaryNotInRangeError(Exception):
    def __init__(self, salary, message = "salary ís not in (5000, 15000) range"):
        self.salary = salary
        self.message = message
        super(). __init__(self.message)
        
salary = int(input("Enter salary amount: "))
if not 5000 < salary < 15000:
    raise SalaryNotInRangeError(salary)
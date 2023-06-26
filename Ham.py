# Ham Python

# def function_name(arguments):
#     # funcition body
    
#     return
# def - từ khóa dùng để khai báo một hàm
# function_name -  bất kỳ tê nào được đặt cho hàm
# arguments -  bất kỳ giá trị nào được truyền vào hàm
# return (tùy chọn) - trả về giá trị từ một hàm

# đối số hàm Python

#function with two arguments
# def add_numbers(num1, num2):
#     sum = num1 + num2
#     print("Sum: ", sum)

# #function call with two values
# add_numbers(5, 4)

# #output: Sum: 9

# function definition
# def find_square(num):
#     result = num * num
#     return result

# # function call
# square = find_square(3)

# print('Square:', square)

# # Output: Square: 9

# function that adds two numbers
# def add_numbers(num1, num2):
#     sum = num1 + num2
#     return sum

# # calling function with two values
# result = add_numbers(5, 4)

# print('Sum: ', result)

# # output: Sum: 9

# print() - in chuỗi bên trong dấu ngoặc kép
# sqrt() - trả về căn bậc hai của một số
# pow() - trả về lũy thừa của một số

# import math

# # sqrt computes the square root
# square_root = math.sqrt(4)

# print("square root of 4 is", square_root)

# #pow() comptes the power
# power = pow(2, 3)

# print("2 to the power 3 is", power)

# function defimition
# def get_square(num):
#     return num * num

# for i in [1,2,3]:
#     # function call
#     result = get_square(i)
#     print('Square of', i, '=', result)


# đối số hàm với các giá trị mặc định

# def add_numbers(a = 7, b = 8):
#     sum = a + b
#     print('Sum: ', sum)
    
# #function call with two arguments
# add_numbers(2, 3)

# # function call with one argument
# add_numbers(a = 2)

# #function call with no arguments
# add_numbers()

# ham Python voi cac doi so tuy y

# program to find sum of multiple numbers

def find_sum(*numbers):
    result = 0
    
    for num in numbers:
        result = result + num
        
    print("Sum = ", result)
    
# function call with 3 arguments
find_sum(1, 2, 3)

# function call with 2 arguments
find_sum(4, 9)



#number = 5

#outer if statement
#if (number >= 0):
    # inner if statement
#    if number == 0:
#        print('Number is 0')
        
    #inner else statement
#    else:
#        print('Number is positive')
        
#outer else statement
#else:
#    print('Number is negative')
    
# Output: Number is posutive

# use of range() to define a range of values
#values = range(4)

#iterate from i = 0 to i = 3
#for i in values:
#    print(i)
    
#python trong khi Loop
# program to display numbers from 1 to 5

# initialize the variable
# i = 1
# n = 5
# # while loop from i = 1 to 5
# while i <= n:
#     print(i)
#     i = i + 1
    
    
#python trong khi Loop
#program to calculate the sum of numbers
# until the user enters zero

# total = 0
# number =  int(input('Enter a number: '))

# # add numbers until number is zero

# while number != 0:
#     total += number #total = total + number
    
#     #take integer input again
#     number = int(input('Enter a number: '))
    
    
# print('total =', total)

# vô hạn trong khi loop trong Python

# age = 32
# # the test condition is always True
# while age > 18:
#     print('You can vote')

# python trong khi vòng lặp với người khác

# counter = 0

# while counter < 3:
    
#     print('Inside loop')
#     counter = counter + 1
# else:
#     print('Inside else')

# counter = 0
# while counter < 3:
#     # loop ends because of break
#     # the else part is not executed
    
#     if counter == 1:
#         break
    
#     print('Inside loop')
#     counter = counter + 1
# else:
#     print('Inside else')
    
    
# python phá vỡ câu lệnh với while Loop
#program to find first 5 multiples of 6
# i = 1

# while i <= 10:
#     print('6 * ',(i), '=', 6 * i)
    
#     if i >= 5:
#         break
    
#     i = i + 1
    
# for i in range(5):
#     if i == 3:
#         continue
#     print(i)

# python tiep tuc statement voi while loop
#program to print odd numbers from 1 to 10

num = 0

while num < 10:
    num += 1
    
    if (num % 2) == 0:
        continue
    print(num)
    

# # ham Python lambda

# # declare a lambda function
# greet = lambda : print('Hello world')

# #call lambda function
# greet()

# #output: hello world

# program to double each item in a list using map()

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x * 2, my_list))

print(new_list)

#output: [2, 10, 8, 12, 16, 22, 6, 24]
# different types of tuples

# Empty tuple
my_tuple = ()
print(my_tuple)

#Tuple having itergers
my_tuple = (1, 2, 3)
print(my_tuple)

#tuple having integers
my_tuple = (1, "Hello", 3.4)
print(my_tuple)

#nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)

#type()

var1 = ("hello")
print(type(var1)) # <class 'str'>

# creating a tuple having one element
var2 = ("hello",)
print(type(var2)) # <class 'tuple'>

#parentheses is optional
var3 = "hello",
print(type(var3)) # <class 'tuple'>

# accessing tuple elements using negative indexing
letters = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

print(letters[-1]) #print 'z'
print(letters[-3])

print(letters[1:4]) # print ('r', 'o', 'g')

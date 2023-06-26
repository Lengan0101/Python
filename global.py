# global variable
c = 1
def add():
    # use of global keyword
    global c
    
    #increment c by 2
    c = c + 2
    
    print(c)
    
add()

#output: 3

# hàm lồng nhau

def outer_function():
    num = 20
    
    def inner_function():
        global num
        num = 25
        
    print("Before calling inner_function(): ", num)
    inner_function()
    print("After calling inner_function(): ", num)
    
outer_function()
print("Outside both function: ", num)
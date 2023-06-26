# try:
# #open a file
#     file1 = open("text.txt", "r")

# # read the file
#     read_content = file1.read()
#     print(read_content)

# finally:
# #close the file
#     file1.close()

with open("text.txt", "r") as file1:
    read_content = file1.read()
    print(read_content)
    
with open("text.txt", "w") as file1:
    
    file1.write('Programming is Fun.')
    file1.write('Programiz for beginners')
    
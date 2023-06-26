# đọc nọi dung của tệp
# f = open("read.txt","r")
# print(f.read())

# trả về 5 ký tự đầu tiên của tệp:
f = open("read.txt","r")
# print(f.read(5))
# # đọc dòng đầu tiên
# print(f.readline())
# print(f.readline())

# for x in f:
#     print(x)

# print(f.readline())
# f.close()

f.write("Now the file has more content")
f.close()

#open and read the file after the appending:
f = open("read.txt", "r")
print(f.read())
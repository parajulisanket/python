# readfile.
# open function = opens a file, and returns it as a file object.
# read method = reads the entire file and returns the string.
# seek method = to change the position of the cursor.
# tell method = it gives the position of the cursor.
# readline method = reads one entire line from the file.
# readlines method = read all the lines at single go and then return them as each line a string element in a list.
# close method = it close the file
# with open = while using this we should not use close. It closes the file automatically.
# write method = allows us to write data in a file.
# append method = append method is used in write method to append new string in file.
# read and write(r+) = This method opens file for both read and write.


# ---------------using .read method----------------
# f = open('file1.txt')
# print(f.read()) 
# f.close()

# ---------------using .tell method----------------
# f = open('file1.txt')
# print(f.read())
# print("The position of the cursor is:",f.tell())
# f.close()

# ---------------using .seek method----------------
# f = open('file1.txt')
# print(f.read())
# print("The position of the cursor is:",f.tell())
# f.seek(0)
# print(f.read())
# f.close()

# ---------------using .readline method----------------
# f = open('file1.txt')
# print(f.readline())
# f.close()

# ---------------using .readlines method----------------
# f = open('file1.txt')
# lines = f.readlines()
# print(len(lines))
# for i in lines:
#     print(i) 
# f.close()

# ---------------using .(with open) method----------------

# with open('file1.txt') as f:
#     data = f.read()
#     print(data)
# print(f.closed)

# ------------------------write----------------------

# ---------------using .write(w) method----------------
# with open('file2.txt' , 'w') as f:
#     f.write('hello!!')


# ---------------using .append(a) method----------------

# with open('file1.txt','a') as f:
#     f.write('\nIt is very enjoyable.')


# with open('file2.txt','a') as f:
#     f.write('\nMy name is Sanket.')


# ---------------using .read and write(r+) method----------------

# with open('file3.txt', 'r+') as f:
#     f.seek(len(f.read()))
#     f.write('\nHi')
#     f.write('\nHow are you?')


# ---------------using .read(r) and write(w) method----------------VVI---

# with open('file1.txt','r') as rf:
#     with open('file4.txt','w') as wf:
#         wf.write('HI\n')
#         wf.write(rf.read())
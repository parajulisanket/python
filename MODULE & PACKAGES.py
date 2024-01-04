# MOdule :
    # resuable logic, organized code

# Package:
    # collection of module

# Alias (as):
    # Nickname given to module/package.

# PIP (Python Istall Package)
    # Python Package Manager. Install, Uninstall and Update.

# import webbrowser 
# title = input('enter the song')
# webbrowser.open(f'https://www.youtube.com={title}')


#------------------------------------------------
# import pywhatkit

# number = input("enter your number")
# for num in number:
#     pywhatkit.sendwhatmsg(num,'hello',12,4)


#------------------------------------------------


# import module_1

# print("Additon :",module_1.add(10,20))
# print("Substraction :",module_1.subtract(10,20))
# print("Multiplication :",module_1.multiply(10,20))
# print("Divison :",module_1.division(10,20))

#------------------------
# import module_1 as m
# print(m.add(10,20))

#-------------------------
# from module_1 import division
# print(division(20,10))
# from module_1 import multiply
# print(multiply(20,10))
# from module_1 import subtract
# print(subtract(20,10))
# from module_1 import add
# print(add(20,10))

import sys

a = list(range(1000))
print(sys.getsizeof(a))

print(sys.getsizeof(1))


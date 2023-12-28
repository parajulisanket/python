#-----------------break;----------------

# i = 0
# while i < 10:
#     print('sanket')
#     break
# print("i am after break.")

#----------------------------------------
# names = ['ram','shyam', 'hari', 'rita','sita']
# for name in names:
#     if name == 'hari':
#         print('name found')
#         break
# --------------------------------------------------------

# names = ['ram','shyam', 'hari', 'rita','sita']
# for name in names:
#     if name =='rita':
#         break
#     print(name)



#-------------continue---------------------------------------

# nums = [1,2,3,4,5,6,7,8,9,10]

# for n in nums:
#     if n % 2 == 0:
#         continue
#     else:
#         print('odd')


###------------FUNCTION----------------------------------------

# def add():
#     print(1+1)

# add()  #invoking function/ executing function

#----------------------------------------------------------------

# def info(fn, ln ,age):
#     # print("Hi",fn,ln,'.' "Your age is",age)
#     print(f'Hi {fn} {ln}. Your age is {age}')

# info('sanket','parajuli',20)

# -----------------key word arguments------------------------------------------
# def info(fn, ln ,age):
#     # print("Hi",fn,ln,'.' "Your age is",age)
#     print(f'Hi {fn} {ln}. Your age is {age}')

# info(fn='sanket',ln='parajuli',age=20)
# info(fn='sanket',age=20,ln='parajuli')

#----------------------defult Function--------------------------------------------------

# def info(fn, ln ,age, balance=0):
#     print(f'Hi {fn} {ln}. Your age is {age}')
#     print(f'Your balance is {balance}')
  
# info(balance=100,fn='sanket',ln='parajuli',age=20)  

#--------------------------------------------------------------------------------

# def add(*args):
#     print(args)

# add()
# add(1)
# add(1,2)
# add(1,2,3)

# def my_function(*kids):
#   print("The youngest child is " + kids[2])

# my_function("Emil", "Tobias", "Linus","sanket","parajuli")

#-----------------------------------------------------------

# def info(**kwargs):
#     print(kwargs)

# info()
# info(fn="sanket")
# info(fn="sanket",ln="parajuli")
# info(fn="sanket",ln="parajuli",age=20)

# def my_function(**kid):
#   print("His last name is " + kid["lname"])
#   print("His first name is " + kid["fname"])

# my_function(fname = "Tobias", lname = "Refsnes",mname="bahadur")


#-----------------------------------------------

# def add(a,b,c):
#     return a+b+c

# total = add(10,20,30)
# print(total)


# for i in range(10):
#   print(i)

# 1 -----------------------------------
# def odd_even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
    
# user = int(input("enter the number: "))
# result = odd_even(user)
# print(result)


# 2 -------------------------------
# def upper_case(str):
#     return str.upper()

# user = input("enter the string: ")
# print(upper_case(user))


# 3 ----------------------------------
# def last_alpha(inp_str):
#     result = inp_str[-1]
#     return result

# user = input("enter the string: ")
# print(last_alpha(user))

# 4 -------------------------------------
# def number_a(inp_str):
#   inp_str = inp_str.lower()
#   count = 0
#   for i in inp_str:
#     if 'a' in i:
#       count += 1
#   return count

# user = input("enter a string: ")
# print(number_a(user))


# 5 ----------------------------------
# def max_number(inp_str):
#     max = inp_str[0]

#     for i in inp_str:
#         if i > max:
#             max = i
#     return max
    

# user = [10,20,40,50,45,34]
# print(max_number(user))


# 6 ---------------------------------
# def average(num):
#     # sum = 0
#     # for i in num:
#     #     sum += i
#     # answer = sum / len(num)
#     # return answer
#     return round(sum(num) / len(num))

# print(average([1,2,3,4,5,6,7,8,9]))
    

# 7 WAPP and return consonents present in the string.
 
# def consonent(inp_str):
#     empty = ""
#     count = 0
#     vowels = "AEIOUaeiou"
#     for i in inp_str:
#         if i not in vowels:
#             empty = empty + i
#             count = count + 1
#     return empty,count

# user = input("enter a string: ")
# print(consonent(user))


# 8 WAPP to check wheather that email address is gmail address or not.

# def email(inp_str):
#     a = inp_str.split('@')[1]
#     for i in a:
#         if i in 'gmail.com':
#             return True
#         return False

# user = input("enter a email: ")
# print(email(user))

# 9 WAPP that checks wheather edu.np is present in string or not

# def check(inp_str):
#     a = inp_str.split('@')[1]
#     for i in a:
#         if i in 'edu.np':
#             return True
#         return False

# user = input("enter a email: ")
# print(check(user))
 

# 10 WAPP that takes number and seperate into odd and even

# def odd_even(*args):
#     even = []
#     odd = []

#     for i in args:
#         if i % 2 == 0:
#             even.append(i)
#         else:
#             odd.append(i)
#     return even,odd

# print(odd_even(1,2,3,4,5,6,7,8,9))


# 11 WAPP to check wheather the number is palindrom or not.

# def palindrom(inp_str):
#     if inp_str.lower() == inp_str[::-1].lower():
#         return True
#     return False

# user = input("enter a string: ")
# print(palindrom(user))

# 14 WAPP 


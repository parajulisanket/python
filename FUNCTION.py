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
#         print('even')
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

#-----------------key word arguments------------------------------------------
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

#-----------------------------------------------------------

# def info(**kwargs):
#     print(kwargs)

# info()
# info(fn="sanket")
# info(fn="sanket",ln="parajuli")
# info(fn="sanket",ln="parajuli",age=20)




#-----------------------------------------------

# def add(a,b,c):
#     return a+b+c

# total = add(10,20,30)
# print(total)


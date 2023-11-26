# -----------list comprehension ------------------
# A way to create list from existing iterables.

# numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
# even = [item for item in numbers if item % 2 == 0]
# print(even)

#----------------------------------------------------

# names = ['ram','shyam','hari','rythm','shonu','ritu','rishu']
# name = [name for name in names if 'a' in name.lower()]
# print(name)

#----------------------------------------------------

# numbers = range(1, 101)
# answer =[number for number in numbers if number % 2 == 0 and number % 5 == 0]
# print(answer)

#----------------------------------------------------

# names = ['ram','shyam','hari','rythm','shonu','ritu','rishu']
# Cap_name = [name.capitalize()for name in names]
# print(Cap_name)

#------------------Filter----------------------------

# def is_even(n):
#     return True if n % 2 == 0 else False
# # print(list(filter(is_even,[1,2,3,4,5,6,7,8,9])))

# print(list(filter(lambda x : True if x % 2 == 0 else False, [1,2,3,4,5,6,7,8,9])))

#----------------------------------------------------

# names = ['ram','shyam','hari','rythm','shonu','ritu','rishu']
# print(list(filter(lambda n: True if 'a' in n.lower() else False,names)))

#----------------------------------------------------

# numbers = range(1, 101)
# print(list(filter(lambda n: True if n % 2 == 0 and n % 5 == 0 else False, numbers)))


#------------------Map------------------------------
# map means to change the value.

# print(list(map(lambda x: x ** 2,[1,2,3,4,5,6,6,7,8])))

# names = ['ram','shyam','hari','rythm','shonu','ritu','rishu']
# print(list(map(lambda n: n.capitalize(),names)))


#------------------reduce------------------------------

# from functools import reduce
# print(reduce(lambda x,y: x+y,[1,2,3,4,5,]))

#------------------------------------------

# from functools import reduce
# print(reduce(lambda x,y: x*y,[1,2,3,4,5,]))
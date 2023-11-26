#----------------print the number in negative form----------------------------------
# negative = [-i for i in range(1,11)]
# print(negative)

#-----------print the initial of string-------------------------------------

# names = ['sanket','parajuli','baneshower']
# new_name = [name[0] for name in names]
# print(new_name)

#---------------reverse the string---------------------------------

# names = ['ram','syam','hari']
# reverse = [name[::-1] for name in names]
# print(reverse)

#----------------- if statement-------------------------------

# even_number = [i for i in range(1,11) if i % 2 == 0]
# odd_number = [i for i in range(1,11) if i % 2 == 1]
# print(odd_number)
# print(even_number)

#----------------- if-else statement-------------------------------

# num = [1,2,3,4,5,6,7,8,9,10]

# result = [i*2 if (i % 2 ==0) else -i for i in num]
# print(result)

#-----------------convert number to string-------------------------------

# def num_to_string(x):
#     return [str(i) for i in x if(type(i)==int) or type(i)==float] 
# print(num_to_string([True,False,[1,2,3], 1 , 2 ,3, 3.0 ]))

#-----------------list comprehension in nested list-------------------------------

# result = [[i for i in range(1,4)] for j in range(3) ]
# print(result)

#------------------------------------------------

# def answer(fruits):
#     return [str(fruit) for fruit in fruits if fruit[0]=='a']
# print(answer(['apple','banana','carrot','grapes','watermelon','orange']))

#-------------------------------------------------------------------------------------------------------------------------

# 1-------square of number-----------------------------------------

# square = [i**2 for i in range(1,11)]
# print(square)

# 2------------even number from 1 to 200------------------------------------

# even_number = [i for i in range(1,101) if i % 2 == 0]
# print(even_number)

# 3---------------------square of odd number 1 to 15---------------------------

# odd_square = [i**2 for i in range(1,16) if i % 2 == 1]
# print(odd_square)

# 4-------------string length-----------------------------------

# name = ['sanket','parajuli','baneshower']
# length = [len(i) for i in name]
# print(length)

# 5------------- vowel in string-----------------------------------

# names = 'sanket parajuli baneshower'
# vowel=[name for name in names if name.lower() in 'aeiou']
# print(vowel)

# 6------------- Uppercase conversion-----------------------------------

# names = ['sanket','Parajuli','baneshower']
# result = [name.upper() for name in names]
# print(result)

# 7------------- create a list that is divisible by both 3 and 5 -------------------------------------------------

# num = range(1,51)
# answer = [i for i in num if i % 3 == 0 and i % 5 ==0]
# print(answer)

# 8------------- create 2D list that represents multiplication table from 1 to 5 using nested list comprehension---

# answer = [[[i*j for i in range(1,11)] for j in range(1,6)]]
# print(answer)

# 9------------- create a list from 1 to 20 and replace even number with'Even' and odd number with 'Odd -----------

# num = range(1,21)
# answer = ['Even' if i % 2 == 0 else 'Odd' for i in num ]
# print(answer)

# 10------------- give a list of numbers and create new list containing only unique value(remove duplicates)-------

# nums = [1,2,3,3,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9,10]
# answer = [x for i , x in enumerate(nums) if x not in nums[:i] ]
# print(answer)

# 11---------create a list where each number is doubled------------------

# num = [1,2,3,4,5,6,7,8,9,10]
# answer = [i*2 for i in num]
# print(answer)

# 12--------generate a list of number form 1 to 50 that are divisible by 7----------------

# answer = [i for i in range(1,51) if i % 7 == 0]
# print(answer)

# 13--------create a list of cube number from 1 to 10----------------

# answer = [i**3 for i in range(1,11)]
# print(answer)


#(1) write a function that takes a number and return True if the number is even and return False if number is odd.

# def is_even(n):
#     if n %2 ==0:
#         return(True)
#     else:
#         return(False)

# num = int(input("Enter the number: "))
# result = is_even(num)
# print(f'The result is {result}')


#(2) write a function that takes a string and returns True if u and U is present in the string and else return False 

# def is_present(ch):
#     if 'u' in ch.lower():
#         return True
#     else:
#         return False
    
# name = input("enter the string: ")
# result = is_present(name)
# print("The result is",result)


#(3) write a function that takes a string and returns the length of the string

# def find_len(name):
#     return name

# user = input("enter the string: ")
# result = find_len(len(user))
# print("The length of string is:",result)


#(4) write a function tha takes three numbers and reutnrs tha average of those 3 numbers

# def average(a,b,c):
#     return (a + b + c) / 3

# first_number = int(input("enter the 1st number: "))
# second_number = int(input("enter the 2nd number: "))
# third_number = int(input("enter the 3rd number: "))
# answer = average(first_number,second_number,third_number)
# print("The average is: ",round(answer,2))


#(5) write a function that takes two numbers and returns the greatest of those two numbers 

# def is_greater(fn,sn):
#     if fn > sn:
#         return fn
#     else:
#         return sn
    
# first_number = int(input("enter 1st number:"))
# second_number = int(input("enter 2nd number: "))
# result = is_greater(first_number,second_number)
# print("The greater number is",result)


#(6) write a function that takes a string and returns the reverse of a string

# def reverse(str):
#     return str[::-1]

# user = input("enter the string: ")
# result = reverse(user)
# print("The reverse is: ",result)


#(7) Write a funtion thar takes a string and returns True if the string is palindrome and return None if not a palindrome

# def palindrome(str):
#     if str[::-1] == str:
#         return True
#     else:
#         return None

# user = input("enter the string: ")
# result = palindrome(user)
# print("The answer is:",result)



#(8) write a function that takes first name and last name and age in keyword arguements and returnrs the values in a dictionary form 

# def info(fn, ln , age):
#     return {'first_name':fn,'last_name':ln,'age':age}

# info(fn='sanket',ln='parajuli',age=20)


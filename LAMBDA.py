# s = lambda x : x** 2
# print(s(10))

# write a lambda function that takkes a string and return the first letter of that string.

# user_input = input("enter the string:")
# user = lambda x : x[0]
# print(user(user_input))


# write a lambda function function that takes a number and return True if the number if even and False otherwise.

# user_input = int(input("enter the number:"))
# user = lambda x: True if x % 2 == 0 else False
# print("The answer is:",user(user_input))


# write a lambda function that takes a number and return True if the number if divisible by both 2 and 5.

# user_input = int(input("enter the number:"))
# user = lambda x: True if x % 2 == 0 and x % 5 == 0 else False
# print(user(user_input))


# write a program that takes string from the users and return the last character of the name .

# a = input("enter the name:")
# b = lambda ch: ch[-1]
# print("The answer is:",b(a))

# write a program that returns True if length of the string is more than five(using if else statement).

# user_input = input("enter the string:")
# length = lambda l: True if len(l) > 5 else False
# print("The answer is",length(user_input))


# write a program that returns True if length of the string is more than five.

# x = input("enter the string:")
# y = lambda s: len(s) >= 4 
# print("The answer is:",y(x))

# --------odd even using lambda along with if else:--------------
# a = int(input("enter the number:"))
# b = lambda n: True if n % 2 == 0 else False
# print("the answer is:",b(a))


# WAPP that take two numbers and return the summbition of those two number

# user1 = int(input("enter the 1st number: "))
# user2 = int(input("enter the 2nd number: "))

# answer  = lambda user1,user2: (user1 + user2)  
# print(answer(user1,user2))


# WAPP that returns true if even false if odd

# user = int(input("enter the number: ")) 
# answer = lambda user: (print(f"{user} is even") if user % 2 == 0 else print(f"{user} is odd"))
# answer(user)


# write  a lambda function that takkes a string and return the first letter of that string.

# user_input = input("enter the string: ")
# answer = lambda x : x[-1]
# print(answer(user_input))


# write a lambda function that takkes a string and return the reverse of that string.

# user_input = input("enter the string:")
# user = lambda x : x[::-1]
# print(user(user_input))


# write a lambda function that takkes a string and check palindrome or not.

# user_input = input("enter the string:")
# user_input = user_input.casefold()
# user = lambda x : True if user_input == user_input[::-1] else False
# print(user(user_input))


# write a lambda function that takkes a string and check weather letter u in string pr not.

# user_input = input("enter the string:")
# user_input = user_input.casefold()
# user = lambda x : True if 'u' in user_input else False
# print(user(user_input))

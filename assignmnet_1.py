#ASSIGNMENT:
# 1.create a calculator:

# fn = int(input("enter the 1st number: "))
# sn = int(input("enter the 2nd number: "))
# operator = input("enter the operator (+, -, /, *) ")

# if operator == '+':
#     print("The sum is:",fn+sn)
# elif operator =='*':
#     print("The multiplication is:",fn*sn)
# elif operator =='/':
#     print("The division is:",fn/sn)
# elif operator == '-':
#     print("The substraction is:",fn-sn)
# else:
#     print("Invalid operator.")


# ---------------------------------------------------------------
# fn = int(input("enter the 1st number:"))
# sn = int(input("enter the 2nd number:"))
# ch = input("Enter your choice (+, -, /, * ) ")

# if ch == '+':
#     sum = fn + sn
#     print("The result is:",sum)  
# elif ch == '-' and fn > sn:
#     sub = fn - sn
#     print("The substraction is:",sub)
# elif ch == '-' and sn > fn:
#     sub = sn - fn
#     print("The substraction is:",sub)
# elif ch == '*':
#     mul = fn * sn
#     print("The multipilcation is:",mul)
# elif ch == '/' and fn > sn:
#     div = fn / sn
#     print("The division is:",round(div,2))
# else:
#     print("Invalid operator.")

# ------------calculator------------------:

# fn = int(input("enter first number: "))
# sn = int(input("enter second number: "))
# operator = input("enter operator:")
# if operator not in '+ - * / % //' :
#     print("Invalid operator")
# else:
#     if operator =='+':
#         print(f'The sum of {fn} and {sn} is {fn+sn}')
    
#     elif operator =='-':

#         while True:
#             require = input("Press 'y' for absolute value else press 'n' for normal answer: ").upper()
#             if require == 'Y':
#                 if fn > sn:
#                     print(f"The diff of {fn} and {sn} is {fn-sn}")
#                 elif fn < sn:
#                     print(f"The diff of {fn} and {sn} is {sn-fn}")
#             elif require == 'N':
#                 print(f"The diff of {fn} and {sn} is {fn-sn}")

     
#     elif operator =='*':
#         print(f'The mult of {fn} and {sn} is {fn*sn}')
    
#     elif operator =='/':
#         if fn < sn:
#             print(f"The div of {sn} and {fn} is {sn/fn}")
#         else:
#             print(f'The div of {fn} and {sn} is {fn/sn}')
    
#     elif operator =='%':
#         if fn < sn:
#             print(f'The mod of {sn} and {fn} is {sn%fn}')
#         else:
#             (f'The mod of {fn} and {sn} is {sn%fn}')

        
#     elif operator =='//':
#         print(f'The float_divison of {fn} and {sn} is {fn//sn}')



# # Taking two number from the users to perform calculation
# num1 = int(input("input number 1: ")) 
# num2 = int(input("input number 2: ")) 
# # asking the user to choose the operator
# operator = input("Select an operator, * for multiplication, - for subtraction, + for addition, / for division: ")

# # using the if-else conditions to get the output and printing the answer
# if operator == '+':
#     print(f"Results: Adding {num1} and {num2} = {num1 + num2}")
# elif operator == '-':
#     if num2 > num1:
#         print(f"Results: Subtracting {num2} from {num1} = {num2 - num1}")
#     else:
#         print(f"Results: Subtracting {num1} from {num2} = {num1 - num2}")
# elif operator == '*':
#     print(f"Results: Multiplying {num1} by {num2} = {num1 * num2}")
# elif operator == '/':
#     print(f"Results: Dividing {num1} from {num2} = {num1 / num2}")
# else:
#     print(f"{operator} operator is invalid.")

    

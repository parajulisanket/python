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



#  hari = 82 ram = 65 shyam 55 rita 42

# name_score = {'hari': 82,'ram': 65,'shyam': 55,'rita': 42 }
# student =input("Enter the name of the students :").capitalize() 
# if name_score[student] >= 80 :
#     print(f'Congratulation! {student} You got distinction.')
#     #print("Congratulation!",student,"You got distinction.")
# elif name_score[student] >= 60 and name_score[student] < 80 :
#     print(f'Congratulation! {student} you got First division.')
#     # print("Congratulation!",student,"you got First division.")
# elif name_score[student] >=50 and name_score[student] <60 :
#     print(f'Congratulation! {student} you got Second division.')
#     # print("Congratulation!",student,"you got Second division.")
# elif name_score[student] < 50:
#     print(f"Congratulation! {student} you will receive Mom's flying chappel.")
#     #print("Congratulation!",student,"you will receive Moms flying chappel.")


# student_grade = {'ram': 85, 'shyam': 65, 'hari':55,'rita': 42}
# name = input('enter your name: ').lower()

# if name not in student_grade:
#     print('Name not found')
# else:
#     if student_grade[name]>= 80:
#         print(f'hi {name.capitalize()},you grade is {student_grade[name]}')
#     elif student_grade[name] >= 60:
#         print(f'hi {name.capitalize()},you grade is {student_grade[name]}')
#     elif student_grade[name] >= 50:
#         print(f'hi {name.capitalize()},you grade is {student_grade[name]}')
#     else:
#         print(f"hi {name.capitalize()},Mom's flying chappel {student_grade[name]}")
    


#1 make a keyword detector in python (import keyword)
import keyword

keyword_list = keyword.kwlist
user = input("enter a word: ")

if user in keyword_list:
    print(f"{user} is a keyword.")

#2 enter your expenditure on january rent, lunch, fule/travel, food (filename = month.png) 
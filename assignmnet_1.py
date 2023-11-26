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

fn = int(input("enter the 1st number:"))
sn = int(input("enter the 2nd number:"))
ch = input("Enter your choice (+, -, /, * ) ")

if ch == '+':
    sum = fn + sn
    print("The result is:",sum)  
elif ch == '-' and fn > sn:
    sub = fn - sn
    print("The substraction is:",sub)
elif ch == '-' and sn > fn:
    sub = sn - fn
    print("The substraction is:",sub)
elif ch == '*':
    mul = fn * sn
    print("The multipilcation is:",mul)
elif ch == '/' and fn > sn:
    div = fn / sn
    print("The division is:",round(div,2))
else:
    print("Invalid operator.")

    # calculator:
# fn = int(input("enter first number: "))
# sn = int(input("enter second number: "))
# operator = input("enter operator:")
# if operator not in '+ - * /' :
#     print("Invalid operator")
# else:
#     if operator =='+':
#         print(f'The sum of{fn} and {sn} is {fn+sn}')
#     elif fn >= sn:
#         print(f'The diff of{fn} and {sn} is {fn+sn}')
#     elif:
#     print(f'The diff of{fn} and {sn} is {sn+fn}')

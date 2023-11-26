# calculator using function, also with certain criteria... 
def sum(fn,sn):
    return fn + sn
def sub(fn,sn):
    if sn > fn :
        return sn - fn
    else:
        return fn - sn
def mul(fn,sn):
    return fn * sn
def div(fn,sn):
    if sn > fn:
        return sn / fn
    else:
        return fn / sn
def power(fn,sn):
    return fn**sn

num1= int(input("enter 1st number:"))
num2 = int(input("enter 2nd number:"))
operator = input("enter the operator: + , -, /, *, ** : ")
if operator == '+' :
    print("The sum is:",sum(num1,num2))
elif operator == '-':
    print("The sub is:",sub(num1,num2))
elif operator == '/':
    print("The div is:",round(div(num1,num2),2))
elif operator == '*':
    print("The mul is:",mul(num1,num2))
elif operator =='**':
    print("The power is:",power(num1,num2))
else:
    print("Invalid operator.")
# honestly i have solved this by my on..
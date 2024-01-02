# exception handling: 
 
# ----bugs: The fault/ errors in programs are called bugs.
# ----debugging: The process of finding and fixing bugs is called debugging.(Our program should be free of bugs)

# Type of errors :

     # syntax errors:
        #It occurs due to mistake in the syntax.
        #If we write code that python does not understand it throws an errors called syntax error.
        # It is occurs when there is a typo.
        # our program doen't compile if there is syntax error.
        # our syntax should be free errors.
        # compiler first scans the code to check if it is free of synatx errors if there is a syntax error it doesn't compile the code.

#----------------------------------------------------------------------
    #logical errors:
        # it happens where there is a problem in the logic.
        # this program runs but doen't give us the correct output.

# example of logical error;
# while True:
#     age = int(input("enter age"))
#     if age > 21: # logic doen't meet here.
#         print("you cannot buy beer.")
#     else:
#         print("you can buyt beer.")

#----------------------------------------------------------------------

# runtime errors/ excception:
        #runtime errors are called expections.
        #this causes sudden/unwanted termination of the program.
        #This error should be handled in a friendly manner.

#example of runtime error:
# while True:
#     first = int(input("enter first number"))
#     second = int(input("enter second number"))
#     print(first/second)


#----------------------------------------------------------------------

# try:
    # risky code
    # code that can throw an error

# example of try and except and finally:
# while True:
#     try:
#         first = int(input("enter first number: "))
#         second = int(input("enter second number: "))
#         print(first/second)
#     except ZeroDivisionError:
#         print("second number can't be zero.")
#     except ValueError:
#         print("input must be number.")
#     except Exception as e:
#         print("an error occured.")
#         print(type(e))
#     finally:
#         print("Thank you for visiting."
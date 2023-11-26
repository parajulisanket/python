#  OOP > Object Oriennted Program : 
# Career oriented > career focussed 
# It is style of writing code using (class) and (object).
    # class:  
#      Class is a blue print of an object.
#     It is a design/model/template of an object.
#     It defines/describe how an object should look like.
    # object:    
# object is an instantiation / perfect example of a class.
# It has features / characteristic as described by the class.
#  reference variable > variable that points to an object is called reference variable.


# Types of variable.
    # instance variable:
        # variable whose value depends on the objects are called instance varaible.
        # it is accessed by using self inside the class and by using object name outside the class.
        # copy of instance varaible is created for every object.

    # static variable.
        # variable whose value depends on the class are called instance varaible.
        # it is accessed by using class name both inside and outside the class.
        # also called class-level variable.
        # copy of static varaible is created only once when the class is cretaed.

#instance method
    
    #methods that access instance variable are called instance method.
    #self should be the first parameter.
    # accessed by using inside the class and by using objest name outside of the class.

#class method:
    # method that access static variables are called class method.
    # cls should be the first paremeter.
    # accessed by using class name both inside and outside of the class
    # classmethod decorator is required.

# satic method:
    # method that do not depend on class or objects are called  static method.
    # can be parameterless or parameterized.
    # accessed by using name both inside and outside of the class
    # staticmethod decorator is required.

## ---Pillers of OOP----------
#Encapsulation:
    # The process of grouping together the properties of the class.
    # it makes easier to find the bugs.
    # bundling of attributes and methods inside a single class.

#Abstraction:
    # process of handling complexity by hiding unnecessary information from the user.

# Inheritance:
    # allows us to define a class that inherts all the methods and properties from another/parent class.

# Polymorphism: 
    # polymorphism 




#---------------------------------------------------------

# class Person:
#     def __init__(self): # magic method
#         self.first_name = 'sanket'
#         self.last_name = 'parajuli'
#         self.age = 20

# p = Person() #  object instantiation
# print(p.first_name,p.last_name,p.age)
# print(p.first_name) 

#--------------------instance method:-----------------------------------------

# class Person:
#     def __init__(self,f_name,l_name,age):
#         self.f_name = f_name
#         self.l_name = l_name
#         self.age = age
    
#     def full_name(self): # instance method:
#         return f"{self.f_name} {self.l_name}"
    
#     def is_above_18(self):
#         if self.age > 18:
#             return 'Yes'
#         else:
#             return 'No'

# p1 = Person('sanket','parajuli',2)
# p2 = Person('samana','parajuli',18)
# print(p2.f_name)
# print(p1.full_name())
# print(p1.is_above_18())


#-------------------- class varaible:---------------------------------------

# class circle:
#     pi = 3.14 # class variable
#     def __init__(self,radius):
#         self.radius = radius

#     def area(self): # instance method
#         return circle.pi * self.radius**2

# user = int(input("enter the radius:"))
# p = circle(user)
# print("area of circle is:",p.area())


#-----------------------------------------------------------

# class Sunwaystudent:
#     school_name = 'Sunway college' # class variable
#     school_address = 'maitidevi'
#     def __init__(self,f_name,l_name,age):
#         self.f_name = f_name
#         self.l_name = l_name
#         self.age = age

# user1 = input("enter the first name:")
# user2 = input("enter the last name:")
# user3 = int(input("enter the age:"))

# p = Sunwaystudent(user1,user2,user3)

# print(f'Your fullname is {p.f_name} {p.l_name}.')
# print(f'Your age is {p.age}.')

#-----------------------Encapsulation & Abstraction------------------------------------

# class Phone:
#     def __init__(self,brand, model,price): 
#         self.brand = brand
#         self.model = model
#         self.price = price

#     def make_a_call(self,phone_number):
#         self.phone_number = phone_number
#         print(f'calling {self.phone_number}.....')

#     def fullname(self):
#         return (f'{self.brand} {self.model}')

# p = Phone('iphone','x',10000)
# print(p.fullname())
# print(p.price)

# user = int(input("enter your number:"))
# print(p.make_a_call(user))
    

#-----------------------Inheritance------------------------------------
    
# class Phone:
#     def __init__(self,brand, model,price): 
#         self.brand = brand
#         self.model = model
#         self.price = price

#     def fullname(self):
#         return (f'{self.brand} {self.model}')
    
# class Smartphone(Phone): # Inheritance method:
#     def __init__(self, brand, model, price,internal_memory,rear_camera):
#         Phone.__init__(self,brand,model,price)
#         self.interanl_memory = internal_memory
#         self.rear_camera = rear_camera


# a = Phone('Iphone','X',10000)
# b = Smartphone('Oneplus','5',30000,'6_GB','20_MP')
# print("Price of",a.fullname(),"is",a.price)
# print("Price of",b.fullname(),"is",b.price)
    

# -------------------------------Polymorphism-------------------------------

# class employee:
#     def __init__(self,fn, ln, age):
#         self.fn = fn
#         self.ln = ln
#         self.age = age

#     def get_name(self):
#         print("i am base class.")

# class fulltimeEmployee(employee):
#     def __init__(self, fn, ln, age,address,salary):
#         super().__init__(fn, ln, age)
#         self.address = address
#         self.salary = salary

#     def get_name(self):
#         print("I am full time class.")

# p = fulltimeEmployee('sanket','parajuli','20','baneshower',100)
# p.get_name()
# print(p.fn)
# print(p.get_name)





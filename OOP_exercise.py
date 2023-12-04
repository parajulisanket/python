# 0-------------------basic exercise--------------------------------------

# class Laptop:
#     def __init__(self,brand_name, model_name, price):
#         self.brand_name = brand_name
#         self.model_name = model_name
#         self.price = price 

# p = Laptop('Apple','macbook_Air',155000)

# print("The brand of laptop is",p.brand_name) 
# print("The model is",p.model_name)
# print("The price is",p.price)

# 1---------instance variable----------Find the discount-----------------------------

# class Discount:
#     def __init__(self, MP, SP):
#         self.MP = MP
#         self.SP = SP

#     def final_price(self):
#         return self.MP - self.SP
    
# user1 = int(input("enter the Marked price:"))
# user2 = int(input("enter the selling price:"))

# p = Discount(user1,user2)

# print("The discount is",p.final_price())


# 2-----------instance method--------area of rectangle----------------------------
 
# class Rectangle:
#     def __init__(self,length, width):
#         self.length = length
#         self.width = width

#     def result(self): # instance method:
#         return self.length * self.width
    
# user1 = int(input("enter the length:"))
# user2 = int(input("enter the width:"))

# p = Rectangle(user1,user2)

# print("Area of rectangle is:",p.result())


# 3----------class variable---------circumference and area of circle------------
# area = pi * r**2  and circumference = 2 * pi * r-----

# class circle:
#     pi = 3.14 # class variable
#     def __init__(self,radius):
#         self.radius = radius

#     def area(self): # instance method
#         return circle.pi * self.radius**2
    
#     def circumfrence(self): # instance method
#         return 2 * circle.pi * self.radius
    
# user = int(input("enter the radius:"))

# p = circle(user)

# print("area of circle is:",p.area())
# print("area of circle is:",p.circumfrence())


# 4----------Inheritance method---------basic question----------------------------

# class Vehicle:
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model

#     def full_name(self): # instance method:
#         return self.model

# class Car(Vehicle): # apply of inheritance method: 
#     def __init__(self, make, model,color,year):
#         Vehicle.__init__(self, make,model)
#         self.color = color
#         self.year = year

# # user1 =input("enter the country:")
# # user2 =input("enter the model:")
# # user3 =input("enter the color:")
# # user4 =input("enter the year:")
# # a = Vehicle(user1,user2)
# # b = Car(user1,user2,user3,user4)
# a = Vehicle('German','BMW')
# b = Car('America','Tesla','Red','2004')

# print(a.full_name(),"was originated at",a.make,".")
# print(b.full_name(),"was originated at",b.make,"in",b.year,"in",b.color,"color.")

#-----------------------------------------------------

# class Person:
#     def __init__(self,f_name,l_name,age):
#         self.f_name = f_name
#         self.l_name = l_name
#         self.age = age
        
#     def full_name(self): # insatnce method
#         return f'{self.f_name} {self.l_name}'

# class Student(Person): # inheritance method:
#     def __init__(self,f_name,l_name,age, grade, college_name):
#         Person.__init__(self,f_name,l_name,age) 
#         self.grade = grade
#         self. college_name =  college_name

# a = Person('Sanket','Parajuli',20)
# b = Student('Ram','Hari',22,'bachelore','sunway_Int')

# print(a.full_name(),"age is",a.age)
# print(b.full_name(),"age is",b.age,"and he studies at",b.college_name,"he is a",b.grade,'student.')





# 5--------instance methods-----------calculatore using OOP-------------------------
# while True:
#     class Calculator:
#         def __init__(self,a,b,operator):
#             self.a = a
#             self.b = b
#             self.operator = operator
    
#         def answer(self): # instance method:
#             if self.operator =='+':
#                 return self.a + self.b
#             elif self.operator == '-':
#                 return self.a - self.b
#             elif self.operator == '*':
#                 return self.a * self.b
#             elif self.operator == '/':
#                 return self.a / self.b



#     user1 = int(input("enter the 1st number:"))
#     user2 = int(input("enter the 2nd number:"))
#     result = input("enter the operator:")

#     p = Calculator(user1,user2,result)

#     print("The answer is:",p.answer())

#----------------------------------------------------------------

# class Person:
#     def __init__(self,fn,ln,age):
#         self.fn = fn
#         self.ln = ln
#         self.age = age

#     def full_name(self):
#         return f"Your fullname is {self.fn} {self.ln}, and your age {self.age}"
    
# class Student(Person):
#     def __init__(self, fn, ln, age,course,semester,college_name):
#         super().__init__(fn, ln, age)
#         self.course = course
#         self.semester = semester
#         self.college_name = college_name 

#     def detail(self):
#         return f"Your collage name is {self.college_name} course is {self.course}, and you are in {self.semester} sem."
    
# user1 = input("enter your first name: ")
# user2 = input("enter your last name: ")
# user3 = int(input("enter your age: "))
# user4 = input("enter the name of college: ")
# user5 = input("enter your course name: ")
# user6 = int(input("enter your semester: "))
            
# p = Person(user1, user2, user3)
# p1 = Student(user4, user5, user6)

# print(p.full_name())
# print(p1.detail())


#----------------Multilevel inheritance-------------------

# class Phone:
#     def __init__(self,brand_name, model_name,price):
#         self.brand_name = brand_name
#         self.model_name = model_name
#         self.price = price

    
#     def fulldetail(self):
#         return f"The price of {self.brand_name} {self.model_name} is {self.price}."
    
# class Smartphone(Phone):
#     def __init__(self,brand_name, model_name,price,country,year):
#         super().__init__(brand_name, model_name,price)
#         self.country = country
#         self.year = year
        
#     def location(self):
#         return f"{self.fulldetail} was made in {self.country}."

        
# class Advancephone(Smartphone):
#     def __init__(self, brand_name, model_name, price, country, year, camera, speed):
#         super().__init__(brand_name, model_name, price, country, year)
#         self.camera = camera
#         self.speed = speed

#     def camera_quality(self):
#         return f"The camera quality if {self.fullname} is {self.camera}."

# O = Phone('apple','Iphone 8', 30000)   
# O1 = Smartphone('apple', 'Iphone X', 60000, 'America', 2018)
# O2 = Advancephone('apple', 'Iphone 13', 120000, 'America', 2022, '20MP', '155hz' )
# print(O.fulldetail())
# print(O1.fulldetail())
# print(O2.fulldetail())


# --------------------Multiple inheritance(2)---------------------

# class A:
#     def class_a_method(self):
#         return "I'm class A method."
    
#     def hello(self):
#         return 'hello from class A.'
    
# class B:
#     def class_b_method(self):
#         return "I'm class B method."
    
#     def hello(self):
#         return 'hello from class B.'
    
# class C(A,B):
#     pass

# # o = A()
# # o1 = B()
# # print(o.class_a_method())
# # print(o1.class_b_method())
# o2 = C()
# print(o2.hello())


class Cal:
    def __init__(self,fn, sn):
        self.fn = fn
        self.sn = sn

    def sum(self):
        return f'{self.fn} + {self.sn}'
    
user1 = int(input("enter the 1st number:"))
user2 = int(input("enter the 2st number:"))

p1 = Cal((user1,user2))
print(p1.sum())


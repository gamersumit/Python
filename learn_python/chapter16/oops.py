# OOPs :
# CLASS :

########################################################################

# class Person:
#     def __init__(self, first_name, last_name, age): # init is our constructor and self is our this keyword / object reference
#         # instance variables
#         print("constructor called")
#         self.person_first_name = first_name.title()
#         self.last_name = last_name.title()
#         self.age = age


# p1 = Person('sumit', 'aggarwal', 22)
# p2 = Person('lalit', 'yadav', 22)

# print(p1.person_first_name)
# print(p1.last_name)


# ################################################################

# # EXCERCISE 1:

# class Laptop:
#     def __init__(self, name, model, price):
#         self.name = name
#         self.model = model
#         self.price = price

# lap1 = Laptop('dell g14', 'xx093xr', '70000')
# lap2 = Laptop('mi notebook horizon 14', 'mfmr3003uy', '49000')

# print(lap1.name,lap2.name,lap1.price,lap2.price,lap1.model,lap2.model)


################################################################
# INSTANCES AND METHODS :

# class Person:
#     def __init__(self, first_name, last_name, age): # init is our constructor and self is our this keyword / object reference
#         # instance variables
#         self.first_name = first_name.title()
#         self.last_name = last_name.title()
#         self.age = age

#     def full_name(self):
#         return self.first_name + ' ' + self.last_name


# p1 = Person('sumit', 'aggarwal', 22)
# p2 = Person('lalit', 'yadav', 22)

# print(p1.full_name())
# print(Person.full_name(p2))  # important



################################################################

# # EXCERCISE 2:

# class Laptop:
#     def __init__(self, name, model, price):
#         self.name = name
#         self.model = model
#         self.price = price
    
#     def apply_discount(self, discount):
#         return self.price / 100 * (100 - discount)

# lap1 = Laptop('dell g14', 'xx093xr', 70000)
# lap2 = Laptop('mi notebook horizon 14', 'mfmr3003uy', 49000)

# print(lap1.apply_discount(40))


################################################################

# CLASS VARIABLES :

# class Circle1 :
#     def __init__(self, radius, pi):
#         self.radius = radius
#         self.pi = pi
    
#     def area(self):
#         # return pi*(radius**2) # invalid as we didn't use self
#         return self.pi * (self.radius**2)


# c1 = Circle1(3, 3.14)  
# c2 = Circle1( 4, 3.14) # correct but repeation and extra memory for every object
# print(c1.area())


# # # ----------- #

# class Circle2 :
#     pi = 3.14  # class variable

#     def __init__(self, radius):
#         self.radius = radius
    
#     def area(self):
#         return Circle2.pi * (self.radius**2)  # Cirlcl2.pi() is used means it will be a constant
    
#     def circumference(self):
#         return 2 * self.pi * self.radius   # self.pi() is used means pi can vary for differnent objects
    
    
# c3 = Circle2(3)
# print('area = ', c3.area())

# print('circum = ', c3.circumference())
# print('c3', c3.__dict__)


# c3.pi = 4
# print('c3', c3.__dict__)
# print('circum = ', c3.circumference())
# print('area = ', c3.area())


# c4 = Circle2(4)
# print('c4', c4.__dict__)
# print(c4.area())
# print(c4.circumference()) 



################################################################

# # EXCERCISE 3:

# class Objects:
#     count = 0

#     def __init__(self):
#         Objects.count += 1

# print(Objects.count)
# ob1 = Objects()
# print(Objects.count)
# ob2 = Objects()
# print(Objects.count)



################################################################

# CLASS METHOD vs Instance Methods :

# class Person:
#     count = 0
#     def __init__(self, first_name, last_name, age): # init is our constructor and self is our this keyword / object reference
#         # instance variables
#         Person.count += 1
#         self.first_name = first_name.title()
#         self.last_name = last_name.title()
#         self.age = age
       
#     # class method :
#     @classmethod
#     def total_instances(cls):
#         return f"you have created {cls.count} instances of class {cls.__name__}."

#     # instance method : 
#     def full_name(self):
#         return self.first_name + ' ' + self.last_name
    
#     def is_above_18(self) :
#         return self.age > 18
    
    
# p1 = Person('sumit', 'aggarwal', 22)
# p2 = Person('lalit', 'yadav', 22)

# print(p1.total_instances())
# print(Person.total_instances())


################################################################

# CLASS METHOD as CONSTUCTORS :
# Stactic METHOD:

# class Person:
#     count = 0
#     # default constructor
#     def __init__(self, first_name, last_name, age): # init is our constructor and self is our this keyword / object reference
#         # instance variables
#         print("default_constructor called")
#         Person.count += 1
#         self.first_name = first_name.title()
#         self.last_name = last_name.title()
#         self.age = age

#     # another constructor / method constructor
#     @classmethod
#     def another(cls, string): 
#         f_name, l_name, age = string.split(',')
#         age = int(age)
#         print("method constructor called")
#         return cls(f_name, l_name, age)
       
#     # class method :
#     @classmethod
#     def total_instances(cls):
#         return f"you have created {cls.count} instances of class {cls.__name__}."


#     # STATIC METHOD : no relation with objects
#     @staticmethod
#     def hello():
#         print("hello, static method called")

#     # instance method : 
#     def full_name(self):
#         return self.first_name + ' ' + self.last_name
    
#     def is_above_18(self) :
#         return self.age > 18
    

# p0 = Person.another("prashant,zarika,24")
# print(p0.full_name())
# print(p0.__dict__) 

# p0.hello()
# Person.hello()


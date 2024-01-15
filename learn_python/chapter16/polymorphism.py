# # DUNDER METHODS/ SPECIAL MAGIC METHODS: __MEHTOD__ (WRITTEN IN DOUBLE UNDERSCORE) :
# ## E.G. -> __init__, __dict__, __name__ etc

# class Person:
#     def __init__(self, first_name, last_name, age): # init is our constructor and self is our this keyword / object reference
#         # instance variables
#         print("constructor called")
#         self.first_name = first_name.title()
#         self.last_name = last_name.title()
#         self.age = age


#     def __str__(self):   # take precedence over repr 
#         return f"{self.first_name} {self.last_name} and {self.age}"

#     def __repr__(self): # written in a way whose output can be copied and used as it is to create an object
#         return f"Person(\'{self.first_name}\',\'{self.last_name}\',\'{self.age}\')"
    
#     # OPERATOR OVERLOADING :
 
#     def __add__(self, other):   # it will overload + operator
#         return self.age+ other.age
    
#     def __mul__(self, other): # it will overload * operator
#         return self.age * other.age

# p1 = Person('sumit', 'aggarwal', 21)
# p2 = Person('lalit', 'yadav', 22)

# print(p1.first_name)
# print(p1.last_name)
# print(p1) ## trigger __str__ method if defined else __repr__ method if defined else it will give memory location (address)
# print(p1.__repr__())
# print(p1 + p2)
# print(p1*p2)



################################################################    
## POLYMORPHISM :  ability to take many forms at a given time
## e.g:- operator overloading, method overridings, etc
################################################################






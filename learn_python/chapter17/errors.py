# ERRORS: 

##* 1. syntax error:

## a.
# def fun: # parentheses required (syntax error)
#     pass

## ----- ##

## b.
# var = 'sumit'* # syntax error (invalid value to variable)

# ******************************** #

##* 2. INdentation error:

# def fun():
#     print('fun')  
#  print('fun2')  # indentation error

# ******************************** #

##* 3. Name Error:

## a.
# print(age)  # name 'age' is not defined results in name error


## --------- ##

## b.
# print(fun(5)) # name 'fun' is not defined results in name error


# ******************************** #

##* 4. Type Error: wrong type on  some operation performed

## a.
# print(5 + 'sumit') # TypeError: unsupported operand type(s) for +: 'int' and 'str'
### print(5 * 'sumit') # it's fine


# ******************************** #

##* 5. Index Error: providing invalid index while iterating any iterable or iterators

## a.
# ls = [0,1,2,3,4]
# print(ls[9])  #IndexError: list index out of range


# ******************************** #

##* 6. Value Error:  if the datatype is correct but value is inncorrect

## a.
# print(int('abc'))    #ValueError: invalid literal for int() with base 10: 'abc'
# print(int('5'))      # it is correct

# ******************************** #

##* 7. Attribute Error:  if attribute is not defined but still used 

## a.
# ls = [1,2,3,4]
# ls.push(5)  # AttributeError: 'list' object has no attribute 'push'


# ******************************** #

##* 8. Key Error:  if key is not present but still tried to access  

## a.
# d = {'name' : 'sumit', 'age' : 21}   
# print(d['fullname'])  # KeyError: 'fullname'


#********------------------------------------------------**********

###* Raising Errors in  python :

# def add(a,b) : 
#     if(type(a) is int and type(b) is int):
#      return a + b
    
#     raise TypeError("you are passing wrong datatype values")

# print(add(3,2))
# print(add(4,'s'))


################################
#* EXAMPLE 1: NotImplementedError

# class Animal:
#     def __init__(self, name):
#         self.name = name
    
#     def sound(self):   # abstract method
#         raise NotImplementedError('you have to implement this method in your subclass')
    
# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)
#         self.breed = breed

# class Cat(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)
#         self.breed = breed
    
#     def sound(self):
#         return 'meow meow'
    
# c= Cat('sissy', 'tigercat')
# print(c.name)
# print(c.sound())    
    
# d = Dog('juno', 'golden' )
# print(d.name)
# print(d.sound())


################################
#* EXAMPLE 2: 

# class Mobile:
#     def __init__(self, name):
#         self.name = name


# class Mobilestores:
#     def __init__(self):
#         self.mobiles = []
    
#     def add_mobile(self, new_mobile):
#         if isinstance(new_mobile, Mobile):
#             self.mobiles.append(new_mobile)
#         else :
#             raise TypeError("new_mobile should be object of Mobile class")

# store1 = Mobilestores()
# print(store1.mobiles)
# mobile1 = Mobile('samsung galaxy 21')
# mobile2 = Mobile('one plus 2T')
# mobile3 = Mobile('redmi note 5 pro')
# mobile4 = Mobile('motorola edge 40')
# mobile5 = 'oppo renvo 8' ## not a mobile it is a string

# store1.add_mobile(mobile1)
# store1.add_mobile(mobile2)
# store1.add_mobile(mobile3)
# store1.add_mobile(mobile4)

# for item in store1.mobiles :
#     print(item.name)

# store1.add_mobile(mobile5)

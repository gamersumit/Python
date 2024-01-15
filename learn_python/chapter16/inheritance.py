# class Phone:
#     def __init__(self, brand, model_name, price):
#         self.brand = brand
#         self.model_name = model_name
#         self.price = price  
       
#     def make_call(self, number):
#         print(f"calling {number} ...")
    
#     def full_name(self):
#         return f"{self.brand} {self.model_name}"
    
# class Smartphone(Phone):   
#     def __init__(self, brand, model_name, price,ram,rear_camra):
#         ## TWO WAYS :
#         ## 1.
#         ## Phone.__init__(self, brand, model_name, price)

#         ## 2.
#         super().__init__(brand, model_name, price)
#         self.ram = ram
#         self.rear_camra = rear_camra


# ph1 = Smartphone('mi', 'note 5 pro', 15000, '4 GB', '2.6 aperture',)
# print(ph1.__dict__)
# print(ph1.full_name())


# # MULTI LEVEL INHERITANCE :  A -->> B -->> C ... 

# class Flagship(Smartphone):
#     def __init__(self, brand, model_name, price, ram, rear_camra, processor):
#         super().__init__(brand, model_name, price,ram,rear_camra)
#         self.processor = processor

#     ## METHOD OVERRIDING :
#     def full_name(self):
#         return super().full_name() + ' FLAGSHIP'




# ph2 = Flagship('samsung', 'f22', 100000, '12 GB', '0.6 aperture', 'snapdragon 8 gen 2')
# print(ph2.full_name())
# print(ph2.__class__.__name__)
# print(ph2.processor)
# print(ph2.__dict__)



# ### METHOD RESOLUTION ORDER (MRO) :
# # print(help(Flagship))  # program will execute in order of method resolution
# # if we call full_name function or any overwritten function it will be excuted in MRO ORDER FROM CHILD TO PARENT:


# ### IS INSTANCE METHOD : 
# print('is instance ', isinstance(ph2, Flagship)) 
# print('is instance  ', isinstance(ph2, Smartphone)) 
# print('is instance ', isinstance(ph2,Phone)) 
# print('is instance ', isinstance(ph1, Flagship))


# ### IS SUB CLASS METHOD : 
# print('is subclass ', issubclass(Smartphone,Phone))
# print('is subclass ', issubclass(Phone, Smartphone)) 
# print('is subclass ', issubclass(Flagship, Phone)) 
# print('is subclass ', issubclass(Flagship,Flagship)) 


### MULTIPLE INHERITANCE :
class A:
    def class_a_method(self):
        return 'I\'m a class A method'
    
    def hello(self):
        return 'Hello from class A'
    

class B:
    def class_b_method(self):
        return 'I\'m a class B method'
    
    def hello(self):
        return 'Hello from class B'
    
class C(B, A):  # order of parent classes writter in parenthesis matter
    pass


instance_c = C()
print(instance_c.class_a_method())
print(instance_c.class_b_method())
##print(help(C))
print(C.mro())
print(instance_c.hello())  # will excute method of class written first while declearing class C


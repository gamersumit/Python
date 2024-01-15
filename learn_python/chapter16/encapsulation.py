# # Encapsulation :  data + methods for data
# # In python everything is public but to let other devs know that a variable can affect the software if changed we use _vari_name as naming convention
# ## __init__ or __name__ # dunder/ magic methods : IT IS NOT A NAMING CONVENTION

# class Phone:
#     def __init__(self, brand, model_name, price):
#         self.brand = brand
#         self._model_name = model_name
#         self.__price = price  # name mangling : python will change its name due to __ to make it available for only this particular class
#         self.complete_spec = f"{brand} {model_name} and price is: {price}."

#     def make_call(self, number):
#         print(f"calling {number} ...")
    
#     def full_name(self):
#         return f"{self.brand} {self.model_name}"
    
#     # solution to problem1:
#     @property
#     def complete_specification(self):
#         return f"{self.brand} {self._model_name} and price is: {self._Phone__price}."
    
#     # solution for problem2:
#     @property  # getter
#     def model_name(self):
#         return self._model_name
    
#     # setter // should be declared after getter
#     @model_name.setter
#     def model_name(self, new_value):
#         pass


# phone1 = Phone('nokia', '1100', 1000)
# print(phone1.__dict__)
# print(phone1._model_name)
# ## print(phone1.__price)  ## wi;; give error
# print(phone1._Phone__price)
# print(phone1.brand)
# print(phone1.complete_spec)

# #problem 1: change in price will not change price in complete spec variable
# phone1._Phone__price = -500
# print(phone1._Phone__price)
# print(phone1.complete_spec)


# # # -------------- #

# ## To solve this we can make a method named as complete_spec() instead of a variable.
# # also we can use @property decorator to call our complete_spec() method as a variable

# print(phone1.complete_specification)  # we did'nt use paraenthesis 



# # problem 2: we don't want our price to be negative or our modelname should not change, it can be set to neagtive during object initalization and after updation of value
# # to solve this problem we use getter and setter in python

# print(phone1._model_name)
# print(phone1.model_name)
# phone1.model_name = "1200"   # will not be change
# print(phone1._model_name)
# print(phone1.model_name)

# phone1._model_name = "1200"  # will change model name
# print(phone1._model_name)
# print(phone1.model_name)
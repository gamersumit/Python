# # EXCEPTIONS HANDLING :  TRY, EXCEPT, ELSE, FINALLY
# # Erros at runtime may cause exxceptions

# while True:
#     try: 
#         age = int(input("enter your age : ")) # if user enter seven it will create problems
#        # print(f"user\' input is {age} ")
#        # break  # it will only excute when age will be correctly inputted else it will throw exception before break statement

#     except ValueError:   # it will only execute when there will be a value error
#         print("invalid input")
    
#     except :
#         print("Unexpected Error: ")

#     else :  # we can add multiplelines in try but it is a bad practice that's y we write those lines in else block which will be triggred if there is no exception/error
#         print(f"user\' input is {age} ")
#         # before break finally will be executed
#         break

#     finally :  # finally block will always be executed it doesn't matter if there is error or not
#         print(f"finally block")

# if age < 18 :
#     print('you can\'t play this game.')

# else :
#     print('you can play this game')



################################################################    
## EXCERCISE 1:

# def division():
#     while True:
#         a,b = input('enter two number seperated by comma(,): ').split(',')
#         try :
#            a = int(a)
#            b = int(b)
#            return a/b
        
#         except ValueError :
#             print("please enter natural numbers only")
        
#         except ZeroDivisionError as err:
#             print(err)
#             print("can't divide by zero")

#         except :
#             print("unexpected Error")
        
            

# print(division())


################################################################
# CUSTOM Exceptions :

# class CustomErrorName(ValueError):
#     pass

# def validate(name):
#     if len(name) < 8 : raise CustomErrorName('name is too short')

# username = input("Enter username: ")
# validate(username)
# print(f'hello! {username.title()}')

        

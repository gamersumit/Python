import pdb 

## DEBUGGING : Debugging is the process of finding and fixing errors or bugs in the source code of any software. When software does not work as expected, computer programmers study the code to determine why any errors occurred.

## WHY DEBUGGING: 
# 1. OUR PROGRAM IS NOT RUNNING AND CAUSING UNEXPECTED ERRORS.
# 2. OUR PROGRAM IS WORKING BUT NOT AS EXPECTED.


##* STEPS for Debugging: 
# 1. set trace
# 2. execute code line by line


pdb.set_trace()
## pdb commands :
## l line number of trace
## n to go to next line
## q to quit
## c continue -> code will execute in normal mode
name = input("please type your name: ")
age = input("please type your age: ")  # age shoulb be an integer # known mistake to try debugging
print(f"hello {name} your age is {age}")
age2 = age + 5
# age2 = int(age) + 5
print(f"hello {name} you will be {age2} in next five years")


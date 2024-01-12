### Problem 1: Advanced Summation

# def ad_sum(*args):
#     total = 0
#     ls = filter(lambda x: type(x) == list, args)
#     numbers = filter(lambda x: type(x) == int, args)
#     for i in ls: total += sum(i)
    
#     return total+sum(numbers)

# print(ad_sum(1,2,3,4,5,[1,2,8],3,[9]))



########################################################################

### Problem 2: Recursive Concatenation

# def rev_con(*args, **kwargs):
#     concat = ""
#     for sub in args: concat += sub[::-1]
#     return concat.replace(" ","")

# print(rev_con('hello', 'world', 'open ai', 'chatgpt'))

########################################################################

### Problem 3: Weighted average:

# def wei_avg(*args):
#     return sum(map(lambda tup: tup[0]*tup[1], args))

# print(wei_avg((10, 0.3), (20,0.2), (30,0.5)))



########################################################################

### Problem 4: Dynamic Student Information

# def info(**kwargs):
#     for key, value in kwargs.items():
#         print(f" {key.title()} : {value} ")

# info(name = 'bob', age = 21, hobbies = ['reading', 'gaming'])


########################################################################

### Problem 5: Prime Number Checker

# def isPrime(num):
#     for i in range(2,int(num** 0.5)+1):
#         if num % i == 0: return False
#     return True


# inp = [2,3,4,5,6,7,8,9,10]
# ls = list(map(isPrime, inp))
# print(ls)
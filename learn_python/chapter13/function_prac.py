# advance function practice:

# EXAMPLE 1:

avg_list = lambda *args: [(sum(pair) / len(args)) for pair in zip(*args)] 
print(avg_list([1,2,3,4,5,6], [2,4,6,8], [3,6,9], [1,9,2,8], [5,5,5]))
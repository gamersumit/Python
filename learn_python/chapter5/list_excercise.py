def list_input(number):
    total_element = int(input("ENTER NUMBER OF ELEMENTS: "))
    for i in range(total_element):
        ele = int(input("enter element: "))
        number.append(ele)


# excercise 1:

# number = []
# total_element = int(input("ENTER NUMBER OF ELEMENTS: "))

# for i in range(total_element):
#     ele = int(input("enter element: "))
#     number.append(ele)
# square = []
# for i in number:
#     square.append(i**2)

# print(square)


# excercise 2:

# def reverse_list(ori_list):
#     rev_list = []
#     while len(ori_list):
#         rev_list.append(ori_list.pop())
#     return rev_list


# number = []
# total_element = int(input("ENTER NUMBER OF ELEMENTS: "))

# for i in range(total_element):
#     ele = int(input("enter element: "))
#     number.append(ele)

# number.reverse() # this will not return anything
# print(number)
# print(number[::-1])

# print(reverse_list(number))



# excercise 3:

# def rev_element(words):
#     rev_words = []
#     for i in words:
#         rev_words.append(i[::-1])
#     return rev_words

# words = []
# total_element = int(input("ENTER NUMBER OF ELEMENTS: "))

# for i in range(total_element):
#     ele = input("enter element: ")
#     words.append(ele)

# print(rev_element(words))


# excercise 4:

# def odd_even(ori_list):
#     o_e = [[], []]
#     for i in ori_list:
#         if i%2 == 0:
#             o_e[1].append(i)
#         else :
#             o_e[0].append(i)
#     return o_e


# number = []
# total_element = int(input("ENTER NUMBER OF ELEMENTS: "))

# for i in range(total_element):
#     ele = int(input("enter element: "))
#     number.append(ele)

# print(odd_even(number))


# excercise 5:

# def intersection_list(l1, l2):
#     inter = []
#     for i in l1:
#         if i in l2:
#             inter.append(i)
    
#     return inter


# number1 = []
# list_input(number1)

# number2 = []
# list_input(number2)

# print(intersection_list(number1, number2))
        

# excercise 6:

# def total_lists(matrix):
#     count = 0
#     for i in matrix:
#         if(type(i) == list) :
#             count += 1
#     return count

# matrix = [1,2,3,[1,2,3], [5,6], "word", ['word', 'alpha'], []]
# print(total_lists(matrix))
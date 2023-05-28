# print("Hello, World!")
# name = input("What's your name? ")
# print("Hello {}!\nWelcome to Dataquest!".format(name))

# code convention
# https://fireship.io/lessons/code-this-not-that-python-edition/


# todo-1
# t = [[3 - i for i in range(3)] for j in range(3)]
# s = 0
# for i in range(3):
#     s += t[i][i]
# print(s)

# todo-2
# z = 10
# y = 0
# x = y < z and z > y or y > z and z < y
# print(x)

# todo-3
# var = 0
# while var < 6:
#     var += 1
#     if var % 2 == 0:
#         continue
#     print("#")

# todo-4
# i = 0
# while i <= 5:
#     i += 1
#     if i % 2 == 0:
#         break
#     print("*")

# todo-5
# vals = [0, 1, 2]
# vals.insert(0, 1)
# del vals[1]
# print(vals)
# # sum of all elements in a list
# print(sum(vals))

# todo-6
# a = 1
# b = 0
# c = a & b
# d = a | b
# e = a ^ b
# print(c + d + e)

# todo-7
# nums = [1, 2, 3]
# vals = nums[-1:-2]
# print(nums)
# print(vals)

# todo-8
# nums = [1, 2, 3]
# vals = nums
# del vals[1:2]
# print(nums)
# print(vals)

# todo-9
# my_list_1 = [1, 2, 3]
# my_list_2 = []
# for v in my_list_1:
#     my_list_2.insert(0, v)
# print(my_list_2)

# todo-10
# my_list = [[0, 1, 2, 3] for i in range(2)]
# print(my_list[2][0])

# todo-11
# i = 0
# while i <= 3:
#     i += 2
#     print("*")

# todo-12
# vals = [0, 1, 2]
# vals[0], vals[2] = vals[2], vals[0]
# print(vals)

# todo-13
# my_list = [i for i in range(-1, 2)]
# print(my_list)

# todo-14
# for i in range(1):
#     print("#")
# else:
#     print("#")

# todo-15
# var = 1
# while var < 10:
#     print("#")
#     var = var << 1

# todo-16
# my_list = [1, 2, 3]
# for v in range(len(my_list)):
#     my_list.insert(1, my_list[v])
# print(my_list)

# todo-17
# my_list = [1, 2, 3, 4]
# print(my_list[-3:-2])

# todo-18
# my_list = [3, 1, -2]
# print(my_list[my_list[-1]])

# print("hi charm")
# loop=["1", "2", "3", "4", "5", "6", "7"]
# print(len(loop))
# for x in range((len(loop))-1,-1,-2):
#     print(loop[x])
# print ("\n")
# for x in range(6,2,-1):
#     print (x)
# even= [1,2,3,4,5,6,7,8,9,10]
# even_number=[]
# for x in even:
#     if x%2 ==0:
#         even_number.append(x)
# print("even :"+ str(even_number))
#
#
# array = [1,2] #can be mutated (changed)
# tuple =(1,2) #cant be mutated (cannot be changed)
#
# # Functions
# def sayhi(name):
#     return print("hi " + name)
#
# sayhi("sahil")
#
#
# # if else
#
# # if condition:
# #
# # elif condition:
# #
# # else
#
# # can also use and /or in if conditions
#
# number = input("enter a number: ")
# if number == 4:
#     print("itis 4")
# elif number == 7:
#     print("7")
# else:
#     print("nothign")
#

# def maxn(num1, num2,num3):
#     lists= [num1,num2,num3]
#     largest=0
#     for x in lists:
#             if x>largest:
#                 largest = x
#     return largest
#
# print(maxn(4,5,25))

# Dictionary (class in other)

# students ={
#
#     "name": "sukh",
#     "age":"12",
#     5:"numner"
# }
# print(students["name"])
# print(students.get("name"))
# print(students.get("name","Default value if nothing found"))

# name = input("Entera name:")
# while name != "sukh":
#     name = str(input("Entera name:"))
#     if name == "raj":
#         name = "sukh"

#
# list_num=[]
# num= int(input("Enter a number (0 to exit): "))
# list_num.append(num)
# while num != 0:
#     num = int(input("Enter a number (0 to exit): "))
#
#     list_num.append(num)
#
# list_num.pop(len(list_num)-1)
# print(list_num)
#
# list_num.sort(reverse=True)
# print(list_num)
#
# op= input("choose operator")
# add=0
# addn=1
# if op == "+":
#     for x in list_num:
#         add = add+float(x)
# elif op == "-":
#     for x in list_num:
#         add = abs(add)-float(x)
# elif op == "*":
#     for x in list_num:
#
#         addn = addn * float(x)
#
# elif op == "/":
#     # y = list_num[1]
#     # for x in list_num[1:]:
#     #     y=y/x
#     # add=y
#     #
#     add= list_num[0]
#     for x in list_num[1:]:
#         add = add/x
#
#     # for x in list_num:
#     #     if x== list_num[0]:
#     #         add = float(list_num[0])/float(list_num[1])
#     #         print("1")
#     #     elif  x== list_num[1]:
#     #         print("2")
#     #         continue
#     #     else:
#     #         print("3")
#     #         add = add / float(x)
# else:
#     print("nothing")
#
# if op=="*":
#     print(str(addn))
# else:
#     print(str(add))

#
# number_grid=[
#
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
#
# for x in number_grid:
#     for y in x:
#         print(y)
# #or
# for x in range(len(number_grid)):
#     for y in range(len(number_grid[0])):
#         print(number_grid[x][y])


'''
Try and except
'''


# try:
#     value = 10/0
#
#     number = int(input("enter a number: "))
#     print(number)
#
# except ZeroDivisionError:
#     print("CANR DEVIDE WITH ZERO")
# #or
# except ZeroDivisionError as err:
#     print(err)
#
# except ValueError:
#     print("invalid input")
from math import trunc, ceil

'''
Reading fron External file
'''
#
# #modes read r, write w, append a, read+write (r+)
# employee_file = open("employee.txt", "r+" )
#
# # check if file is readable
# filelist= employee_file.readlines()
# if employee_file.readable():
#     for x in filelist:
#         print(x)
# employee_file.write("hello")
#
# employee_file.close()

'''
Write a file(append)
'''
'''
Import another file

import filename

print (filename.variable)

'''
'''
 
Class and objects
'''
#
# from student import stu_class
#
# student1 = stu_class("sukh","computers", 4.0, False)
# student2 = stu_class("sahil","computers", 4.0, True)
# student3 = stu_class("jack","computers", 4.0, False)
# student4 = stu_class("sam","computers", 4.0, True)
#
# stu_list =[
#     student1, student2, student3, student4
# ]


#
# def studentpasschecker(studentname):
#     passConfirm = 0
#     stu_name = ""
#     for x in stu_list:
#         if studentname in (button.name for button in stu_list):
#             if x.name == studentname:
#                 if x.is_passed == True:
#                     passConfirm = 1
#                     stu_name = x.name
#                 else:
#                     stu_name = x.name
#         else:
#             passConfirm =2;
#     if passConfirm ==1:
#         print(stu_name +" is passed")
#     elif passConfirm ==2:
#         print("doesnt ecist")
#     else:
#         print(stu_name +" is failed")
#
# def getInput():
#     value= input("Enter the name: ")
#     return value
#
#
# FinalInput = getInput()
#
# studentpasschecker(FinalInput)

# print(stu_class.if_passed(student2))

# def foo(a, b, c, *therest):
#     allExtra = list(therest)
#     return len(allExtra)
#
# def bar(a, b, c, **options):
#     if options["magicnumber"] == 7:
#         return True
#     else:
#         return False


# test code
# if foo(1, 2, 3, 4) == 1:
#     print("Good.")
# if foo(1, 2, 3, 4, 5) == 2:
#     print("Better.")
# if bar(1, 2, 3, magicnumber=6) == False:
#     print("Great.")
# if bar(1, 2, 3, magicnumber=7) == True:
#     print("Awesome!")


'''
Advanced topics : List comprehension
'''
# list_comprehension =["sahil", "sam", "jack"]
# startsWithS = [ x for x in list_comprehension if x[0] == "s"]
#
# print(startsWithS)

'''
Lambda function
'''
# l = [2,4,7,3,14,19]
# for x in l:
#     oddOrEven = lambda x: (x%2) == 0
#
#     print(oddOrEven(x))

'''

Sets: lists that contain unique value and has many functions, union, difference, intersection, symetric_intersection

'''
# list_for_set = ["one", "two", "three"]
# list_for_set2 = ["four", "five", "three"]
# A = set(list_for_set)
# B = set(list_for_set2)
#
# print (A.intersection(B))
# print(A.difference(B))

# def sum(x,y):
#     return x+y
#
# help(sum(1,2))
# from functools import reduce
#
# my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
# my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
# my_numbers = [4, 6, 9, 23, 5]
# product = 1
#
# map_result = list(map(lambda x: round(x ** 2, 3), my_floats))
# filter_result = list(filter(lambda name: len(name) <= 7, my_names))
# reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers)
#
# map_result2 = [round((x*x),3) for x in my_floats]
# filter_result2 = [x for x in my_names if len(x)<=7]
#
# print(map_result)
# print(filter_result)
# print(reduce_result)
# print(map_result2)
# print(filter_result2)

board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
#
# def print_board():
#     for x in range(3):
#         print(board[x*3: (x+1)*3])
#
# print_board()
# print(board[0*3: (0+1)*3])
# print(board[1*3: (1+1)*3])
# print(board[2*3: (2+1)*3])
#
# list = [1,2,3,4,5,6,7]
# rev_list = []
# leng = len(list)-1
# print(leng)
# for x in range(len(list)):
#     list[x] = list[leng]
#     leng -= 1
# print(list)

'''
1=7
2=6
3=5
4=4
5=3
'''

# print(rev_list)


# arr = [1,2,3,4,7,3,6]
# num = 9
# arr2 = []
# for x in arr:
#     for y in arr:
#         if x+y == num:
#             if [x,y] not in arr2 and [y,x] not in arr2:
#                  arr2.append([x,y])
#
# print(arr2)
#
# for x in arr:
#     if x< num:
#         if (num - x) in arr:
#             if [x, (num-x)] not in arr2 and [(num-x), x] not in arr2:
#                 arr2.append([x,abs(num-x)])
#
# print(arr2)

# arr2 = [
#     [3,4,5,2],
#     [1,2,3,5],
#     [2,34,5,6],
#
# ]
# sum = 0
# sunarr=[]
# for x in arr2:
#     for y in x:
#         sum = sum + y
#     sunarr.append(sum)
#     sum= 0
# print(sunarr)

'''
Fibonacci number
The simplest is the series 1, 1, 2, 3, 5, 8
'''
#
# def feb(x,y):
#     sum = 0
#     one = x
#     two = y
#     arr = [x,y]
#     for x in range(10):
#         sum = one + two
#         one = two
#         two = sum
#         arr.append(sum)
#
#     return arr
# print(feb(1,1))

''''
palindrome '''

# def ifPalindrome(words):
#     word = [x for x in words if x != " "]
#     print(word)
#     # c->a->t
#     # t->a->c
#     start = 0
#     last = len(word) - 1
#     bool = True
#     for x in range(ceil(last/2)):
#
#         if word[start] == word[last]:
#             start +=1
#             last-=1
#         else:
#             bool = False
#
#
#     return bool
#
#
# print(ifPalindrome("abcba"))

'''
Find the first repeating char

'''
# string = "abcbab"
# string_array = [x for x in string]
# DuplicateCheck =[]
# Duplicates =[]
# for x in string:
#     if x not in DuplicateCheck:
#         DuplicateCheck.append(x)
#         string_array.pop(string_array.index(x))
#     else:
#         if x not in Duplicates:
#             Duplicates.append(x)
#             string_array.pop(string_array.index(x))
# print(string_array)
# print(DuplicateCheck)
# print(Duplicates)

'''
Finding non duplicate
'''
#
# string = "abbzazb"
# string_array = [x for x in string]
# unique = []
# for x in range(len(string_array)):
#     if x>0:
#         if string_array[x] not in string_array[x+1::] and string_array[x] not in string_array[:x]:
#             # print(string_array[x] + " is unique")
#             unique.append(string_array[x])
#             break
#     else:
#         if string_array[x] not in string_array[x+1::]:
#             # print(string_array[x] + " is unique")
#             unique.append(string_array[x])
#             break
# if len(unique)>0:
#     print(unique)
# else:
#     print("No unique char")




#
# for x in range(1,9):
#     print(x)
'''
ADD TWO BINAY NUMBERS
'''
# num1 ="517"
# num2= "12933"
# carry = 0
# addition = []
# for x in range(len(num1)-1,-1,-1):
#     total = int(num1[x]) + int(num2[x]) + carry
#     carry =0
#     if total>9:
#         carry =1
#         total = total-10
#     addition.insert(0,total)
#     # addition.append(total)
#
#
# print(addition)


# total = num1+ num2
# print(total)

'''
check if a number is a power of 2 suk as 4 8'''


#
# def check(target):
#     isfound= False
#     total = 1
#     while True:
#         total = total*2
#         if total == target:
#             # isfound = True
#             return True
#         if total> target:
#             return False
#
# print(check(6))
# import random
#
# box = []
#
# for x in range(9):
#     box.append(' ')
#
# def printbox():
#
#     for x in range(3):
#         print(' | '.join(box[x*3:(x+1)* 3]))
#
#
# def printnumericbox():
#     box = []
#     for x in range(9):
#         box.append(str(x))
#     for x in range(3):
#         print(' | '.join(box[x*3:(x+1)* 3]))
#
# def availableMoves():
#     array= []
#     index = 0
#     for x in box:
#         if x == ' ':
#             array.append(index)
#         index +=1
#     return array
#
#
# def is_won(index, player):
#     #check row, column and diagonal
#     row_ind = index//3
#     row = box[row_ind *3: (row_ind+1) *3]
#     if all(spot == player for spot in row):
#         return True
#
#     #check Column
#     col_ind = index%3
#     col = [box[col_ind + x * 3] for x in range(3)]
#     if all(spot == player for spot in col):
#         return True
#
#     #check diagonal 0,4,8 or 2,4,6    so 0,2,4,6,8
#
#     if index %2 ==0:
#         d_one = [box[x] for x in [0,4,8]]
#         if all(spot == player for spot in d_one):
#             return True
#         d_two = [box[x] for x in [2, 4, 6]]
#         if all(spot == player for spot in d_two):
#             return True
#
#
# def playgame():
#     printnumericbox()
#     print("---------")
#     won = False
#
#     while(won!=True):
#
#         printbox()
#         userImput = int(input("Enter your input(0-8): "))
#         if userImput not in range(0,9):
#             print("Only enter between 0-8")
#             continue
#         if userImput in range(0,9) and userImput not in availableMoves():
#             print("That option is already filled.")
#             continue
#         box[int(userImput)] = 'X'
#
#         if is_won(userImput, 'X'):
#             print("X win")
#             won=True
#
#         if len(availableMoves())>0:
#             computerInput = random.choice(availableMoves())
#
#             box[computerInput] = 'O'
#             if is_won(computerInput, 'O'):
#                 print("computer win")
#                 won = True
#
# playgame()


def twoSum(nums, target):
    result = []
    for x in range(len(nums)):
        for y in range(len(nums)):
            if nums[x] + nums[y] == target:
                if nums[x] + nums[y] not in result and nums[y] + nums[x] not in result:
                    result = [nums[x] , nums[y]]
    return result

arr =[2,4,3]
num = 6
arr2 =[]

for x in arr:
    if x< num:
        if (num - x) in arr:
            if [x, (num-x)] not in arr2 and [(num-x), x] not in arr2:
                arr2= [x,abs(num-x)]
print(arr2)
str_a = "hello"
for i in str_a:
    print(i)

lst_a = ["a", "b", "c", "d"]
for i in lst_a:
    print(i)

tpl_a = ("e", "f", "g")
for i in tpl_a:
    print(i)

str_x = "xyz"
str_y = "abc"
for i in str_x:
    print(i)
for i in str_y:
    print(i)

str_x = "xyz"
str_y = "abc"
for i in str_x:
    for j in str_y:
        print((i,j))

# Reverse str_a=“John is clever”
# str_a = "John is clever"
# res = []
# splt_stra = str_a.split(" ")  # ['John', 'is', 'clever']
# print("the string after splitting is {}".format(splt_stra))
# for i in splt_stra:
    # x = i[::-1]
    # print(x)
    # res.append(x)
# print(res)     ['nhoJ', 'si', 'revelc']
# rev_str = " ".join(res)
# print("the rev string is {}".format(rev_str))

str_a = "John is clever"
res = []
splt_stra = str_a.split(" ")
for i in splt_stra:
    res.append(i[::-1])
rev_str = " ".join(res)
print("the rev string is {}".format(rev_str))

# list comprehension
str_a = "John is clever"
res_lst = [i[::-1] for i in str_a.split(" ")]         # list comprehension
print(res_lst)
reversed_str = " ".join(res_lst)
print("the rev string is {}".format(reversed_str))


# squares of elements in list

lst_to_sqr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sqr_lst = []
for i in lst_to_sqr:
    sqr_lst.append(i*i)
print("the squared values is {}".format(sqr_lst))

# squares with list comprehension
lst_to_sqr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sqrd_lst = [i**2 for i in lst_to_sqr]
print("The squared value of list items is {}".format(sqrd_lst))

for i in range(0, 5):
    print(i)
for i in range(1, 10):
    print(i)
for i in range(1, 10, 2):
    print(i)

# square the numbers from 1 to 9
lst_sqr = [i**2 for i in range(1, 10)]
print("The square from range 1 to 10 is {}".format(lst_sqr))
# print([i**2 for i in range(1, 10)])

# sum from 1 to 10
lst_to_sum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
summation = 0
for i in lst_to_sum:
    summation = summation+i
print("The sum of all items in list is {}".format(summation))

# using range function
sum_of_items = 0
for i in range(1, 11):
    sum_of_items = sum_of_items+i
print("The sum of range of items from 1 to 11 is {}".format(sum_of_items))


# find the cubes
# find the sum from range 1, 100

str_x = "Python"
len_str_x = len(str_x)
for i in range(0,len_str_x):
    print("The value of {} index is {}".format(i, str_x[i]))

lst_x = [1, 2, 3, 4]
lst_y = [5, 6, 7, 8]
len_lst_x = len(lst_x)
sum_lst_x_y = []
for i in range(0, len_lst_x):
    summation = lst_x[i]+lst_y[i]
    sum_lst_x_y.append(summation)
print("the sum of two lists are {}".format(sum_lst_x_y))

"""
len_lst_x = 4   
1st iteration i = 0-->summation=lst_x[0]+lst_y[0]=1+5=6--->>sum_lst_x_y=[6]
2nd iteration i = 1-->summation=lst_x[1]+lst_y[1]=2+6=8--->>sum_lst_x_y=[6,8]
3rd iteration i = 2-->summation=lst_x[2]+lst_y[2]=3+7=10--->>sum_lst_x_y=[6,8,10]
4th iteration i = 3-->summation=lst_x[3]+lst_y[3]=4+8=12--->>sum_lst_x_y=[6,8,10,12]
"""

lst_x = [1, 2, 3, 4]
lst_y = [5, 6, 7, 8]
summation = [lst_x[i]+lst_y[i] for i in range(0, len(lst_y))]
print("the sum of two lists is {}".format(summation))

# count of characters
str_y = "Alex is in class"
for i in str_y:
    cnt = str_y.count(i)
    print("The character {} occured {} time".format(i, cnt))

# reverse string without string
str_y = "hello"
rev_str = ""              # empty string
for i in str_y:
    rev_str = i+rev_str
print("the value after reversing string is {}".format(rev_str))

"""
1st iteration i = "h" ---->rev_str="h"+""="h"
2nd iteration i = "e" ---->rev_str="e"+"h"="eh"
3rd iteration i = "l" ---->rev_str="l"+"eh"="leh"
4th iteration i = "l" ---->rev_str="l"+"leh"="lleh"
5th iteration i = "o" ---->rev_str="o"+"lleh"="olleh"
"""


# list all keys and values of dictionary
dict_x = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
keys=[]
values = []
for key, val in dict_x.items():
    keys.append(key)
    values.append(val)
print("The keys are {} and values are {}".format(keys, values))


lst_a = ["name", "age", "salary"]
lst_b = ["John", 27, 50000]
dict_y = dict()
if len(lst_b)==len(lst_a):
    for i in range(len(lst_b)):
        dict_y[lst_a[i]] = lst_b[i]
print("The dictionary out of lists is {}".format(dict_y))


# count characters in a string
str_a = "John is brave and topper of class"
dict_cnt = {i: str_a.count(i) for i in str_a}
print("The count of characters in string is {}".format(dict_cnt))
# print only the repeated characters count
dict_rep = {i: str_a.count(i) for i in str_a if str_a.count(i)>1}
print("The repeated characters are {}".format(dict_rep))

"""
n= 5
output
*
**
***
****
*****
"""
n= 5
lst = []
for i in range(1, n+1):
    lst.append("*"*i)
print(lst)
print("\n".join(lst))


"""
n= 5
output
*
**
***
****
*****
****
***
**
*
"""

# find prime numbers from 1 to 20
















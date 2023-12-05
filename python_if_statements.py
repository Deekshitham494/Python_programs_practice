a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

if a > b:
    diff = a-b
    print(diff)
elif a < b:
    summation = a+b
    print(summation)

# another way of writing above code
if a > b:
    diff = a-b
    print(diff)
else:
    summation = a+b
    print(summation)

# if condition is only required irrespective of else part
if a > b:
    diff = a-b
    print(diff)

lst_x = [1, 2, 3, 4]
lst_y = [5, 6, 7, 8]
len_lst_x = len(lst_x)
sum_lst_x_y = []
if len(lst_x)==len(lst_y):
    for i in range(0, len_lst_x):
        summation = lst_x[i] + lst_y[i]
        sum_lst_x_y.append(summation)
print("the sum of two list are {}".format(sum_lst_x_y))

# using list comprehension
lst_a = [1, 2, 3, 4]
lst_b = [5, 6, 7, 8]
summation = [lst_a[i]+lst_b[i] for i in range(0,len(lst_b)) if len(lst_a)==len(lst_b)]
print("the sum of two lists using list comprehension is {}".format(summation))


# if lists legths are not same

lst_x = [1, 2, 3, 4, 5]
lst_y = [5, 6, 7, 8]
len_lst_x = len(lst_x)
sum_lst_x_y = []
if len(lst_x)==len(lst_y):
    for i in range(0, len_lst_x):
        summation = lst_x[i] + lst_y[i]
        sum_lst_x_y.append(summation)
print("the sum of two list are {}".format(sum_lst_x_y))

# check given string is palindrome or not
str_to_check = input("Enter the value: ")
str_rev = str_to_check[::-1]
if str_to_check == str_rev:
    print("the given string is palindrome")
elif str_to_check != str_rev:
    print("The given string is not a palindrome")

str_a = input("Enter the value: ")
if str_a == str_a[::-1]:
    print("The given string is palindrome")
else:
    print("The given string is not palindrome")

# check whether the given number is even or odd
num_to_check = int(input("Enter the value: "))
if num_to_check % 2 == 0:
    print("The given number is even")
else:
    print("The given number is odd")

#  make a list of even numbers and list of odd numbers from 0 to 20
# even_lst = []    odd_lst = []
even_lst = []
odd_lst = []
for i in range(0, 20):
    if i % 2 == 0:
        even_lst.append(i)
    else:
        odd_lst.append(i)
print("The even numbers from 0 to 20 is {}".format(even_lst))
print("The odd numbers from 0 to 20 is {}".format(odd_lst))

# find the largest among a,b,c numbers
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
if a > b and a > c:
    print("a is greater")
elif b > a and b > c:
    print("b is greater")
else:
    print("c is greater")

lst_y = [2, 4, 3, 2, 5, 3, 6, 7]
res_lst = []
for i in lst_y:
    if i not in res_lst:
        res_lst.append(i)
print("The list after removing duplicates is {}".format(res_lst))

# sort numbers
lst_c = [23, 78, 12, 10, 56, 90, 50]
for i in range(0, len(lst_c)-1):
    for j in range(i+1, len(lst_c)):
        if lst_c[i] > lst_c[j]:
            lst_c[i], lst_c[j] = lst_c[j], lst_c[i]
            # temp = lst_c[i]
            # lst_c[i] = lst_c[j]
            # lst_c[j] = temp
print("The list after sorting is {}".format(lst_c))
print("the maximum value is {}".format(lst_c[-1]))
print("The minimum value is {}".format(lst_c[0]))

"""
1st iteration i = 0 ---> j 1 to len(lst_c)
2nd iteration i = 1----> j 2 to len(lst_c)
3rd iteration i = 2----> j 3 to len(lst_c)
4th iteration i = 3----> j 4 to len(lst_c)
5th iteration i = 4----> j 5 to len(lst_c)
6th iteration i = 5----> j 6 to len(lst_c)

1st iteration i = 0 
    2nd loop j = 1
        lst_c[i] = lst_c[0]=23  lst_c[j]=lst_c[1]=78
        23>78 doesnot satisfy
    j=2
            lst_c[0]=23 lst_c[2]=12
            23>12
            lst_c = [12, 78, 23, 10, 56, 90, 50]
    j = 3
        lst_c[0]=12 lst_c[3]=10
        12>10
        lst_c = [10, 78, 23, 12, 56, 90, 50]
    j = 4
        lst_c[0] = 10 lst_c[4] = 56
        10>56 no
    j = 5
        lst_c[0]=10 lst_c[5] =90
        10>90 no
    j = 6 
        lst_c[0]=10 lst_c[6]= 50
        10>50 no
i = 1
    j = 2
        lst_c[1]=78 lst_c[2]=23
        78>23
        lst_c= [10, 23, 78, 12, 56, 90, 50]
    j = 3
        lst_c[1]=23 lst_c[3]= 12
        23>12
        lst_c = [10, 12, 78, 23, 56, 90, 50]
    j = 4
        lst_c[1]= 12 lst_c[4]= 56
        12>56 no
    j= 5
        lst_c[1]= 12 lst_c[5] = 90
        12>90 no
    j = 6
        lst_c[1] = 12 lst_c[6] = 50
        12>50 no
i = 2
    j = 3
    lst_c[2]= 78 lst_c[3] = 23
    78>23
    lst_c = [10, 12, 23, 78, 56, 90, 50]
    j = 4
    lst_c[2]= 23 lst_c[4]= 56
    23>56 no
    j = 5
    lst_c[2]=23 lst_c[5]=90
    23>90 no
    j= 6
    lst_c[2]=23 lst_c[6]=50
    23>50 no
i = 3
    j = 4
    lst_c[3]=78 lst_c[4]=56
    78>56
    lst_c = [10, 12, 23, 56, 78, 90, 50]
    j = 5
    lst_c[3] = 56 lst_c[5]= 90
    56>90
    j= 6
    lst_c[3] = 56 lst_c[6] = 50
    56>50
    lst_c = [10, 12, 23, 50, 78, 90, 56]
i = 4
    j = 5
    lst_c[4] = 78 lst_c[5]= 90
    78>90
    j = 6
    lst_c[4]=78 lst_c[6] = 56
    78>56
    lst_c = [10, 12, 23, 50, 56, 90, 78]
i = 5
    j = 6
    lst_c[5]= 90 lst_c[6]=78
    90>78
    lst_c = [10, 12, 23, 50, 56, 78, 90]
"""
"""
What is List?
List is a group of elements which can be alphabet, numeric or alpha numeric or combination of all the 3.
List is mutable.
List is enclosed between []

NOTE: List is mutable since it creates extra memory space once it is defined
"""
lst_a = ["a", "b", 1, 3]
emp_lst = []      # One kind of definig empty list
print("One kind of empty list is {}".format(emp_lst))
empt_lst = list()      # Another kind of empty list
print("Another kind of definig empty list is {}".format(empt_lst))


# to find length of list
lst_x =["a", "b", "c", 1, 2]
len_lstx = len(lst_x)
print("Length of list x is {}".format(len_lstx))

# to find type
print("The of the variable is {}".format(type(lst_x)))

lst_y = ["1", "2", "python", 123, "@abc"]
len_lsty = len(lst_y)
print("The length of list is {}".format(len_lsty))

# Indexing of lst_y
ind0_lsty = lst_y[0]
print("The zeroeth index of lst_y is {}".format(ind0_lsty))
ind1_lsty = lst_y[1]
print("The first index of lst_y is {}".format(ind1_lsty))
ind2_lsty = lst_y[2]
print("The second index of lst_y is {}".format(ind2_lsty))
ind3_lsty = lst_y[3]
print("the third index of lst_y is {}".format(ind3_lsty))
ind4_lsty = lst_y[4]
print("The fourth index of lst_y is {}".format(ind4_lsty))

# To print h from python which is an item of lst_y
lst_y = ["1", "2", "python", 123, "@abc"]
lst_python = lst_y[2]
print("the value is {}".format(lst_python))
lsty_h = lst_python[3]
print("The value is {}".format(lsty_h))
lst_y_h = lst_y[2][3]
print("Another way of indexing {}".format(lst_y_h))
lst_y[3] = 456
print("The lst_y after changing the value is {}".format(lst_y))

"""
append: 
        * we can add only 1 element at a time using append command
        * append is faster since it adds only one element and there is no internal iterations performed
        * Time complexity is less
"""
lst_y.append(123)
print("the value of lst_y after appending is {}".format(lst_y))

"""
extend: 
        * We can add n number elements at a time using extend command
        * Extend is slower compared to append since it iterates through out the elements it needs to be added
        * Time complexity is more
"""
lst_y.extend(["a", "b"])
print("The lst_y after extending is {}".format(lst_y))

lst_y.extend([["3", "4"]])
print("the value of lst_y after extending list is {}".format(lst_y))


lst_a = ["1", "2", "3", "a"]
lst_a[3] = "4"
print("The list value after changing is {}".format(lst_a))

lst_b = ["a", "b", "c"]
lst_b.extend(["d","e"])
print(lst_b)

# Item Reversing in list
str_a = "Welcome class"    #  output:    "emocleW ssalc"
str_a_lst = str_a.split(" ")
print("The list after splitting the string is {}".format(str_a_lst))
# lst_ind0 = str_a_lst[0]
# print(lst_ind0)
# rev_ind0 = lst_ind0[::-1]
# print(rev_ind0)
# str_a_lst[0] = rev_ind0
# print(str_a_lst)
str_a_lst[0]= str_a_lst[0][::-1]
str_a_lst[1] = str_a_lst[1][::-1]
print(str_a_lst)
str_a_rev = " ".join(str_a_lst)
print("the value after reversing items is {}".format(str_a_rev))

lst_x = [1, 2, ["a", "b", "python"], 3, 4]
lst_x[2][2] = lst_x[2][2][::-1]
print(lst_x)

lst_z = ["a", "b", ["john", "class", "Alex"], 4, 5, 7] # outpt = ["a", "b", ["john", "ssalc", "Alex"], 4, 5, 7]

# deleting methods

# clear - it clears all the elements in the lists
lsta = [1, 2, 3]
lsta.clear()
print("List after clearing is {}".format(lsta))

# pop - it deletes last index value
lstb = ["a", "b", "c", "d"]
lstb.pop()
print("The list after pop is {}".format(lstb))
lstb.pop()
print("The list after pop is {}".format(lstb))

# remove - we can specify which item or element to be deleted from list

lstc = ["John", "Bob", "Alex", "xyz"]
lstc.remove("Bob")
print("The value after removing Bob from list is {}".format(lstc))
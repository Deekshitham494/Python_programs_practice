"""
What is string?
Strings are immutable data type. a string is a sequence of characters or a sequence of elements, which can be
a alphabet, alpha numeric or it can be combination of all two.
String is enclosed between " or '

NOTE: String is immutable since it creates memory space only for the elements defined
"""

empty_string = ""
str_a = "python"
str_n = "1234"
str_s = " "
str_an = "python3.9"

len_str = len(str_an)
print("The length of string is {}".format(len_str))
type_str = type(str_an)
print("The type of variable str_an is {}".format(type_str))

# Indexing

str_x = "python"
strx_zeroeth_ind = str_x[0]
print("Zeroeth index value of a strx is {}".format(strx_zeroeth_ind))
strx_fst_ind = str_x[1]
print("Fist index value of strx is {}".format(strx_fst_ind))
strx_sec_ind = str_x[2]
print("Second index value of strx is {}".format(strx_sec_ind))
strx_thrd_ind = str_x[3]
print("Third index value of strx is {}".format(strx_thrd_ind))
strx_frth_ind = str_x[4]
print("Fourth index value of strx is {}".format(strx_frth_ind))
strx_fifth_ind = str_x[5]
print("Fifth index value of strx is {}".format(strx_fifth_ind))

# Slicing

str_y = "welcome to class"
ind0_to_ind4 = str_y[0:4]
print("The value of string from zero to fourth index is {}".format(ind0_to_ind4))
ind1_to_ind5 = str_y[1:5]
print("The value of string from first to fifth index is {}".format(ind1_to_ind5))
ind0_to_ind3 = str_y[0:3]
print("the value of string from zero to third index is {}".format(ind0_to_ind3))

# slicing with step size
str_z = "welcome"
len_strz = len(str_z)
print(len_strz)
slc_with_stp2 = str_z[0:7:2]      # length of stry is 7
print("the value of slicing str z with step size 2 is {}".format(slc_with_stp2))
slc_with_stp3 = str_z[0:7:3]
print("the value of slicing str z with step size 3 is {}".format(slc_with_stp3))

# slicing all from right or left
ind3_to_all = str_z[3:]
print("Value from 3rd index to all is {}".format(ind3_to_all))
till_ind5 = str_z[:5]
print("value till 5th index is {}".format(till_ind5))

# Reverse indexing
str_c = "python"
ind1_neg = str_c[-1]
print("Value of negative index one is {}".format(ind1_neg))
ind2_neg = str_c[-2]
print("Value of negative index two is {}".format(ind2_neg))
ind3_neg = str_c[-3]
print("value of negative index three is {}".format(ind3_neg))
ind4_neg = str_c[-4]
print("value of negative index four is {}".format(ind4_neg))
ind5_neg = str_c[-5]
print("Valule of negative index five is {}".format(ind5_neg))
ind6_neg = str_c[-6]
print("Value of negative index six is {}".format(ind6_neg))


# Reverse slicing

str_c_slc = str_c[4:1:-1]
print("value of slicing from one to four in reverse format is {}".format(str_c_slc))

# str_d = "welcome"
# str_d_slc = str_d[6:1:-1]
# print("value of slicing from two to six in reverse format is {}".format(str_d_slc))


str_rev = str_c[::-1]
print("Reversing str c is {}".format(str_rev))

# String concatination
str1 = "welcome"
str2 = "John"
str_res = str1+" "+str2
print("Value after concatinating is {}".format(str_res))

# capitalize - it will capitalize first character of string

str_a = "python"
a = str_a.capitalize()
print("Value after capitalizing string is {}".format(a))

# upper case - it converts complete characters in a string into upper case
upp_case = str_a.upper()
print("Upper case values are {}".format(upp_case))

# lower case - it converts complete characters in a string into lower case
str_b = "WelCoME"
low_case = str_b.lower()
print("Lower case values are {}".format(low_case))

str_c = "hello"
res = str_c[0:2]+str_c[2:4].upper()+str_c[-1]
print("Value after capitalizing only l is {}".format(res))

# to check whether given string is upper
print("The string is upper {}".format(res.isupper()))
str_upp = "HELLO"
print("The string is upper {}".format(str_upp.isupper()))


# to check whether given string is lower
print("The string is lower {}".format(res.islower()))
str_low = "hello"
print("The string is lower {}".format(str_low.islower()))

# Title - it will convert into title
str_x = "welcome to python"
tit_str = str_x.title()
print("The value converting it into title is {}".format(tit_str))

# to check whether it is a title or not
print("The string is title {}".format(str_x.istitle()))
print("The string is title {}".format(tit_str.istitle()))

# count
str_a = "welcome"
print("The count of w in string a is {}".format(str_a.count("w")))
print("The count of e in string a is {}".format(str_a.count("e")))

str_x = "Hello, welcome to class!"
print("The count of l in str x is {}".format(str_x.count("l")))

# index
print("Index value of w in str x is {}".format(str_x.index("w")))
print("Index value of l in str x is {}".format(str_x.index("l")))

# starts with
str_a = "hello"
print("The string is starting with h is {}".format(str_a.startswith("h")))
print("the string is starting with i is {}".format(str_a.startswith("i")))

# Ends with
print("the string is ending with o is {}".format(str_a.endswith("o")))
print("The string is ending with h is {}".format(str_a.endswith("h")))

# split

str_a = "welcome to class"
str_a_split = str_a.split(" ")
print("The value of string after splitting is {}".format(str_a_split))
print("The type after splitting string is {}".format(type(str_a_split)))

# join

str_b = " ".join(str_a_split)
print("The value after joining list of elements is {}".format(str_b))

str_c = "John. Welcome!"
str_c_spl = str_c.split(".")
print("The value after splitting strong with . is {}".format(str_c_spl))


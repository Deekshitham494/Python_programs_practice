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

str_y = "welcome to class"
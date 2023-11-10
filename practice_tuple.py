"""
What is tuple?
Tuple is immutable, tuples are used to store multiple items or elements or a data in a single variable.
It can be a combination of alphabet, numeric or alpha numeric or combination of all three
Tuples are enclosed between ()

NOTE: Tuple is immutable since it creates memory space only for the defined elements hence we can't add
or change elements
"""

tpl_emp1 = ()   # One way of defining empty tuple
tpl_emp = tuple()  # Another way of defining empty tuple

tpl_a = ("a", "b", 1, "python")
print("The items of tuple is {}".format(tpl_a))

# Length of tuple
len_tpl_a = len(tpl_a)
print("The length of tuple a is {}".format(len_tpl_a))

# Type of tpl
type_tpl_a = type(tpl_a)
print("The type is {}".format(type_tpl_a))

# difference between list and tuple
"""
List:
    * List is mutable
    * List creates extra heap space memory once it is defined
    * List is slow
    * Time complexity is more
    * Once defined elements can be changed
    * List can be appended and extended


Tuple:
    * Tuple is immutable
    * Tuple creates heap space memory only for the defined elements
    * Tuple is faster
    * Time complexity is less
    * Once defined elements cannot be changed
    * Tuple cannot be extended or appended
"""

# indexing
ind0_tpl_a = tpl_a[0]
print("Zeroeth element of tuple a is {}".format(ind0_tpl_a))
ind1_tpl_a = tpl_a[1]
print("First element of tuple a is {}".format(ind1_tpl_a))
ind2_tpl_a = tpl_a[2]
print("Second element of tuple a is {}".format(ind2_tpl_a))
ind3_tpl_a = tpl_a[3]
print("Third element of tuple a is {}".format(ind3_tpl_a))
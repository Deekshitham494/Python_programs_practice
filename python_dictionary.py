"""
What is dictionary?
A dictionary is a ordered collection, which is mutable, but it doenot allow duplicates.
Dictionaries are used to store data as key value pairs.

Note: Dictionary itself is mutable but keys in dictionary are immutable(we can delete entire key value pair
but cannot change key)
"""

emp_dict = {}
emp_dict1 = dict()
print("The empty dictionary using inbuilt function is {}".format(emp_dict1))
dict_a = {"name": "John", "Age": 25}     # name is key  and John is value of name
type_dic = type(dict_a)
print("The type is {}".format(type_dic))
len_dic = len(dict_a)
print("the length of dictionary is {}".format(len_dic))
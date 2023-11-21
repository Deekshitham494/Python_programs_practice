"""
What is dictionary?
A dictionary is ordered collection, which is mutable, but it doesnot allow duplicates.
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

dict_a = {"name": "John", "Age": 25}
val_name = dict_a["name"]
print("The value of name is {}".format(val_name))

val_age = dict_a["Age"]
print("The value of age is {}".format(val_age))

# val_sal = dict_a["salary"]
# print("The value of salary is {}".format(val_sal))

dict_b = {"apple": "Its red in color", "Banana": "Its yellow in color"}
val_apple = dict_b.get("apple")
print("The value of key apple is {}".format(val_apple))

val_grape = dict_b.get("grapes")
print("the value of grapes is {}".format(val_grape))

"""
When we use get key word to fetch a value, if there is no existing key it will return None.
When we use normal assignment method to fetch a value, if there is no existing key it will throw an error
"""

dict_a["name"] = "Alex"
print("The value after changing value is {}".format(dict_a))

dict_a["salary"] = 25000
print("the value of dict_a is {}".format(dict_a))

dict_a.update({"emp code": 168087})
print("The value of dictionary after updating is {}".format(dict_a))

dict_c = {"fruits": ["Apple", "Banana", "Orange"], "Vegetables": {"green": "peas", "red": "carrot"}}
dict_frt_get = dict_c.get("fruits")
print("The value of fruits using get  method is {}".format(dict_frt_get))
dict_frt = dict_c["fruits"]
print("The value of fruits is {}".format(dict_frt))

dict_veg_get = dict_c.get("Vegetables")
print("the value of vegetables using get method is {}".format(dict_veg_get))
dict_veg = dict_c["Vegetables"]
print("The value of vegetables is {}".format(dict_veg))

dict_red_get = dict_c.get("Vegetables").get("red")
print("the value of key red using get is {}".format(dict_red_get))
dict_red = dict_c["Vegetables"]["red"]
print("The value of key red is {}".format(dict_red))

car_details = {"name": "Maruthi 800", "Manufacture year": 2000, "Engine": "Diesel", "Color": "White"}
# to fetch keys
keys_dict = car_details.keys()
print("the keys of car detais are {}".format(keys_dict))
lst_dict_keys = list(car_details.keys())
print("The list of keys of car details are {}".format(lst_dict_keys))
# to fetch values
val_dict = list(car_details.values())
print("the list of values of car details are {}".format(val_dict))

# items
item_car_det = list(car_details.items())
print("The items of car details are {}".format(item_car_det))

# clear - it deletes all the items ot key value pair of dictionary
dict_a = {"name": "John", "Age": 25}
dict_a.clear()
print("the value after clearing items {}".format(dict_a))

# pop - it deletes particular key mentioned to delete
car_details = {"name": "Maruthi 800", "Manufacture year": 2000, "Engine": "Diesel", "Color": "White"}
car_details.pop("Engine")
print("the dictionary after deleting engine key value pair is {}".format(car_details))

# popitem - it deletes last item or last key value pair
car_details.popitem()
print("The value of dict after popitem is {}".format(car_details))

dict_x = {"fruits": ["apple", "banana"]}
dict_val = dict_x.get("fruits")
print(dict_val)                 # ['apple', 'banana']
dict_val.extend(["grapes", "orange"])
print(dict_val)
dict_x["fruits"] = dict_val
print("the value of dict_x after extending is {}".format(dict_x))

